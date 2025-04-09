# file: isort/exceptions.py:163-168
# asked: {"lines": [163, 164, 166, 167, 168], "branches": []}
# gained: {"lines": [163, 164, 166, 167, 168], "branches": []}

import pytest
from isort.exceptions import UnsupportedEncoding
from pathlib import Path

def test_unsupported_encoding_with_str_filename():
    filename = "test_file.py"
    exception = UnsupportedEncoding(filename)
    assert str(exception) == f"Unknown or unsupported encoding in {filename}"
    assert exception.filename == filename

def test_unsupported_encoding_with_path_filename():
    filename = Path("test_file.py")
    exception = UnsupportedEncoding(filename)
    assert str(exception) == f"Unknown or unsupported encoding in {filename}"
    assert exception.filename == filename
