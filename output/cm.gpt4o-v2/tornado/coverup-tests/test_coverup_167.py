# file: tornado/escape.py:78-83
# asked: {"lines": [78, 83], "branches": []}
# gained: {"lines": [78, 83], "branches": []}

import pytest
from tornado.escape import json_decode

def test_json_decode_with_str():
    json_str = '{"key": "value"}'
    result = json_decode(json_str)
    assert result == {"key": "value"}

def test_json_decode_with_bytes():
    json_bytes = b'{"key": "value"}'
    result = json_decode(json_bytes)
    assert result == {"key": "value"}
