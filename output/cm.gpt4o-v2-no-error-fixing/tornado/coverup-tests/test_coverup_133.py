# file: tornado/escape.py:67-75
# asked: {"lines": [67, 75], "branches": []}
# gained: {"lines": [67, 75], "branches": []}

import pytest
from tornado.escape import json_encode

def test_json_encode_basic():
    assert json_encode({"key": "value"}) == '{"key": "value"}'

def test_json_encode_with_script_tag():
    assert json_encode("</script>") == '"<\\/script>"'

def test_json_encode_with_nested_script_tag():
    assert json_encode({"key": "</script>"}) == '{"key": "<\\/script>"}'

def test_json_encode_with_list_containing_script_tag():
    assert json_encode(["</script>"]) == '["<\\/script>"]'

def test_json_encode_with_complex_structure():
    data = {
        "key1": "</script>",
        "key2": ["<script>", {"nested_key": "</script>"}]
    }
    expected = '{"key1": "<\\/script>", "key2": ["<script>", {"nested_key": "<\\/script>"}]}'
    assert json_encode(data) == expected
