# file: lib/ansible/parsing/yaml/objects.py:71-73
# asked: {"lines": [71, 72, 73], "branches": []}
# gained: {"lines": [71, 72, 73], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

class AnsibleSequence(AnsibleBaseYAMLObject, list):
    ''' sub class for lists '''
    pass

def test_ansible_sequence_inheritance():
    seq = AnsibleSequence()
    assert isinstance(seq, AnsibleBaseYAMLObject)
    assert isinstance(seq, list)

def test_ansible_sequence_functionality():
    seq = AnsibleSequence([1, 2, 3])
    assert seq == [1, 2, 3]
    seq.append(4)
    assert seq == [1, 2, 3, 4]
    seq.remove(2)
    assert seq == [1, 3, 4]
