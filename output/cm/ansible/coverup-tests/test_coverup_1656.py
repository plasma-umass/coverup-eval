# file lib/ansible/parsing/yaml/objects.py:33-58
# lines [44, 49, 50, 51]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

def test_ansible_base_yaml_object_get_position():
    obj = AnsibleBaseYAMLObject()
    obj._data_source = "source"
    obj._line_number = 42
    obj._column_number = 24
    position = obj.ansible_pos
    assert position == ("source", 42, 24)

def test_ansible_base_yaml_object_set_position():
    obj = AnsibleBaseYAMLObject()
    obj.ansible_pos = ("source", 42, 24)
    assert obj._data_source == "source"
    assert obj._line_number == 42
    assert obj._column_number == 24

def test_ansible_base_yaml_object_set_position_with_invalid_value():
    obj = AnsibleBaseYAMLObject()
    with pytest.raises(AssertionError) as excinfo:
        obj.ansible_pos = ("source", 42)  # Missing column number
    assert 'ansible_pos can only be set with a tuple/list of three values: source, line number, column number' in str(excinfo.value)
