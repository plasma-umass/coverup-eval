# file tornado/escape.py:147-167
# lines [147, 148, 159, 160, 161, 162, 164, 165, 166, 167]
# branches ['159->160', '159->161', '165->166', '165->167']

import pytest
from tornado.escape import parse_qs_bytes

def test_parse_qs_bytes():
    # Test with bytes input
    qs_bytes = b'key1=value1&key2=value2'
    result = parse_qs_bytes(qs_bytes)
    assert result == {'key1': [b'value1'], 'key2': [b'value2']}

    # Test with string input
    qs_str = 'key1=value1&key2=value2'
    result = parse_qs_bytes(qs_str)
    assert result == {'key1': [b'value1'], 'key2': [b'value2']}

    # Test with keep_blank_values=True
    qs_blank = 'key1=value1&key2=&key3=value3'
    result = parse_qs_bytes(qs_blank, keep_blank_values=True)
    assert result == {'key1': [b'value1'], 'key2': [b''], 'key3': [b'value3']}

    # Test with strict_parsing=True
    with pytest.raises(ValueError):
        parse_qs_bytes('key1=value1&key2', strict_parsing=True)

    # Test with non-ASCII characters
    qs_non_ascii = 'key1=valüe1&key2=valüe2'
    result = parse_qs_bytes(qs_non_ascii)
    assert result == {'key1': ['valüe1'.encode('latin1')], 'key2': ['valüe2'.encode('latin1')]}
