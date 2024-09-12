# file: lib/ansible/plugins/inventory/toml.py:128-149
# asked: {"lines": [128, 142, 143, 144, 145, 146, 147, 149], "branches": [[142, 143], [142, 144], [144, 145], [144, 146], [146, 147], [146, 149]]}
# gained: {"lines": [128, 142, 143, 144, 145, 146, 147, 149], "branches": [[142, 143], [142, 144], [144, 145], [144, 146], [146, 147], [146, 149]]}

import pytest
from ansible.plugins.inventory.toml import convert_yaml_objects_to_native
from ansible.module_utils.six import text_type

class MockYAMLObject:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

def mock_convert_yaml_objects_to_native(obj):
    if isinstance(obj, dict):
        return {k: mock_convert_yaml_objects_to_native(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [mock_convert_yaml_objects_to_native(v) for v in obj]
    elif isinstance(obj, MockYAMLObject):
        return str(obj)
    elif isinstance(obj, text_type):
        return text_type(obj)
    else:
        return obj

def test_convert_yaml_objects_to_native_dict(monkeypatch):
    monkeypatch.setattr('ansible.plugins.inventory.toml.convert_yaml_objects_to_native', mock_convert_yaml_objects_to_native)

    obj = {
        'key1': MockYAMLObject('value1'),
        'key2': {
            'nested_key': MockYAMLObject('nested_value')
        }
    }
    result = convert_yaml_objects_to_native(obj)
    assert result == {
        'key1': 'value1',
        'key2': {
            'nested_key': 'nested_value'
        }
    }

def test_convert_yaml_objects_to_native_list(monkeypatch):
    monkeypatch.setattr('ansible.plugins.inventory.toml.convert_yaml_objects_to_native', mock_convert_yaml_objects_to_native)

    obj = [
        MockYAMLObject('value1'),
        [MockYAMLObject('nested_value')]
    ]
    result = convert_yaml_objects_to_native(obj)
    assert result == [
        'value1',
        ['nested_value']
    ]

def test_convert_yaml_objects_to_native_text_type(monkeypatch):
    monkeypatch.setattr('ansible.plugins.inventory.toml.convert_yaml_objects_to_native', mock_convert_yaml_objects_to_native)

    obj = text_type('value')
    result = convert_yaml_objects_to_native(obj)
    assert result == 'value'

def test_convert_yaml_objects_to_native_other():
    obj = 12345
    result = convert_yaml_objects_to_native(obj)
    assert result == 12345
