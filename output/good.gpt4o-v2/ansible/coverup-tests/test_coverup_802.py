# file: lib/ansible/parsing/yaml/objects.py:66-68
# asked: {"lines": [66, 67, 68], "branches": []}
# gained: {"lines": [66, 67, 68], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleUnicode
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
from ansible.module_utils.six import text_type

def test_ansible_unicode_inheritance():
    # Test that AnsibleUnicode is a subclass of AnsibleBaseYAMLObject and text_type
    assert issubclass(AnsibleUnicode, AnsibleBaseYAMLObject)
    assert issubclass(AnsibleUnicode, text_type)

def test_ansible_unicode_instance():
    # Test that an instance of AnsibleUnicode can be created and is an instance of the expected classes
    unicode_string = AnsibleUnicode("test")
    assert isinstance(unicode_string, AnsibleUnicode)
    assert isinstance(unicode_string, AnsibleBaseYAMLObject)
    assert isinstance(unicode_string, text_type)
    assert unicode_string == "test"
