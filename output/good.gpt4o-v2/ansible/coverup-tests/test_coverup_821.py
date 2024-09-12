# file: lib/ansible/parsing/yaml/objects.py:61-63
# asked: {"lines": [61, 62, 63], "branches": []}
# gained: {"lines": [61, 62, 63], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleBaseYAMLObject

def test_ansible_mapping_is_instance_of_dict_and_ansiblebaseyamlobject():
    obj = AnsibleMapping()
    assert isinstance(obj, dict)
    assert isinstance(obj, AnsibleBaseYAMLObject)
