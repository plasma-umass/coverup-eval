# file pymonet/immutable_list.py:99-111
# lines [99, 108, 109, 111]
# branches ['108->109', '108->111']

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_map():
    # Create a simple ImmutableList and a function to map over it
    original_list = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    fn = lambda x: x * 2

    # Map the function over the ImmutableList
    mapped_list = original_list.map(fn)

    # Check that the resulting ImmutableList has the correct values
    assert mapped_list.head == 2
    assert mapped_list.tail.head == 4
    assert mapped_list.tail.tail.head == 6
    assert mapped_list.tail.tail.tail is None

    # Check that the original ImmutableList is unchanged
    assert original_list.head == 1
    assert original_list.tail.head == 2
    assert original_list.tail.tail.head == 3
    assert original_list.tail.tail.tail is None

def test_immutable_list_map_single_element():
    # Create a single-element ImmutableList and a function to map over it
    single_element_list = ImmutableList(1)
    fn = lambda x: x + 10

    # Map the function over the ImmutableList
    mapped_list = single_element_list.map(fn)

    # Check that the resulting ImmutableList has the correct value
    assert mapped_list.head == 11
    assert mapped_list.tail is None

    # Check that the original ImmutableList is unchanged
    assert single_element_list.head == 1
    assert single_element_list.tail is None
