# file: lib/ansible/parsing/yaml/objects.py:66-68
# asked: {"lines": [66, 67, 68], "branches": []}
# gained: {"lines": [66, 67, 68], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleBaseYAMLObject

def test_ansible_unicode_inheritance():
    # Test that AnsibleUnicode is a subclass of AnsibleBaseYAMLObject and text_type
    assert issubclass(AnsibleUnicode, AnsibleBaseYAMLObject)
    assert issubclass(AnsibleUnicode, str)  # text_type is an alias for str in Python 3

def test_ansible_unicode_instance():
    # Test that an instance of AnsibleUnicode can be created and is an instance of both AnsibleBaseYAMLObject and text_type
    obj = AnsibleUnicode("test string")
    assert isinstance(obj, AnsibleUnicode)
    assert isinstance(obj, AnsibleBaseYAMLObject)
    assert isinstance(obj, str)  # text_type is an alias for str in Python 3
    assert obj == "test string"
