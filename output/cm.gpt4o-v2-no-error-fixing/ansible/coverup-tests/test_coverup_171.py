# file: lib/ansible/plugins/inventory/toml.py:128-149
# asked: {"lines": [128, 142, 143, 144, 145, 146, 147, 149], "branches": [[142, 143], [142, 144], [144, 145], [144, 146], [146, 147], [146, 149]]}
# gained: {"lines": [128, 142, 143, 144, 145, 146, 147, 149], "branches": [[142, 143], [142, 144], [144, 145], [144, 146], [146, 147], [146, 149]]}

import pytest
from ansible.plugins.inventory.toml import convert_yaml_objects_to_native
from ansible.module_utils.six import text_type

@pytest.mark.parametrize("input_obj, expected_output", [
    ({"key": "value"}, {"key": "value"}),
    (["item1", "item2"], ["item1", "item2"]),
    (text_type("string"), text_type("string")),
    (123, 123),
])
def test_convert_yaml_objects_to_native(input_obj, expected_output):
    assert convert_yaml_objects_to_native(input_obj) == expected_output

def test_convert_yaml_objects_to_native_nested():
    input_obj = {"key": ["item1", {"nested_key": text_type("nested_value")}]}
    expected_output = {"key": ["item1", {"nested_key": text_type("nested_value")}]}
    assert convert_yaml_objects_to_native(input_obj) == expected_output
