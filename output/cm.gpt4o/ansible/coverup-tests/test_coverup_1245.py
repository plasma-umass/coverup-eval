# file lib/ansible/parsing/yaml/objects.py:33-58
# lines [49, 50, 51]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

def test_set_ansible_position_invalid_type():
    obj = AnsibleBaseYAMLObject()
    with pytest.raises(AssertionError, match='ansible_pos can only be set with a tuple/list of three values: source, line number, column number'):
        obj.ansible_pos = "invalid_type"

def test_set_ansible_position_invalid_length():
    obj = AnsibleBaseYAMLObject()
    with pytest.raises(AssertionError, match='ansible_pos can only be set with a tuple/list of three values: source, line number, column number'):
        obj.ansible_pos = ("source", 1)  # Only two elements instead of three

def test_set_ansible_position_valid():
    obj = AnsibleBaseYAMLObject()
    obj.ansible_pos = ("source", 1, 2)
    assert obj.ansible_pos == ("source", 1, 2)
