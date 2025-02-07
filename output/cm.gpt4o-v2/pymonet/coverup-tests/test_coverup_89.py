# file: pymonet/immutable_list.py:77-86
# asked: {"lines": [77, 86], "branches": []}
# gained: {"lines": [77, 86], "branches": []}

import pytest
from pymonet.immutable_list import ImmutableList

def test_append():
    # Create an initial ImmutableList
    initial_list = ImmutableList(1)
    
    # Append a new element to the list
    new_list = initial_list.append(2)
    
    # Verify the new list has the appended element
    assert new_list.head == 1
    assert new_list.tail.head == 2
    assert new_list.tail.tail is None

    # Clean up
    del initial_list
    del new_list
