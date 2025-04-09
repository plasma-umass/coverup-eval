# file: tornado/escape.py:147-167
# asked: {"lines": [147, 148, 159, 160, 161, 162, 164, 165, 166, 167], "branches": [[159, 160], [159, 161], [165, 166], [165, 167]]}
# gained: {"lines": [147, 148, 159, 160, 161, 162, 164, 165, 166, 167], "branches": [[159, 160], [159, 161], [165, 166], [165, 167]]}

import pytest
from tornado.escape import parse_qs_bytes

def test_parse_qs_bytes_with_str():
    qs = "key1=value1&key2=value2"
    result = parse_qs_bytes(qs)
    assert result == {
        "key1": [b"value1"],
        "key2": [b"value2"]
    }

def test_parse_qs_bytes_with_bytes():
    qs = b"key1=value1&key2=value2"
    result = parse_qs_bytes(qs)
    assert result == {
        "key1": [b"value1"],
        "key2": [b"value2"]
    }

def test_parse_qs_bytes_with_blank_values():
    qs = "key1=&key2=value2"
    result = parse_qs_bytes(qs, keep_blank_values=True)
    assert result == {
        "key1": [b""],
        "key2": [b"value2"]
    }

def test_parse_qs_bytes_with_strict_parsing():
    qs = "key1=value1&key2=value2"
    result = parse_qs_bytes(qs, strict_parsing=True)
    assert result == {
        "key1": [b"value1"],
        "key2": [b"value2"]
    }

def test_parse_qs_bytes_with_invalid_strict_parsing():
    qs = "key1=value1&key2"
    with pytest.raises(ValueError):
        parse_qs_bytes(qs, strict_parsing=True)
