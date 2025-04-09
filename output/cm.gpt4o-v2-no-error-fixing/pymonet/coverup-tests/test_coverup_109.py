# file: pymonet/immutable_list.py:113-130
# asked: {"lines": [122, 123, 124, 125, 127, 128, 130], "branches": [[122, 123], [122, 127], [123, 124], [123, 125], [127, 128], [127, 130]]}
# gained: {"lines": [122, 123, 124, 125, 127, 128, 130], "branches": [[122, 123], [122, 127], [123, 124], [123, 125], [127, 128], [127, 130]]}

import pytest
from pymonet.immutable_list import ImmutableList

def test_filter_empty_list():
    empty_list = ImmutableList(is_empty=True)
    result = empty_list.filter(lambda x: x is not None)
    assert result.is_empty

def test_filter_single_element_list_true():
    single_element_list = ImmutableList(1)
    result = single_element_list.filter(lambda x: x == 1)
    assert result.head == 1
    assert result.tail is None

def test_filter_single_element_list_false():
    single_element_list = ImmutableList(1)
    result = single_element_list.filter(lambda x: x == 2)
    assert result.is_empty

def test_filter_multiple_elements():
    list_with_elements = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    result = list_with_elements.filter(lambda x: x % 2 == 1)
    assert result.head == 1
    assert result.tail.head == 3
    assert result.tail.tail is None

def test_filter_multiple_elements_all_false():
    list_with_elements = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    result = list_with_elements.filter(lambda x: x > 3)
    assert result.is_empty
