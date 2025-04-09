# file: flutils/codecs/b64.py:66-92
# asked: {"lines": [66, 68, 84, 87, 90, 92], "branches": []}
# gained: {"lines": [66, 68, 84, 87, 90, 92], "branches": []}

import base64
import pytest
from flutils.codecs.b64 import decode

def test_decode_bytes():
    data = b'hello'
    result, length = decode(data)
    assert result == 'aGVsbG8='
    assert length == len(data)

def test_decode_bytearray():
    data = bytearray(b'world')
    result, length = decode(data)
    assert result == 'd29ybGQ='
    assert length == len(data)

def test_decode_memoryview():
    data = memoryview(b'python')
    result, length = decode(data)
    assert result == 'cHl0aG9u'
    assert length == len(data)

def test_decode_with_errors_argument():
    data = b'example'
    result, length = decode(data, errors='ignore')
    assert result == 'ZXhhbXBsZQ=='
    assert length == len(data)
