# file: pymonet/immutable_list.py:152-168
# asked: {"lines": [152, 161, 162, 164, 165, 168], "branches": [[161, 162], [161, 164], [164, 165], [164, 168]]}
# gained: {"lines": [152, 161, 162, 164, 165, 168], "branches": [[161, 162], [161, 164], [164, 165], [164, 168]]}

import pytest
from pymonet.immutable_list import ImmutableList

def test_reduce_empty_list():
    lst = ImmutableList()
    result = lst.reduce(lambda acc, x: acc + x, 0)
    assert result == 0

def test_reduce_single_element():
    lst = ImmutableList.of(1)
    result = lst.reduce(lambda acc, x: acc + x, 0)
    assert result == 1

def test_reduce_multiple_elements():
    lst = ImmutableList.of(1, 2, 3)
    result = lst.reduce(lambda acc, x: acc + x, 0)
    assert result == 6

def test_reduce_with_non_zero_initial():
    lst = ImmutableList.of(1, 2, 3)
    result = lst.reduce(lambda acc, x: acc + x, 10)
    assert result == 16

def test_reduce_with_different_function():
    lst = ImmutableList.of(1, 2, 3)
    result = lst.reduce(lambda acc, x: acc * x, 1)
    assert result == 6
