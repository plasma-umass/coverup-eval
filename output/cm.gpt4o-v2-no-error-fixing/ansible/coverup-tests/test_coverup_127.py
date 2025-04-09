# file: lib/ansible/parsing/yaml/objects.py:33-58
# asked: {"lines": [33, 34, 39, 40, 41, 43, 44, 46, 47, 48, 49, 50, 51, 54, 55, 56, 58], "branches": []}
# gained: {"lines": [33, 34, 39, 40, 41, 43, 44, 46, 47, 48, 49, 50, 51, 54, 55, 56, 58], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

def test_get_ansible_position():
    obj = AnsibleBaseYAMLObject()
    obj._data_source = "source"
    obj._line_number = 10
    obj._column_number = 5
    assert obj._get_ansible_position() == ("source", 10, 5)

def test_set_ansible_position():
    obj = AnsibleBaseYAMLObject()
    obj._set_ansible_position(("source", 10, 5))
    assert obj._data_source == "source"
    assert obj._line_number == 10
    assert obj._column_number == 5

def test_set_ansible_position_invalid():
    obj = AnsibleBaseYAMLObject()
    with pytest.raises(AssertionError, match="ansible_pos can only be set with a tuple/list of three values: source, line number, column number"):
        obj._set_ansible_position(("source", 10))

def test_ansible_pos_property():
    obj = AnsibleBaseYAMLObject()
    obj.ansible_pos = ("source", 10, 5)
    assert obj.ansible_pos == ("source", 10, 5)
