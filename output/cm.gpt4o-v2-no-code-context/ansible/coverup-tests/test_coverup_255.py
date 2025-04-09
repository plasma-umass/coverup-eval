# file: lib/ansible/plugins/inventory/toml.py:128-149
# asked: {"lines": [128, 142, 143, 144, 145, 146, 147, 149], "branches": [[142, 143], [142, 144], [144, 145], [144, 146], [146, 147], [146, 149]]}
# gained: {"lines": [128, 142, 143, 144, 145, 146, 147, 149], "branches": [[142, 143], [142, 144], [144, 145], [144, 146], [146, 147], [146, 149]]}

import pytest
from ansible.plugins.inventory.toml import convert_yaml_objects_to_native
from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleMapping, AnsibleSequence
from ansible.module_utils.six import text_type

def test_convert_yaml_objects_to_native_dict():
    obj = AnsibleMapping({'key1': AnsibleUnicode('value1'), 'key2': AnsibleUnicode('value2')})
    result = convert_yaml_objects_to_native(obj)
    assert isinstance(result, dict)
    assert result == {'key1': 'value1', 'key2': 'value2'}

def test_convert_yaml_objects_to_native_list():
    obj = AnsibleSequence([AnsibleUnicode('value1'), AnsibleUnicode('value2')])
    result = convert_yaml_objects_to_native(obj)
    assert isinstance(result, list)
    assert result == ['value1', 'value2']

def test_convert_yaml_objects_to_native_text_type():
    obj = AnsibleUnicode('value')
    result = convert_yaml_objects_to_native(obj)
    assert isinstance(result, text_type)
    assert result == 'value'

def test_convert_yaml_objects_to_native_other():
    obj = 12345
    result = convert_yaml_objects_to_native(obj)
    assert result == 12345
