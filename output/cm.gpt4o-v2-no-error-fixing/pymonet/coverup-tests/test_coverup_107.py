# file: pymonet/immutable_list.py:88-97
# asked: {"lines": [97], "branches": []}
# gained: {"lines": [97], "branches": []}

import pytest
from pymonet.immutable_list import ImmutableList

def test_unshift():
    # Create an initial ImmutableList
    initial_list = ImmutableList(2)
    
    # Use unshift to add a new element at the beginning
    new_list = initial_list.unshift(1)
    
    # Verify the new list has the new element at the beginning
    assert new_list.head == 1
    assert new_list.tail.head == 2

    # Verify the tail of the new list is the initial list
    assert new_list.tail == initial_list

    # Verify the new list is not empty
    assert not new_list.is_empty
