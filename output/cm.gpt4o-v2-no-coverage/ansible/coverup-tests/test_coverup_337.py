# file: lib/ansible/plugins/inventory/toml.py:128-149
# asked: {"lines": [128, 142, 143, 144, 145, 146, 147, 149], "branches": [[142, 143], [142, 144], [144, 145], [144, 146], [146, 147], [146, 149]]}
# gained: {"lines": [128, 142, 143, 144, 145, 146, 147, 149], "branches": [[142, 143], [142, 144], [144, 145], [144, 146], [146, 147], [146, 149]]}

import pytest
from ansible.plugins.inventory.toml import convert_yaml_objects_to_native
from ansible.module_utils.six import text_type

def test_convert_yaml_objects_to_native_dict():
    input_data = {'key1': 'value1', 'key2': {'key3': 'value3'}}
    expected_output = {'key1': 'value1', 'key2': {'key3': 'value3'}}
    assert convert_yaml_objects_to_native(input_data) == expected_output

def test_convert_yaml_objects_to_native_list():
    input_data = ['value1', ['value2', 'value3']]
    expected_output = ['value1', ['value2', 'value3']]
    assert convert_yaml_objects_to_native(input_data) == expected_output

def test_convert_yaml_objects_to_native_text_type():
    input_data = text_type('value1')
    expected_output = text_type('value1')
    assert convert_yaml_objects_to_native(input_data) == expected_output

def test_convert_yaml_objects_to_native_other():
    input_data = 12345
    expected_output = 12345
    assert convert_yaml_objects_to_native(input_data) == expected_output
