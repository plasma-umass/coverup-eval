# file lib/ansible/parsing/yaml/objects.py:71-73
# lines [71, 72, 73]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleSequence

def test_ansible_sequence_instantiation():
    # Test instantiation of AnsibleSequence
    sequence = AnsibleSequence([1, 2, 3])
    assert isinstance(sequence, AnsibleSequence)
    assert isinstance(sequence, list)
    assert sequence == [1, 2, 3]

def test_ansible_sequence_append():
    # Test appending to AnsibleSequence
    sequence = AnsibleSequence()
    sequence.append(1)
    assert sequence == [1]

def test_ansible_sequence_extend():
    # Test extending AnsibleSequence
    sequence = AnsibleSequence([1])
    sequence.extend([2, 3])
    assert sequence == [1, 2, 3]

def test_ansible_sequence_insert():
    # Test inserting into AnsibleSequence
    sequence = AnsibleSequence([1, 3])
    sequence.insert(1, 2)
    assert sequence == [1, 2, 3]

def test_ansible_sequence_remove():
    # Test removing from AnsibleSequence
    sequence = AnsibleSequence([1, 2, 3])
    sequence.remove(2)
    assert sequence == [1, 3]

def test_ansible_sequence_pop():
    # Test popping from AnsibleSequence
    sequence = AnsibleSequence([1, 2, 3])
    item = sequence.pop()
    assert item == 3
    assert sequence == [1, 2]

def test_ansible_sequence_clear():
    # Test clearing AnsibleSequence
    sequence = AnsibleSequence([1, 2, 3])
    sequence.clear()
    assert sequence == []

def test_ansible_sequence_index():
    # Test getting index from AnsibleSequence
    sequence = AnsibleSequence([1, 2, 3])
    index = sequence.index(2)
    assert index == 1

def test_ansible_sequence_count():
    # Test counting elements in AnsibleSequence
    sequence = AnsibleSequence([1, 2, 2, 3])
    count = sequence.count(2)
    assert count == 2

def test_ansible_sequence_sort():
    # Test sorting AnsibleSequence
    sequence = AnsibleSequence([3, 1, 2])
    sequence.sort()
    assert sequence == [1, 2, 3]

def test_ansible_sequence_reverse():
    # Test reversing AnsibleSequence
    sequence = AnsibleSequence([3, 2, 1])
    sequence.reverse()
    assert sequence == [1, 2, 3]

def test_ansible_sequence_copy():
    # Test copying AnsibleSequence
    sequence = AnsibleSequence([1, 2, 3])
    copy_sequence = sequence.copy()
    assert copy_sequence == sequence
    assert copy_sequence is not sequence
