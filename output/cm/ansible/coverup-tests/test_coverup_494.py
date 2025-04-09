# file lib/ansible/module_utils/common/collections.py:31-38
# lines [31, 32, 33, 34, 35, 36, 38]
# branches ['33->34', '33->38']

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_eq():
    # Create two ImmutableDict instances with the same content
    dict_a = ImmutableDict({'key': 'value'})
    dict_b = ImmutableDict({'key': 'value'})
    
    # Create a regular dict with the same content
    regular_dict = {'key': 'value'}
    
    # Create an object that will raise a TypeError when hashed
    class Unhashable:
        def __hash__(self):
            raise TypeError
    
    unhashable = Unhashable()
    
    # Test equality comparison with another ImmutableDict with the same content
    assert dict_a == dict_b
    
    # Test equality comparison with a regular dict with the same content
    # This should not be equal as ImmutableDict does not intend to be equal to a regular dict
    assert not (dict_a == regular_dict)
    
    # Test equality comparison with an unhashable object
    assert not (dict_a == unhashable)
    
    # Test equality comparison with an object of different content
    assert not (dict_a == {'other_key': 'other_value'})
    
    # Test equality comparison with an object of a different type
    assert not (dict_a == 42)
