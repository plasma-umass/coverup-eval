# file: pymonet/immutable_list.py:152-168
# asked: {"lines": [152, 161, 162, 164, 165, 168], "branches": [[161, 162], [161, 164], [164, 165], [164, 168]]}
# gained: {"lines": [152, 161, 162, 164, 165, 168], "branches": [[161, 162], [161, 164], [164, 165], [164, 168]]}

import pytest
from pymonet.immutable_list import ImmutableList

def test_reduce_empty_list():
    empty_list = ImmutableList()
    result = empty_list.reduce(lambda acc, x: acc + x, 0)
    assert result == 0

def test_reduce_single_element_list():
    single_element_list = ImmutableList(1)
    result = single_element_list.reduce(lambda acc, x: acc + x, 0)
    assert result == 1

def test_reduce_multiple_elements_list():
    multiple_elements_list = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    result = multiple_elements_list.reduce(lambda acc, x: acc + x, 0)
    assert result == 6

def test_reduce_with_non_zero_initial_acc():
    multiple_elements_list = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    result = multiple_elements_list.reduce(lambda acc, x: acc + x, 10)
    assert result == 16
