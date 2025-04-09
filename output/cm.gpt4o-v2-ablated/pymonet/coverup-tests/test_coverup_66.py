# file: pymonet/immutable_list.py:132-150
# asked: {"lines": [141, 142, 144, 145, 147, 148, 150], "branches": [[141, 142], [141, 144], [144, 145], [144, 147], [147, 148], [147, 150]]}
# gained: {"lines": [141, 142, 144, 145, 147, 150], "branches": [[141, 142], [141, 144], [144, 145], [144, 147], [147, 150]]}

import pytest
from pymonet.immutable_list import ImmutableList

class TestImmutableList:
    def test_find_empty_list(self):
        lst = ImmutableList()
        assert lst.find(lambda x: x is not None) is None

    def test_find_single_element_list_match(self):
        lst = ImmutableList()
        lst.head = 1
        lst.tail = None
        assert lst.find(lambda x: x == 1) == 1

    def test_find_single_element_list_no_match(self):
        lst = ImmutableList()
        lst.head = 1
        lst.tail = None
        assert lst.find(lambda x: x == 2) is None

    def test_find_multiple_elements_match(self):
        lst1 = ImmutableList()
        lst1.head = 2
        lst1.tail = None

        lst2 = ImmutableList()
        lst2.head = 1
        lst2.tail = lst1

        assert lst2.find(lambda x: x == 2) == 2

    def test_find_multiple_elements_no_match(self):
        lst1 = ImmutableList()
        lst1.head = 2
        lst1.tail = None

        lst2 = ImmutableList()
        lst2.head = 1
        lst2.tail = lst1

        assert lst2.find(lambda x: x == 3) is None
