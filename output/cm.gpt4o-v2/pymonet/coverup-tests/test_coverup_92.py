# file: pymonet/immutable_list.py:88-97
# asked: {"lines": [88, 97], "branches": []}
# gained: {"lines": [88, 97], "branches": []}

import pytest
from pymonet.immutable_list import ImmutableList

def test_unshift():
    # Create an initial ImmutableList
    initial_list = ImmutableList(1)
    
    # Use unshift to add a new element at the beginning
    new_list = initial_list.unshift(0)
    
    # Verify the new list has the new element at the beginning
    assert new_list.head == 0
    assert new_list.tail.head == 1

def test_add():
    # Create two ImmutableLists
    list1 = ImmutableList(1)
    list2 = ImmutableList(2)
    
    # Add the two lists
    combined_list = list1 + list2
    
    # Verify the combined list
    assert combined_list.head == 1
    assert combined_list.tail.head == 2

    # Test adding with an invalid type
    with pytest.raises(ValueError):
        list1 + [3]  # This should raise a ValueError

