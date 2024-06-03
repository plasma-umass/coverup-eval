# file pymonet/immutable_list.py:71-75
# lines [71, 72, 73, 75]
# branches ['72->73', '72->75']

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_to_list():
    # Test case where tail is None
    list_with_no_tail = ImmutableList()
    list_with_no_tail.head = 1
    list_with_no_tail.tail = None
    assert list_with_no_tail.to_list() == [1]

    # Test case where tail is not None
    tail_list = ImmutableList()
    tail_list.head = 2
    tail_list.tail = None

    list_with_tail = ImmutableList()
    list_with_tail.head = 1
    list_with_tail.tail = tail_list

    assert list_with_tail.to_list() == [1, 2]
