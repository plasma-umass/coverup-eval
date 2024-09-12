# file: pymonet/immutable_list.py:13-16
# asked: {"lines": [13, 14, 15, 16], "branches": []}
# gained: {"lines": [13, 14, 15, 16], "branches": []}

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_initialization_with_head():
    lst = ImmutableList(head=1)
    assert lst.head == 1
    assert lst.tail is None
    assert not lst.is_empty

def test_immutable_list_initialization_with_tail():
    tail_list = ImmutableList(head=2)
    lst = ImmutableList(head=1, tail=tail_list)
    assert lst.head == 1
    assert lst.tail == tail_list
    assert not lst.is_empty

def test_immutable_list_initialization_empty():
    lst = ImmutableList(is_empty=True)
    assert lst.head is None
    assert lst.tail is None
    assert lst.is_empty

def test_immutable_list_initialization_default():
    lst = ImmutableList()
    assert lst.head is None
    assert lst.tail is None
    assert not lst.is_empty
