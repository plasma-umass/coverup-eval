# file: lib/ansible/parsing/yaml/objects.py:61-63
# asked: {"lines": [61, 62, 63], "branches": []}
# gained: {"lines": [61, 62, 63], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

class AnsibleMapping(AnsibleBaseYAMLObject, dict):
    ''' sub class for dictionaries '''
    pass

def test_ansible_mapping_is_instance_of_dict():
    obj = AnsibleMapping()
    assert isinstance(obj, dict), "AnsibleMapping should be an instance of dict"

def test_ansible_mapping_is_instance_of_ansible_base_yaml_object():
    obj = AnsibleMapping()
    assert isinstance(obj, AnsibleBaseYAMLObject), "AnsibleMapping should be an instance of AnsibleBaseYAMLObject"

def test_ansible_mapping_dict_behavior():
    obj = AnsibleMapping()
    obj['key'] = 'value'
    assert obj['key'] == 'value', "AnsibleMapping should behave like a dictionary"
    del obj['key']
    assert 'key' not in obj, "AnsibleMapping should support item deletion like a dictionary"
