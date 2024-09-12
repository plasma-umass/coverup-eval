# file: flutils/codecs/b64.py:66-92
# asked: {"lines": [66, 68, 84, 87, 90, 92], "branches": []}
# gained: {"lines": [66, 68, 84, 87, 90, 92], "branches": []}

import pytest
from flutils.codecs.b64 import decode

def test_decode_bytes():
    data = b"hello world"
    expected_output = "aGVsbG8gd29ybGQ="
    expected_length = len(data)
    
    result, length = decode(data)
    
    assert result == expected_output
    assert length == expected_length

def test_decode_bytearray():
    data = bytearray(b"hello world")
    expected_output = "aGVsbG8gd29ybGQ="
    expected_length = len(data)
    
    result, length = decode(data)
    
    assert result == expected_output
    assert length == expected_length

def test_decode_memoryview():
    data = memoryview(b"hello world")
    expected_output = "aGVsbG8gd29ybGQ="
    expected_length = len(data)
    
    result, length = decode(data)
    
    assert result == expected_output
    assert length == expected_length
