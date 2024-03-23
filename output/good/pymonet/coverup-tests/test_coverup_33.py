# file pymonet/immutable_list.py:13-16
# lines [13, 14, 15, 16]
# branches []

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_init():
    # Test initializing with default values
    empty_list = ImmutableList()
    assert empty_list.head is None
    assert empty_list.tail is None
    assert empty_list.is_empty is False

    # Test initializing with a head value
    head_value = 'head'
    list_with_head = ImmutableList(head=head_value)
    assert list_with_head.head == head_value
    assert list_with_head.tail is None
    assert list_with_head.is_empty is False

    # Test initializing with a tail value
    tail_list = ImmutableList()
    list_with_tail = ImmutableList(tail=tail_list)
    assert list_with_tail.head is None
    assert list_with_tail.tail == tail_list
    assert list_with_tail.is_empty is False

    # Test initializing with is_empty=True
    empty_list_by_flag = ImmutableList(is_empty=True)
    assert empty_list_by_flag.head is None
    assert empty_list_by_flag.tail is None
    assert empty_list_by_flag.is_empty is True
