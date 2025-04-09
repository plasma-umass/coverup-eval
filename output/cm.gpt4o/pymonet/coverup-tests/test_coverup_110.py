# file pymonet/immutable_list.py:132-150
# lines [148]
# branches ['147->148']

import pytest
from pymonet.immutable_list import ImmutableList

def test_find_executes_line_148():
    # Create a mock function that will return True when called with the head element
    mock_fn = lambda x: x == 1

    # Create an ImmutableList with head element that matches the mock function condition
    list_with_matching_head = ImmutableList()
    list_with_matching_head.head = 1
    list_with_matching_head.tail = ImmutableList()
    list_with_matching_head.tail.head = 2
    list_with_matching_head.tail.tail = None

    # Call the find method and assert that it returns the head element
    result = list_with_matching_head.find(mock_fn)
    assert result == 1

    # Clean up
    del list_with_matching_head
    del mock_fn
