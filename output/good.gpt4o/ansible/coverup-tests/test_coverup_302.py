# file lib/ansible/plugins/inventory/toml.py:128-149
# lines [128, 142, 143, 144, 145, 146, 147, 149]
# branches ['142->143', '142->144', '144->145', '144->146', '146->147', '146->149']

import pytest
from ansible.plugins.inventory.toml import convert_yaml_objects_to_native

def test_convert_yaml_objects_to_native_dict():
    input_data = {
        'key1': 'value1',
        'key2': {
            'nested_key1': 'nested_value1',
            'nested_key2': ['list_item1', 'list_item2']
        }
    }
    expected_output = {
        'key1': 'value1',
        'key2': {
            'nested_key1': 'nested_value1',
            'nested_key2': ['list_item1', 'list_item2']
        }
    }
    assert convert_yaml_objects_to_native(input_data) == expected_output

def test_convert_yaml_objects_to_native_list():
    input_data = ['item1', {'key1': 'value1'}, ['nested_list_item1', 'nested_list_item2']]
    expected_output = ['item1', {'key1': 'value1'}, ['nested_list_item1', 'nested_list_item2']]
    assert convert_yaml_objects_to_native(input_data) == expected_output

def test_convert_yaml_objects_to_native_text_type():
    input_data = 'some_text'
    expected_output = 'some_text'
    assert convert_yaml_objects_to_native(input_data) == expected_output

def test_convert_yaml_objects_to_native_other_type():
    input_data = 12345
    expected_output = 12345
    assert convert_yaml_objects_to_native(input_data) == expected_output
