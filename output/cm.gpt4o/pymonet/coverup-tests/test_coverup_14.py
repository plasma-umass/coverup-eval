# file pymonet/immutable_list.py:56-64
# lines [56, 57, 58, 59, 61, 62, 63]
# branches ['58->59', '58->61']

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_of():
    # Test with a single element
    single_element_list = ImmutableList.of(1)
    assert single_element_list.head == 1
    assert single_element_list.tail is None

    # Test with multiple elements
    multi_element_list = ImmutableList.of(1, 2, 3)
    assert multi_element_list.head == 1
    assert multi_element_list.tail.head == 2
    assert multi_element_list.tail.tail.head == 3
    assert multi_element_list.tail.tail.tail is None

    # Test with no elements (should raise an error)
    with pytest.raises(TypeError):
        ImmutableList.of()

    # Test with different types
    mixed_type_list = ImmutableList.of(1, "two", 3.0)
    assert mixed_type_list.head == 1
    assert mixed_type_list.tail.head == "two"
    assert mixed_type_list.tail.tail.head == 3.0
    assert mixed_type_list.tail.tail.tail is None
