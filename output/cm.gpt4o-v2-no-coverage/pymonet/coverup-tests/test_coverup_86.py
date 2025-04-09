# file: pymonet/immutable_list.py:88-97
# asked: {"lines": [88, 97], "branches": []}
# gained: {"lines": [88, 97], "branches": []}

import pytest
from pymonet.immutable_list import ImmutableList

def test_unshift():
    # Create an empty ImmutableList
    empty_list = ImmutableList.empty()
    
    # Unshift an element to the empty list
    new_list = empty_list.unshift(1)
    
    # Verify the new list is not empty and has the correct head element
    assert not new_list.is_empty
    assert new_list.head == 1
    
    # Verify the tail of the new list is the original empty list
    assert new_list.tail == empty_list
    
    # Create a non-empty ImmutableList
    non_empty_list = ImmutableList.of(2, 3)
    
    # Unshift an element to the non-empty list
    new_list = non_empty_list.unshift(1)
    
    # Verify the new list has the correct head element
    assert new_list.head == 1
    
    # Verify the tail of the new list is the original non-empty list
    assert new_list.tail == non_empty_list

    # Verify the length of the new list
    assert len(new_list) == len(non_empty_list) + 1
