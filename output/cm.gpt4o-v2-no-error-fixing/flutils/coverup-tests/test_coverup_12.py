# file: flutils/codecs/b64.py:66-92
# asked: {"lines": [66, 68, 84, 87, 90, 92], "branches": []}
# gained: {"lines": [66, 68, 84, 87, 90, 92], "branches": []}

import pytest
from flutils.codecs.b64 import decode

def test_decode_bytes():
    data = b"hello world"
    encoded_str, length = decode(data)
    assert encoded_str == "aGVsbG8gd29ybGQ="
    assert length == len(data)

def test_decode_bytearray():
    data = bytearray(b"hello world")
    encoded_str, length = decode(data)
    assert encoded_str == "aGVsbG8gd29ybGQ="
    assert length == len(data)

def test_decode_memoryview():
    data = memoryview(b"hello world")
    encoded_str, length = decode(data)
    assert encoded_str == "aGVsbG8gd29ybGQ="
    assert length == len(data)

def test_decode_errors_argument():
    data = b"hello world"
    encoded_str, length = decode(data, errors='ignore')
    assert encoded_str == "aGVsbG8gd29ybGQ="
    assert length == len(data)
