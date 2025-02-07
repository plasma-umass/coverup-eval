# file: flutils/codecs/raw_utf8_escape.py:91-140
# asked: {"lines": [91, 93, 114, 117, 123, 127, 130, 131, 132, 133, 134, 135, 136, 137, 138, 140], "branches": []}
# gained: {"lines": [91, 93, 114, 117, 123, 127, 130, 131, 132, 133, 134, 135, 136, 137, 138, 140], "branches": []}

import pytest
from flutils.codecs.raw_utf8_escape import decode

def test_decode_valid_data():
    data = b'\\x48\\x65\\x6c\\x6c\\x6f'  # Represents 'Hello' in escaped utf8 hexadecimal
    result, length = decode(data)
    assert result == 'Hello'
    assert length == len(data)

def test_decode_invalid_data_strict():
    data = b'\\x80'  # Invalid utf8 byte
    with pytest.raises(UnicodeDecodeError):
        decode(data, errors='strict')

def test_decode_invalid_data_replace():
    data = b'\\x80'  # Invalid utf8 byte
    result, length = decode(data, errors='replace')
    assert result == '\ufffd'  # Replacement character for invalid utf8
    assert length == len(data)

def test_decode_invalid_data_ignore():
    data = b'\\x80'  # Invalid utf8 byte
    result, length = decode(data, errors='ignore')
    assert result == ''  # Invalid byte is ignored
    assert length == len(data)
