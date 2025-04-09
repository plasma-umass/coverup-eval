# file: pymonet/immutable_list.py:99-111
# asked: {"lines": [108, 109, 111], "branches": [[108, 109], [108, 111]]}
# gained: {"lines": [108, 109, 111], "branches": [[108, 109], [108, 111]]}

import pytest
from pymonet.immutable_list import ImmutableList

def test_map_with_empty_tail():
    # Create an ImmutableList with a single element
    lst = ImmutableList(1)
    
    # Define a simple mapping function
    def increment(x):
        return x + 1
    
    # Apply the map function
    new_lst = lst.map(increment)
    
    # Verify the new list has the mapped value
    assert new_lst.head == 2
    assert new_lst.tail is None

def test_map_with_non_empty_tail():
    # Create an ImmutableList with multiple elements
    lst = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    
    # Define a simple mapping function
    def increment(x):
        return x + 1
    
    # Apply the map function
    new_lst = lst.map(increment)
    
    # Verify the new list has the mapped values
    assert new_lst.head == 2
    assert new_lst.tail.head == 3
    assert new_lst.tail.tail.head == 4
    assert new_lst.tail.tail.tail is None
