# file: lib/ansible/parsing/yaml/objects.py:66-68
# asked: {"lines": [66, 67, 68], "branches": []}
# gained: {"lines": [66, 67, 68], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleBaseYAMLObject
from ansible.module_utils.six import text_type

def test_ansible_unicode_is_instance_of_text_type():
    obj = AnsibleUnicode("test")
    assert isinstance(obj, text_type)

def test_ansible_unicode_is_instance_of_ansible_base_yaml_object():
    obj = AnsibleUnicode("test")
    assert isinstance(obj, AnsibleBaseYAMLObject)

def test_ansible_unicode_inherits_methods_from_text_type():
    obj = AnsibleUnicode("test")
    assert obj.upper() == "TEST"

def test_ansible_unicode_inherits_methods_from_ansible_base_yaml_object():
    obj = AnsibleUnicode("test")
    obj._set_ansible_position(("source", 1, 2))
    assert obj._data_source == "source"
    assert obj._line_number == 1
    assert obj._column_number == 2
