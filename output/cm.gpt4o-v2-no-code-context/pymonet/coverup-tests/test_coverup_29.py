# file: pymonet/immutable_list.py:18-22
# asked: {"lines": [18, 19, 20, 21, 22], "branches": []}
# gained: {"lines": [18, 19, 20, 21, 22], "branches": []}

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_eq_with_non_list():
    list1 = ImmutableList()
    assert not list1 == "not a list"

def test_immutable_list_eq_with_different_head():
    list1 = ImmutableList()
    list1.head = 1
    list1.tail = ImmutableList()
    list1.is_empty = False

    list2 = ImmutableList()
    list2.head = 2
    list2.tail = ImmutableList()
    list2.is_empty = False

    assert not list1 == list2

def test_immutable_list_eq_with_different_tail():
    list1 = ImmutableList()
    list1.head = 1
    list1.tail = ImmutableList()
    list1.is_empty = False

    list2 = ImmutableList()
    list2.head = 1
    list2.tail = ImmutableList()
    list2.tail.head = 2
    list2.is_empty = False

    assert not list1 == list2

def test_immutable_list_eq_with_different_is_empty():
    list1 = ImmutableList()
    list1.head = 1
    list1.tail = ImmutableList()
    list1.is_empty = False

    list2 = ImmutableList()
    list2.head = 1
    list2.tail = ImmutableList()
    list2.is_empty = True

    assert not list1 == list2

def test_immutable_list_eq_with_equal_lists():
    list1 = ImmutableList()
    list1.head = 1
    list1.tail = ImmutableList()
    list1.is_empty = False

    list2 = ImmutableList()
    list2.head = 1
    list2.tail = ImmutableList()
    list2.is_empty = False

    assert list1 == list2
