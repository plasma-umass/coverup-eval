# file: tornado/escape.py:67-75
# asked: {"lines": [67, 75], "branches": []}
# gained: {"lines": [67, 75], "branches": []}

import json
import pytest
from tornado.escape import json_encode

def test_json_encode_basic():
    value = {"key": "value"}
    encoded = json_encode(value)
    assert encoded == '{"key": "value"}'

def test_json_encode_with_script_tag():
    value = {"key": "</script>"}
    encoded = json_encode(value)
    assert encoded == '{"key": "<\\/script>"}'

def test_json_encode_with_nested_script_tag():
    value = {"key": {"nested_key": "</script>"}}
    encoded = json_encode(value)
    assert encoded == '{"key": {"nested_key": "<\\/script>"}}'

def test_json_encode_with_list_containing_script_tag():
    value = ["</script>"]
    encoded = json_encode(value)
    assert encoded == '["<\\/script>"]'

def test_json_encode_with_complex_structure():
    value = {"key": ["<script>", {"nested_key": "</script>"}]}
    encoded = json_encode(value)
    assert encoded == '{"key": ["<script>", {"nested_key": "<\\/script>"}]}'
