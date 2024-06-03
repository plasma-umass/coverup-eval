# file pymonet/immutable_list.py:13-16
# lines [13, 14, 15, 16]
# branches []

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_initialization():
    # Test initialization with default parameters
    empty_list = ImmutableList()
    assert empty_list.head is None
    assert empty_list.tail is None
    assert empty_list.is_empty is False

    # Test initialization with head only
    head_only_list = ImmutableList(head=1)
    assert head_only_list.head == 1
    assert head_only_list.tail is None
    assert head_only_list.is_empty is False

    # Test initialization with head and tail
    tail_list = ImmutableList(head=2)
    head_and_tail_list = ImmutableList(head=1, tail=tail_list)
    assert head_and_tail_list.head == 1
    assert head_and_tail_list.tail == tail_list
    assert head_and_tail_list.is_empty is False

    # Test initialization with is_empty flag
    empty_flag_list = ImmutableList(is_empty=True)
    assert empty_flag_list.head is None
    assert empty_flag_list.tail is None
    assert empty_flag_list.is_empty is True
