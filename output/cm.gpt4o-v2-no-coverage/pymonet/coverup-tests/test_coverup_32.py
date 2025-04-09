# file: pymonet/immutable_list.py:71-75
# asked: {"lines": [71, 72, 73, 75], "branches": [[72, 73], [72, 75]]}
# gained: {"lines": [71, 72, 73, 75], "branches": [[72, 73], [72, 75]]}

import pytest
from pymonet.immutable_list import ImmutableList

def test_to_list_with_tail():
    tail = ImmutableList(2)
    lst = ImmutableList(1, tail)
    result = lst.to_list()
    assert result == [1, 2]

def test_to_list_without_tail():
    lst = ImmutableList(1)
    result = lst.to_list()
    assert result == [1]

def test_to_list_empty():
    lst = ImmutableList()
    result = lst.to_list()
    assert result == [None]
