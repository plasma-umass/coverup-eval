# file: lib/ansible/parsing/yaml/objects.py:71-73
# asked: {"lines": [71, 72, 73], "branches": []}
# gained: {"lines": [71, 72, 73], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleSequence

def test_ansible_sequence_inheritance():
    seq = AnsibleSequence()
    assert isinstance(seq, AnsibleSequence)
    assert isinstance(seq, list)

def test_ansible_sequence_append():
    seq = AnsibleSequence()
    seq.append(1)
    assert seq == [1]

def test_ansible_sequence_extend():
    seq = AnsibleSequence()
    seq.extend([1, 2, 3])
    assert seq == [1, 2, 3]

def test_ansible_sequence_clear():
    seq = AnsibleSequence([1, 2, 3])
    seq.clear()
    assert seq == []

def test_ansible_sequence_insert():
    seq = AnsibleSequence([1, 3])
    seq.insert(1, 2)
    assert seq == [1, 2, 3]

def test_ansible_sequence_remove():
    seq = AnsibleSequence([1, 2, 3])
    seq.remove(2)
    assert seq == [1, 3]

def test_ansible_sequence_pop():
    seq = AnsibleSequence([1, 2, 3])
    item = seq.pop(1)
    assert item == 2
    assert seq == [1, 3]

def test_ansible_sequence_index():
    seq = AnsibleSequence([1, 2, 3])
    index = seq.index(2)
    assert index == 1

def test_ansible_sequence_count():
    seq = AnsibleSequence([1, 2, 2, 3])
    count = seq.count(2)
    assert count == 2

def test_ansible_sequence_sort():
    seq = AnsibleSequence([3, 1, 2])
    seq.sort()
    assert seq == [1, 2, 3]

def test_ansible_sequence_reverse():
    seq = AnsibleSequence([1, 2, 3])
    seq.reverse()
    assert seq == [3, 2, 1]
