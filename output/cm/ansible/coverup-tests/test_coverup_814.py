# file lib/ansible/parsing/yaml/objects.py:61-63
# lines [61, 62, 63]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleMapping

def test_ansible_mapping_instantiation():
    # Test instantiation of AnsibleMapping
    mapping = AnsibleMapping()
    assert isinstance(mapping, AnsibleMapping)
    assert isinstance(mapping, dict)

    # Test that AnsibleMapping can be used as a dictionary
    mapping['key'] = 'value'
    assert mapping['key'] == 'value'
    assert 'key' in mapping
    assert len(mapping) == 1

    # Test that AnsibleMapping can be cleared
    mapping.clear()
    assert len(mapping) == 0
