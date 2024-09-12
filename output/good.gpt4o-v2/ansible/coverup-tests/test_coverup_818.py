# file: lib/ansible/parsing/yaml/objects.py:71-73
# asked: {"lines": [71, 72, 73], "branches": []}
# gained: {"lines": [71, 72, 73], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleBaseYAMLObject

def test_ansible_sequence_inheritance():
    seq = AnsibleSequence()
    assert isinstance(seq, AnsibleSequence)
    assert isinstance(seq, list)
    assert isinstance(seq, AnsibleBaseYAMLObject)
