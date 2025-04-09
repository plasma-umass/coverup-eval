# file: flutils/codecs/raw_utf8_escape.py:91-140
# asked: {"lines": [91, 93, 114, 117, 123, 127, 130, 131, 132, 133, 134, 135, 136, 137, 138, 140], "branches": []}
# gained: {"lines": [91, 93, 114, 117, 123, 127, 130, 131, 132, 133, 134, 135, 136, 137, 138, 140], "branches": []}

import pytest
from flutils.codecs.raw_utf8_escape import decode

def test_decode_valid_data():
    data = b'\\x68\\x65\\x6c\\x6c\\x6f'  # Represents 'hello' in escaped utf8 hexadecimal
    result, length = decode(data)
    assert result == 'hello'
    assert length == len(data)

def test_decode_invalid_data_strict():
    data = b'\\x80\\x80\\x80'  # Invalid utf8 bytes
    with pytest.raises(UnicodeDecodeError):
        decode(data, errors='strict')

def test_decode_invalid_data_ignore():
    data = b'\\x80\\x80\\x80'  # Invalid utf8 bytes
    result, length = decode(data, errors='ignore')
    assert result == ''
    assert length == len(data)

def test_decode_invalid_data_replace():
    data = b'\\x80\\x80\\x80'  # Invalid utf8 bytes
    result, length = decode(data, errors='replace')
    assert result == '\ufffd\ufffd\ufffd'  # Replacement character for each invalid byte
    assert length == len(data)

def test_decode_bytearray():
    data = bytearray(b'\\x68\\x65\\x6c\\x6c\\x6f')  # Represents 'hello' in escaped utf8 hexadecimal
    result, length = decode(data)
    assert result == 'hello'
    assert length == len(data)

def test_decode_memoryview():
    data = memoryview(b'\\x68\\x65\\x6c\\x6c\\x6f')  # Represents 'hello' in escaped utf8 hexadecimal
    result, length = decode(data)
    assert result == 'hello'
    assert length == len(data)
