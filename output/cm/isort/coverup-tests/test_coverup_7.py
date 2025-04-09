# file isort/exceptions.py:163-168
# lines [163, 164, 166, 167, 168]
# branches []

import pytest
from isort.exceptions import UnsupportedEncoding
from pathlib import Path

def test_unsupported_encoding_exception():
    filename = "test_file.py"
    exception = UnsupportedEncoding(filename)
    assert str(exception) == f"Unknown or unsupported encoding in {filename}"
    assert exception.filename == filename

    # Test with Path object
    filename_path = Path("test_file.py")
    exception_path = UnsupportedEncoding(filename_path)
    assert str(exception_path) == f"Unknown or unsupported encoding in {filename_path}"
    assert exception_path.filename == filename_path
