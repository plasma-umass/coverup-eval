# file: tornado/escape.py:67-75
# asked: {"lines": [67, 75], "branches": []}
# gained: {"lines": [67, 75], "branches": []}

import pytest
import json
from tornado.escape import json_encode

def test_json_encode_basic():
    assert json_encode({"key": "value"}) == '{"key": "value"}'
    assert json_encode(["item1", "item2"]) == '["item1", "item2"]'
    assert json_encode("simple string") == '"simple string"'
    assert json_encode(123) == '123'
    assert json_encode(None) == 'null'

def test_json_encode_with_script_tag():
    assert json_encode("</script>") == '"<\\/script>"'
    assert json_encode({"key": "</script>"}) == '{"key": "<\\/script>"}'
    assert json_encode(["</script>"]) == '["<\\/script>"]'

def test_json_encode_with_complex_structure():
    complex_structure = {
        "key1": "value1",
        "key2": ["list_item1", {"nested_key": "</script>"}],
        "key3": {"subkey": "</script>"}
    }
    encoded = json_encode(complex_structure)
    assert encoded == '{"key1": "value1", "key2": ["list_item1", {"nested_key": "<\\/script>"}], "key3": {"subkey": "<\\/script>"}}'

@pytest.mark.parametrize("input_value,expected_output", [
    ({"key": "</script>"}, '{"key": "<\\/script>"}'),
    (["</script>"], '["<\\/script>"]'),
    ("</script>", '"<\\/script>"'),
    ({"key": "value</script>"}, '{"key": "value<\\/script>"}'),
])
def test_json_encode_parametrized(input_value, expected_output):
    assert json_encode(input_value) == expected_output
