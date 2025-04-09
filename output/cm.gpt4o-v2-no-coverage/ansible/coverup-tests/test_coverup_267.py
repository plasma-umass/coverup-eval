# file: lib/ansible/parsing/yaml/objects.py:33-58
# asked: {"lines": [33, 34, 39, 40, 41, 43, 44, 46, 47, 48, 49, 50, 51, 54, 55, 56, 58], "branches": []}
# gained: {"lines": [33, 34, 39, 40, 41, 43, 44, 46, 47, 48, 49, 50, 51, 54, 55, 56, 58], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

@pytest.fixture
def yaml_object():
    return AnsibleBaseYAMLObject()

def test_get_ansible_position(yaml_object):
    yaml_object._data_source = "source"
    yaml_object._line_number = 10
    yaml_object._column_number = 20
    assert yaml_object.ansible_pos == ("source", 10, 20)

def test_set_ansible_position(yaml_object):
    yaml_object.ansible_pos = ("new_source", 30, 40)
    assert yaml_object._data_source == "new_source"
    assert yaml_object._line_number == 30
    assert yaml_object._column_number == 40

def test_set_ansible_position_invalid_type(yaml_object):
    with pytest.raises(AssertionError, match="ansible_pos can only be set with a tuple/list of three values: source, line number, column number"):
        yaml_object.ansible_pos = "invalid"

def test_set_ansible_position_invalid_length(yaml_object):
    with pytest.raises(AssertionError, match="ansible_pos can only be set with a tuple/list of three values: source, line number, column number"):
        yaml_object.ansible_pos = ("source", 10)
