# file lib/ansible/parsing/yaml/objects.py:61-63
# lines [61, 62, 63]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

def test_ansible_mapping():
    class AnsibleMapping(AnsibleBaseYAMLObject, dict):
        ''' sub class for dictionaries '''
        pass

    # Create an instance of AnsibleMapping
    mapping = AnsibleMapping()

    # Verify that the instance is a subclass of AnsibleBaseYAMLObject and dict
    assert isinstance(mapping, AnsibleBaseYAMLObject)
    assert isinstance(mapping, dict)

    # Verify that the instance behaves like a dictionary
    mapping['key'] = 'value'
    assert mapping['key'] == 'value'
    assert len(mapping) == 1

    # Clean up
    del mapping
