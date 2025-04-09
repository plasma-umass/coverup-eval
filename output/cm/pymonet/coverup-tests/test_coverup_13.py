# file pymonet/immutable_list.py:56-64
# lines [56, 57, 58, 59, 61, 62, 63]
# branches ['58->59', '58->61']

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_of_with_multiple_elements():
    # Test ImmutableList.of with multiple elements to ensure full coverage
    result = ImmutableList.of(1, 2, 3, 4, 5)
    
    # Verify that the result is an ImmutableList and has the correct elements
    assert isinstance(result, ImmutableList)
    assert result.head == 1
    assert result.tail.head == 2
    assert result.tail.tail.head == 3
    assert result.tail.tail.tail.head == 4
    assert result.tail.tail.tail.tail.head == 5
    assert result.tail.tail.tail.tail.tail is None

def test_immutable_list_of_with_single_element():
    # Test ImmutableList.of with a single element to ensure full coverage
    result = ImmutableList.of(1)
    
    # Verify that the result is an ImmutableList and has the correct element
    assert isinstance(result, ImmutableList)
    assert result.head == 1
    assert result.tail is None
