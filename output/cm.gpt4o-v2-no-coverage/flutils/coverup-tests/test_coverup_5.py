# file: flutils/codecs/b64.py:66-92
# asked: {"lines": [66, 68, 84, 87, 90, 92], "branches": []}
# gained: {"lines": [66, 68, 84, 87, 90, 92], "branches": []}

import pytest
from flutils.codecs.b64 import decode

def test_decode_bytes():
    data = b"hello"
    result, length = decode(data)
    assert result == "aGVsbG8="
    assert length == len(data)

def test_decode_bytearray():
    data = bytearray(b"world")
    result, length = decode(data)
    assert result == "d29ybGQ="
    assert length == len(data)

def test_decode_memoryview():
    data = memoryview(b"test")
    result, length = decode(data)
    assert result == "dGVzdA=="
    assert length == len(data)

def test_decode_with_errors_argument():
    data = b"errors"
    result, length = decode(data, errors="ignore")
    assert result == "ZXJyb3Jz"
    assert length == len(data)
