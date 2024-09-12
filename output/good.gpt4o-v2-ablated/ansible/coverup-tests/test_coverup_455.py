# file: lib/ansible/parsing/yaml/objects.py:33-58
# asked: {"lines": [44, 49, 50, 51], "branches": []}
# gained: {"lines": [44, 49, 50, 51], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

@pytest.fixture
def yaml_object():
    return AnsibleBaseYAMLObject()

def test_get_ansible_position(yaml_object):
    assert yaml_object.ansible_pos == (None, 0, 0)

def test_set_ansible_position_valid(yaml_object):
    yaml_object.ansible_pos = ('source_file', 10, 20)
    assert yaml_object.ansible_pos == ('source_file', 10, 20)

def test_set_ansible_position_invalid_type(yaml_object):
    with pytest.raises(AssertionError, match='ansible_pos can only be set with a tuple/list of three values: source, line number, column number'):
        yaml_object.ansible_pos = 'invalid_type'

def test_set_ansible_position_invalid_length(yaml_object):
    with pytest.raises(AssertionError, match='ansible_pos can only be set with a tuple/list of three values: source, line number, column number'):
        yaml_object.ansible_pos = ('source_file', 10)

def test_set_ansible_position_invalid_value(yaml_object):
    with pytest.raises(AssertionError, match='ansible_pos can only be set with a tuple/list of three values: source, line number, column number'):
        yaml_object.ansible_pos = ('source_file', 10, 20, 30)
