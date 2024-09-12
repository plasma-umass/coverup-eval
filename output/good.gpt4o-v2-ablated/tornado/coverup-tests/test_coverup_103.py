# file: tornado/escape.py:67-75
# asked: {"lines": [67, 75], "branches": []}
# gained: {"lines": [67, 75], "branches": []}

import json
import pytest
from tornado.escape import json_encode

def test_json_encode_basic():
    assert json_encode({"key": "value"}) == '{"key": "value"}'

def test_json_encode_with_forward_slash():
    assert json_encode({"key": "</script>"}) == '{"key": "<\\/script>"}'

def test_json_encode_with_nested_structure():
    data = {"key": ["value1", {"nested_key": "</script>"}]}
    expected = '{"key": ["value1", {"nested_key": "<\\/script>"}]}'
    assert json_encode(data) == expected

def test_json_encode_with_special_characters():
    data = {"key": "value with special characters: \n \t \b \f \r"}
    expected = '{"key": "value with special characters: \\n \\t \\b \\f \\r"}'
    assert json_encode(data) == expected

def test_json_encode_with_unicode():
    data = {"key": "value with unicode: \u1234"}
    expected = '{"key": "value with unicode: \\u1234"}'
    assert json_encode(data) == expected
