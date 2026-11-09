"""Offline CLI regressions using synthetic input in disposable directories."""
import builtins
import contextlib
import io
import os
from pathlib import Path
import runpy
import socket
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile


SCRIPT = Path(__file__).resolve().parents[1] / "convert_skills.py"
FIXTURE = """## Metadata
- **Folder**: example
## Description
A harmless conversion fixture.
## Trigger Phrases
`example`
## Instructions for Claude
Keep this synthetic instruction.
"""


class ConverterCliTests(unittest.TestCase):
    def run_cli(self, root, *args):
        original_import = builtins.__import__

        def without_yaml(name, *positional, **kwargs):
            if name == "yaml" or name.startswith("yaml."):
                raise ImportError("PyYAML deliberately unavailable in this test")
            return original_import(name, *positional, **kwargs)

        output = io.StringIO()
        previous = Path.cwd()
        try:
            os.chdir(root)
            with patch.object(builtins, "__import__", side_effect=without_yaml), \
                    patch.object(subprocess, "check_call", side_effect=AssertionError("installer forbidden")), \
                    patch.object(subprocess, "Popen", side_effect=AssertionError("child process forbidden")), \
                    patch.object(socket, "socket", side_effect=AssertionError("network forbidden")), \
                    patch.object(sys, "argv", [str(SCRIPT), *args]), \
                    contextlib.redirect_stdout(output):
                runpy.run_path(str(SCRIPT), run_name="__main__")
        finally:
            os.chdir(previous)
        return output.getvalue()

    def temporary_directory(self):
        return tempfile.TemporaryDirectory(dir=os.environ.get("TMPDIR"))

    def test_missing_input_does_not_install_dependencies(self):
        with self.temporary_directory() as directory:
            root = Path(directory)
            output = self.run_cli(root)
            self.assertIn("Carpeta no encontrada", output)
            self.assertEqual(list(root.iterdir()), [])

    def test_debug_does_not_write_or_install(self):
        with self.temporary_directory() as directory:
            root = Path(directory)
            source = root / "skills" / "example" / "SKILL.md"
            source.parent.mkdir(parents=True)
            source.write_text(FIXTURE, encoding="utf-8")
            output = self.run_cli(root, "--debug")
            self.assertIn("DEBUG", output)
            self.assertEqual(source.read_text(encoding="utf-8"), FIXTURE)
            self.assertFalse((root / "skills-converted").exists())
            self.assertFalse((root / "skills-zip").exists())

    def test_conversion_and_zip_work_without_yaml(self):
        with self.temporary_directory() as directory:
            root = Path(directory)
            source = root / "skills" / "example" / "SKILL.md"
            source.parent.mkdir(parents=True)
            source.write_text(FIXTURE, encoding="utf-8")
            self.run_cli(root)
            converted = root / "skills-converted" / "example" / "SKILL.md"
            text = converted.read_text(encoding="utf-8")
            self.assertIn("name: example", text)
            self.assertIn("A harmless conversion fixture.", text)
            self.assertIn("Keep this synthetic instruction.", text)
            with zipfile.ZipFile(root / "skills-zip" / "example.zip") as archive:
                self.assertEqual(archive.namelist(), ["example/SKILL.md"])
                self.assertEqual(archive.read("example/SKILL.md"), converted.read_bytes())
            self.assertEqual(source.read_text(encoding="utf-8"), FIXTURE)


if __name__ == "__main__":
    unittest.main()
