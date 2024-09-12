# file: tornado/escape.py:78-83
# asked: {"lines": [78, 83], "branches": []}
# gained: {"lines": [78, 83], "branches": []}

import pytest
import json
from tornado.escape import json_decode, to_basestring

def test_json_decode_with_str():
    json_str = '{"key": "value"}'
    result = json_decode(json_str)
    assert result == {"key": "value"}

def test_json_decode_with_bytes():
    json_bytes = b'{"key": "value"}'
    result = json_decode(json_bytes)
    assert result == {"key": "value"}

def test_json_decode_with_invalid_json():
    invalid_json = '{"key": "value"'
    with pytest.raises(json.JSONDecodeError):
        json_decode(invalid_json)

def test_json_decode_with_empty_string():
    empty_str = ''
    with pytest.raises(json.JSONDecodeError):
        json_decode(empty_str)

def test_json_decode_with_empty_bytes():
    empty_bytes = b''
    with pytest.raises(json.JSONDecodeError):
        json_decode(empty_bytes)
