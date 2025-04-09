# file lib/ansible/module_utils/common/collections.py:55-65
# lines [55, 63, 64, 65]
# branches []

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_difference():
    # Create an instance of ImmutableDict
    original_dict = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    
    # Define the subtractive iterable
    subtractive_iterable = ['b', 'c']
    
    # Call the difference method
    new_dict = original_dict.difference(subtractive_iterable)
    
    # Verify the new ImmutableDict does not contain the keys in subtractive_iterable
    assert 'b' not in new_dict
    assert 'c' not in new_dict
    
    # Verify the new ImmutableDict contains the remaining keys
    assert 'a' in new_dict
    assert new_dict['a'] == 1
    
    # Verify the original ImmutableDict is unchanged
    assert 'b' in original_dict
    assert 'c' in original_dict
    assert original_dict['b'] == 2
    assert original_dict['c'] == 3

@pytest.fixture(autouse=True)
def cleanup(mocker):
    # Mock any necessary cleanup actions here
    yield
    # Perform cleanup actions here if necessary
