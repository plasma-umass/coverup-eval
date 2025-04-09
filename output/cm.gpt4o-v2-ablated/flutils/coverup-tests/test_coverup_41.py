# file: flutils/codecs/raw_utf8_escape.py:91-140
# asked: {"lines": [114, 117, 123, 127, 130, 131, 132, 133, 134, 135, 136, 137, 138, 140], "branches": []}
# gained: {"lines": [114, 117, 123, 127, 130, 131, 132, 133, 134, 135, 136, 137, 138, 140], "branches": []}

import pytest
from flutils.codecs.raw_utf8_escape import decode

def test_decode_strict():
    data = b'\\x48\\x65\\x6c\\x6c\\x6f'  # "Hello" in escaped utf8 hexadecimal
    result, consumed = decode(data, 'strict')
    assert result == 'Hello'
    assert consumed == len(data)

def test_decode_ignore():
    data = b'\\x48\\x65\\x6c\\x6c\\x6f\\x80'  # "Hello" with an invalid utf8 byte
    result, consumed = decode(data, 'ignore')
    assert result == 'Hello'
    assert consumed == len(data)

def test_decode_replace():
    data = b'\\x48\\x65\\x6c\\x6c\\x6f\\x80'  # "Hello" with an invalid utf8 byte
    result, consumed = decode(data, 'replace')
    assert result == 'Hello�'
    assert consumed == len(data)

def test_decode_invalid_utf8():
    data = b'\\x80'  # Invalid utf8 byte
    with pytest.raises(UnicodeDecodeError) as excinfo:
        decode(data, 'strict')
    assert excinfo.value.start == 0
    assert excinfo.value.end == 1
    assert excinfo.value.reason == 'invalid start byte'

def test_decode_memoryview():
    data = memoryview(b'\\x48\\x65\\x6c\\x6c\\x6f')  # "Hello" in escaped utf8 hexadecimal
    result, consumed = decode(data, 'strict')
    assert result == 'Hello'
    assert consumed == len(data)

def test_decode_bytearray():
    data = bytearray(b'\\x48\\x65\\x6c\\x6c\\x6f')  # "Hello" in escaped utf8 hexadecimal
    result, consumed = decode(data, 'strict')
    assert result == 'Hello'
    assert consumed == len(data)

def test_decode_userstring_errors(monkeypatch):
    from collections import UserString
    errors = UserString('strict')
    data = b'\\x48\\x65\\x6c\\x6c\\x6f'  # "Hello" in escaped utf8 hexadecimal
    result, consumed = decode(data, errors)
    assert result == 'Hello'
    assert consumed == len(data)
