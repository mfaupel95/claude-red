# Converter regression tests

Run from the repository root with Python 3.10 or newer:

    python -B -m unittest discover -s tests -p test_converter.py -v

The converter uses only the Python standard library. It must not install
packages at startup, including when input is absent or `--debug` is requested.
PyYAML is not needed: the converter builds its output text directly.

These tests execute the actual CLI entry point with PyYAML deliberately
unavailable. Installer calls, child process creation and socket creation are
replaced with failing guards before the entry point runs. Input, converted
output and ZIP archives use synthetic content in disposable directories under
`TMPDIR` when configured. The original working directory is always restored.
No repository skills, installed packages, credentials or services are used.

Coverage includes absent input, read-only debug mode and conversion with ZIP
content verification. This is a regression suite for the startup dependency
behavior, not a sandbox for arbitrary code or a complete YAML/parser audit.
