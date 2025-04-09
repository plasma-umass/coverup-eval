# file: pymonet/immutable_list.py:13-16
# asked: {"lines": [13, 14, 15, 16], "branches": []}
# gained: {"lines": [13, 14, 15, 16], "branches": []}

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_init_with_head():
    head_value = 1
    lst = ImmutableList(head=head_value)
    assert lst.head == head_value
    assert lst.tail is None
    assert lst.is_empty is False

def test_immutable_list_init_with_tail():
    tail_list = ImmutableList(head=2)
    lst = ImmutableList(tail=tail_list)
    assert lst.head is None
    assert lst.tail == tail_list
    assert lst.is_empty is False

def test_immutable_list_init_with_is_empty():
    lst = ImmutableList(is_empty=True)
    assert lst.head is None
    assert lst.tail is None
    assert lst.is_empty is True

def test_immutable_list_init_with_all_params():
    head_value = 1
    tail_list = ImmutableList(head=2)
    lst = ImmutableList(head=head_value, tail=tail_list, is_empty=True)
    assert lst.head == head_value
    assert lst.tail == tail_list
    assert lst.is_empty is True
