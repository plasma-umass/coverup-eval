# file: flutils/codecs/raw_utf8_escape.py:91-140
# asked: {"lines": [91, 93, 114, 117, 123, 127, 130, 131, 132, 133, 134, 135, 136, 137, 138, 140], "branches": []}
# gained: {"lines": [91, 93, 114, 117, 123, 127, 130, 131, 132, 133, 134, 135, 136, 137, 138, 140], "branches": []}

import pytest
from flutils.codecs.raw_utf8_escape import decode

def test_decode_strict():
    data = b'\\xF0\\x9F\\x98\\x81'  # Escaped UTF-8 for 😁
    result, consumed = decode(data, 'strict')
    assert result == '😁'
    assert consumed == len(data)

def test_decode_replace():
    data = b'\\xF0\\x9F\\x98\\x81\\xC3\\x28'  # Escaped UTF-8 for 😁 followed by invalid byte sequence
    result, consumed = decode(data, 'replace')
    assert result == '😁�('  # � is the replacement character
    assert consumed == len(data)

def test_decode_ignore():
    data = b'\\xF0\\x9F\\x98\\x81\\xC3\\x28'  # Escaped UTF-8 for 😁 followed by invalid byte sequence
    result, consumed = decode(data, 'ignore')
    assert result == '😁('  # Invalid byte sequence is ignored
    assert consumed == len(data)

def test_decode_unicode_decode_error():
    data = b'\\xF0\\x9F\\x98\\x81\\xC3\\x28'  # Escaped UTF-8 for 😁 followed by invalid byte sequence
    with pytest.raises(UnicodeDecodeError) as excinfo:
        decode(data, 'strict')
    assert excinfo.value.start == 4
    assert excinfo.value.end == 5
    assert excinfo.value.reason == 'invalid continuation byte'
