# file flutils/codecs/b64.py:17-62
# lines [36, 39, 40, 41, 42, 43, 48, 49, 50, 51, 52, 53, 54, 55, 56, 58, 59, 62]
# branches []

import pytest
from flutils.codecs.b64 import encode

def test_encode_valid_base64():
    text = "SGVsbG8gV29ybGQh"  # "Hello World!" in base64
    result, length = encode(text)
    assert result == b"Hello World!"
    assert length == len(text)

def test_encode_invalid_base64():
    text = "Invalid base64!!"
    with pytest.raises(UnicodeEncodeError) as excinfo:
        encode(text)
    assert "is not a proper bas64 character string" in str(excinfo.value)

def test_encode_with_whitespace():
    text = "  SGVsbG8gV29ybGQh  \n"
    result, length = encode(text)
    assert result == b"Hello World!"
    assert length == len(text)

def test_encode_multiline_base64():
    text = "SGVsbG8g\nV29ybGQh"
    result, length = encode(text)
    assert result == b"Hello World!"
    assert length == len(text)

def test_encode_empty_string():
    text = ""
    result, length = encode(text)
    assert result == b""
    assert length == len(text)
