# file: pymonet/immutable_list.py:113-130
# asked: {"lines": [113, 122, 123, 124, 125, 127, 128, 130], "branches": [[122, 123], [122, 127], [123, 124], [123, 125], [127, 128], [127, 130]]}
# gained: {"lines": [113, 122, 123, 124, 125, 127, 128, 130], "branches": [[122, 123], [122, 127], [123, 124], [123, 125], [127, 128], [127, 130]]}

import pytest
from pymonet.immutable_list import ImmutableList

def test_filter_empty_list():
    empty_list = ImmutableList(is_empty=True)
    result = empty_list.filter(lambda x: x is not None)
    assert result.is_empty

def test_filter_single_element_list_pass():
    single_element_list = ImmutableList(1)
    result = single_element_list.filter(lambda x: x == 1)
    assert not result.is_empty
    assert result.head == 1
    assert result.tail is None

def test_filter_single_element_list_fail():
    single_element_list = ImmutableList(1)
    result = single_element_list.filter(lambda x: x != 1)
    assert result.is_empty

def test_filter_multiple_elements_all_pass():
    multiple_elements_list = ImmutableList.of(1, 2, 3)
    result = multiple_elements_list.filter(lambda x: x > 0)
    assert not result.is_empty
    assert result.head == 1
    assert result.tail.head == 2
    assert result.tail.tail.head == 3
    assert result.tail.tail.tail is None

def test_filter_multiple_elements_some_pass():
    multiple_elements_list = ImmutableList.of(1, 2, 3)
    result = multiple_elements_list.filter(lambda x: x > 1)
    assert not result.is_empty
    assert result.head == 2
    assert result.tail.head == 3
    assert result.tail.tail is None

def test_filter_multiple_elements_none_pass():
    multiple_elements_list = ImmutableList.of(1, 2, 3)
    result = multiple_elements_list.filter(lambda x: x > 3)
    assert result.is_empty
