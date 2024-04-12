# file lib/ansible/parsing/yaml/objects.py:66-68
# lines [66, 67, 68]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleUnicode

def test_ansible_unicode_instantiation():
    # Test instantiation of AnsibleUnicode
    unicode_string = AnsibleUnicode("test string")
    assert isinstance(unicode_string, AnsibleUnicode)
    assert isinstance(unicode_string, str)  # Use str instead of text_type
    assert unicode_string == "test string"
