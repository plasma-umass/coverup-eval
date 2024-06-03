# file pymonet/immutable_list.py:132-150
# lines [132, 141, 142, 144, 145, 147, 148, 150]
# branches ['141->142', '141->144', '144->145', '144->147', '147->148', '147->150']

import pytest
from pymonet.immutable_list import ImmutableList

class TestImmutableList:
    def test_find_empty_list(self):
        lst = ImmutableList()
        result = lst.find(lambda x: x is not None)
        assert result is None

    def test_find_single_element_list_match(self):
        lst = ImmutableList()
        lst.head = 1
        lst.tail = None
        result = lst.find(lambda x: x == 1)
        assert result == 1

    def test_find_single_element_list_no_match(self):
        lst = ImmutableList()
        lst.head = 1
        lst.tail = None
        result = lst.find(lambda x: x == 2)
        assert result is None

    def test_find_multiple_elements_list_match(self):
        lst = ImmutableList()
        lst.head = 1
        lst.tail = ImmutableList()
        lst.tail.head = 2
        lst.tail.tail = None
        result = lst.find(lambda x: x == 2)
        assert result == 2

    def test_find_multiple_elements_list_no_match(self):
        lst = ImmutableList()
        lst.head = 1
        lst.tail = ImmutableList()
        lst.tail.head = 2
        lst.tail.tail = None
        result = lst.find(lambda x: x == 3)
        assert result is None
