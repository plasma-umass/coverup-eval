# file: tornado/escape.py:147-167
# asked: {"lines": [147, 148, 159, 160, 161, 162, 164, 165, 166, 167], "branches": [[159, 160], [159, 161], [165, 166], [165, 167]]}
# gained: {"lines": [147, 148, 159, 160, 161, 162, 164, 165, 166, 167], "branches": [[159, 160], [159, 161], [165, 166], [165, 167]]}

import pytest
from tornado.escape import parse_qs_bytes

def test_parse_qs_bytes_with_bytes():
    qs = b'foo=bar&baz=qux'
    expected = {'foo': [b'bar'], 'baz': [b'qux']}
    result = parse_qs_bytes(qs)
    assert result == expected

def test_parse_qs_bytes_with_str():
    qs = 'foo=bar&baz=qux'
    expected = {'foo': [b'bar'], 'baz': [b'qux']}
    result = parse_qs_bytes(qs)
    assert result == expected

def test_parse_qs_bytes_with_blank_values():
    qs = b'foo=&baz=qux'
    expected = {'foo': [b''], 'baz': [b'qux']}
    result = parse_qs_bytes(qs, keep_blank_values=True)
    assert result == expected

def test_parse_qs_bytes_with_strict_parsing():
    qs = b'foo=bar&baz=qux&invalid'
    with pytest.raises(ValueError):
        parse_qs_bytes(qs, strict_parsing=True)
