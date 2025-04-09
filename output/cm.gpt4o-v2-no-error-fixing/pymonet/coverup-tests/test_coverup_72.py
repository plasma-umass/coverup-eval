# file: pymonet/immutable_list.py:77-86
# asked: {"lines": [77, 86], "branches": []}
# gained: {"lines": [77, 86], "branches": []}

import pytest
from pymonet.immutable_list import ImmutableList

def test_append():
    # Create an initial ImmutableList
    initial_list = ImmutableList.of(1, 2, 3)
    
    # Append a new element
    new_list = initial_list.append(4)
    
    # Verify the new list has the appended element
    assert new_list.to_list() == [1, 2, 3, 4]
    
    # Verify the original list is unchanged
    assert initial_list.to_list() == [1, 2, 3]

    # Clean up
    del initial_list
    del new_list
