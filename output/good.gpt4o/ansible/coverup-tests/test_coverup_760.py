# file lib/ansible/parsing/yaml/objects.py:71-73
# lines [71, 72, 73]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

class AnsibleSequence(AnsibleBaseYAMLObject, list):
    ''' sub class for lists '''
    pass

def test_ansible_sequence():
    # Create an instance of AnsibleSequence
    ansible_sequence = AnsibleSequence([1, 2, 3])

    # Verify that it is an instance of AnsibleSequence, AnsibleBaseYAMLObject, and list
    assert isinstance(ansible_sequence, AnsibleSequence)
    assert isinstance(ansible_sequence, AnsibleBaseYAMLObject)
    assert isinstance(ansible_sequence, list)

    # Verify the contents of the list
    assert ansible_sequence == [1, 2, 3]

    # Verify list operations
    ansible_sequence.append(4)
    assert ansible_sequence == [1, 2, 3, 4]

    ansible_sequence.remove(2)
    assert ansible_sequence == [1, 3, 4]

    # Clean up
    del ansible_sequence
