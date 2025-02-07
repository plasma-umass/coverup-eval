# file: pymonet/immutable_list.py:47-54
# asked: {"lines": [47, 48, 49, 51, 52, 54], "branches": [[48, 49], [48, 51], [51, 52], [51, 54]]}
# gained: {"lines": [47, 48, 49, 51, 52, 54], "branches": [[48, 49], [48, 51], [51, 52], [51, 54]]}

import pytest
from pymonet.immutable_list import ImmutableList

def test_len_empty_list():
    empty_list = ImmutableList()
    assert len(empty_list) == 0

def test_len_single_element_list():
    single_element_list = ImmutableList(1)
    assert len(single_element_list) == 1

def test_len_multiple_elements_list():
    tail = ImmutableList(2)
    head = ImmutableList(1, tail)
    assert len(head) == 2

def test_len_nested_list():
    tail_tail = ImmutableList(3)
    tail = ImmutableList(2, tail_tail)
    head = ImmutableList(1, tail)
    assert len(head) == 3
