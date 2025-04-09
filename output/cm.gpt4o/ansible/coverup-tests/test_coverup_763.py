# file lib/ansible/parsing/yaml/objects.py:66-68
# lines [66, 67, 68]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

class AnsibleUnicode(AnsibleBaseYAMLObject, str):
    ''' sub class for unicode objects '''
    pass

def test_ansible_unicode():
    # Create an instance of AnsibleUnicode
    unicode_instance = AnsibleUnicode("test string")

    # Verify that the instance is of type AnsibleUnicode
    assert isinstance(unicode_instance, AnsibleUnicode)

    # Verify that the instance is also of type str
    assert isinstance(unicode_instance, str)

    # Verify the content of the instance
    assert unicode_instance == "test string"
