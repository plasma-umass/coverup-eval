# file: lib/ansible/plugins/inventory/toml.py:128-149
# asked: {"lines": [128, 142, 143, 144, 145, 146, 147, 149], "branches": [[142, 143], [142, 144], [144, 145], [144, 146], [146, 147], [146, 149]]}
# gained: {"lines": [128, 142, 143, 144, 145, 146, 147, 149], "branches": [[142, 143], [142, 144], [144, 145], [144, 146], [146, 147], [146, 149]]}

import pytest
from ansible.plugins.inventory.toml import convert_yaml_objects_to_native
from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleMapping, AnsibleSequence
from six import text_type

def test_convert_yaml_objects_to_native_dict():
    obj = {
        'key1': AnsibleUnicode('value1'),
        'key2': AnsibleMapping({'nested_key': AnsibleUnicode('nested_value')}),
        'key3': AnsibleSequence([AnsibleUnicode('list_value1'), AnsibleUnicode('list_value2')])
    }
    expected = {
        'key1': 'value1',
        'key2': {'nested_key': 'nested_value'},
        'key3': ['list_value1', 'list_value2']
    }
    result = convert_yaml_objects_to_native(obj)
    assert result == expected

def test_convert_yaml_objects_to_native_list():
    obj = [
        AnsibleUnicode('value1'),
        AnsibleMapping({'nested_key': AnsibleUnicode('nested_value')}),
        AnsibleSequence([AnsibleUnicode('list_value1'), AnsibleUnicode('list_value2')])
    ]
    expected = [
        'value1',
        {'nested_key': 'nested_value'},
        ['list_value1', 'list_value2']
    ]
    result = convert_yaml_objects_to_native(obj)
    assert result == expected

def test_convert_yaml_objects_to_native_text_type():
    obj = AnsibleUnicode('value')
    expected = 'value'
    result = convert_yaml_objects_to_native(obj)
    assert result == expected

def test_convert_yaml_objects_to_native_other_type():
    obj = 42
    result = convert_yaml_objects_to_native(obj)
    assert result == obj
