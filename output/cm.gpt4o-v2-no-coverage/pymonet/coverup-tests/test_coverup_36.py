# file: pymonet/immutable_list.py:18-22
# asked: {"lines": [18, 19, 20, 21, 22], "branches": []}
# gained: {"lines": [18, 19, 20, 21, 22], "branches": []}

import pytest
from pymonet.immutable_list import ImmutableList

class TestImmutableList:
    def test_eq_with_equal_lists(self):
        list1 = ImmutableList()
        list1.head = 1
        list1.tail = ImmutableList()
        list1.is_empty = False

        list2 = ImmutableList()
        list2.head = 1
        list2.tail = ImmutableList()
        list2.is_empty = False

        assert list1 == list2

    def test_eq_with_different_heads(self):
        list1 = ImmutableList()
        list1.head = 1
        list1.tail = ImmutableList()
        list1.is_empty = False

        list2 = ImmutableList()
        list2.head = 2
        list2.tail = ImmutableList()
        list2.is_empty = False

        assert list1 != list2

    def test_eq_with_different_tails(self):
        list1 = ImmutableList()
        list1.head = 1
        list1.tail = ImmutableList()
        list1.is_empty = False

        list2 = ImmutableList()
        list2.head = 1
        list2.tail = None
        list2.is_empty = False

        assert list1 != list2

    def test_eq_with_different_is_empty(self):
        list1 = ImmutableList()
        list1.head = 1
        list1.tail = ImmutableList()
        list1.is_empty = False

        list2 = ImmutableList()
        list2.head = 1
        list2.tail = ImmutableList()
        list2.is_empty = True

        assert list1 != list2

    def test_eq_with_non_immutable_list(self):
        list1 = ImmutableList()
        list1.head = 1
        list1.tail = ImmutableList()
        list1.is_empty = False

        assert list1 != [1, 2, 3]
