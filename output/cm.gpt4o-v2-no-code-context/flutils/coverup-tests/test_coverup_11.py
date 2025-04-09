# file: flutils/codecs/b64.py:66-92
# asked: {"lines": [66, 68, 84, 87, 90, 92], "branches": []}
# gained: {"lines": [66, 68, 84, 87, 90, 92], "branches": []}

import pytest
import base64
from flutils.codecs.b64 import decode

def test_decode_bytes():
    data = b"hello world"
    expected_encoded_str = base64.b64encode(data).decode('utf-8')
    encoded_str, consumed = decode(data)
    assert encoded_str == expected_encoded_str
    assert consumed == len(data)

def test_decode_bytearray():
    data = bytearray(b"hello world")
    expected_encoded_str = base64.b64encode(data).decode('utf-8')
    encoded_str, consumed = decode(data)
    assert encoded_str == expected_encoded_str
    assert consumed == len(data)

def test_decode_memoryview():
    data = memoryview(b"hello world")
    expected_encoded_str = base64.b64encode(data).decode('utf-8')
    encoded_str, consumed = decode(data)
    assert encoded_str == expected_encoded_str
    assert consumed == len(data)

def test_decode_with_errors_argument():
    data = b"hello world"
    expected_encoded_str = base64.b64encode(data).decode('utf-8')
    encoded_str, consumed = decode(data, errors='ignore')
    assert encoded_str == expected_encoded_str
    assert consumed == len(data)
