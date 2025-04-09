# file: lib/ansible/parsing/yaml/objects.py:61-63
# asked: {"lines": [61, 62, 63], "branches": []}
# gained: {"lines": [61, 62, 63], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleBaseYAMLObject

def test_ansible_mapping_inheritance():
    obj = AnsibleMapping()
    assert isinstance(obj, AnsibleMapping)
    assert isinstance(obj, AnsibleBaseYAMLObject)
    assert isinstance(obj, dict)

def test_ansible_mapping_dict_behavior():
    obj = AnsibleMapping()
    obj['key'] = 'value'
    assert obj['key'] == 'value'
    assert len(obj) == 1
    del obj['key']
    assert 'key' not in obj
    assert len(obj) == 0
