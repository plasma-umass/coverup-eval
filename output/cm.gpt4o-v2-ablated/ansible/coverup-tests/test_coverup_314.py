# file: lib/ansible/parsing/yaml/objects.py:66-68
# asked: {"lines": [66, 67, 68], "branches": []}
# gained: {"lines": [66, 67, 68], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleBaseYAMLObject

def test_ansible_unicode_inheritance():
    # Test that AnsibleUnicode is a subclass of AnsibleBaseYAMLObject and text_type
    assert issubclass(AnsibleUnicode, AnsibleBaseYAMLObject)
    assert issubclass(AnsibleUnicode, str)

def test_ansible_unicode_instance():
    # Test that an instance of AnsibleUnicode behaves like a string
    test_string = "test"
    ansible_unicode_instance = AnsibleUnicode(test_string)
    
    assert isinstance(ansible_unicode_instance, AnsibleUnicode)
    assert isinstance(ansible_unicode_instance, AnsibleBaseYAMLObject)
    assert isinstance(ansible_unicode_instance, str)
    assert ansible_unicode_instance == test_string
    assert ansible_unicode_instance.upper() == test_string.upper()
