# file isort/exceptions.py:163-168
# lines [163, 164, 166, 167, 168]
# branches []

import pytest
from isort.exceptions import UnsupportedEncoding

def test_unsupported_encoding():
    filename = "test_file.py"
    exception = UnsupportedEncoding(filename)
    
    assert isinstance(exception, UnsupportedEncoding)
    assert str(exception) == f"Unknown or unsupported encoding in {filename}"
    assert exception.filename == filename
