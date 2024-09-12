# file: pymonet/immutable_list.py:152-168
# asked: {"lines": [152, 161, 162, 164, 165, 168], "branches": [[161, 162], [161, 164], [164, 165], [164, 168]]}
# gained: {"lines": [152, 161, 162, 164, 165, 168], "branches": [[161, 162], [161, 164], [164, 165], [164, 168]]}

import pytest
from pymonet.immutable_list import ImmutableList

class TestImmutableList:
    def test_reduce_empty_list(self):
        empty_list = ImmutableList()
        result = empty_list.reduce(lambda acc, x: acc + x, 0)
        assert result == 0

    def test_reduce_single_element_list(self):
        single_element_list = ImmutableList()
        single_element_list.head = 5
        single_element_list.tail = None
        result = single_element_list.reduce(lambda acc, x: acc + x, 0)
        assert result == 5

    def test_reduce_multiple_elements_list(self):
        list_with_elements = ImmutableList()
        list_with_elements.head = 1
        list_with_elements.tail = ImmutableList()
        list_with_elements.tail.head = 2
        list_with_elements.tail.tail = ImmutableList()
        list_with_elements.tail.tail.head = 3
        list_with_elements.tail.tail.tail = None
        result = list_with_elements.reduce(lambda acc, x: acc + x, 0)
        assert result == 6

    def test_reduce_with_different_accumulator(self):
        list_with_elements = ImmutableList()
        list_with_elements.head = 1
        list_with_elements.tail = ImmutableList()
        list_with_elements.tail.head = 2
        list_with_elements.tail.tail = ImmutableList()
        list_with_elements.tail.tail.head = 3
        list_with_elements.tail.tail.tail = None
        result = list_with_elements.reduce(lambda acc, x: acc * x, 1)
        assert result == 6
