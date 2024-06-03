# file lib/ansible/module_utils/common/collections.py:31-38
# lines [32, 33, 34, 35, 36, 38]
# branches ['33->34', '33->38']

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_eq_with_hashable(mocker):
    # Create a mock object for the other dictionary
    other_dict = mocker.Mock()
    mocker.patch.object(other_dict, '__hash__', return_value=hash(frozenset({'key': 'value'}.items())))

    # Create an ImmutableDict instance
    imm_dict = ImmutableDict({'key': 'value'})

    # Test equality with a hashable object
    assert imm_dict == other_dict

def test_immutable_dict_eq_with_non_hashable():
    # Create an ImmutableDict instance
    imm_dict = ImmutableDict({'key': 'value'})

    # Test equality with a non-hashable object
    assert not imm_dict == {'key': 'value'}
