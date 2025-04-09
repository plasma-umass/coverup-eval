# file: pymonet/immutable_list.py:27-45
# asked: {"lines": [27, 36, 37, 39, 40, 42, 43, 44], "branches": [[36, 37], [36, 39], [39, 40], [39, 42]]}
# gained: {"lines": [27, 36, 37, 39, 40, 42, 43, 44], "branches": [[36, 37], [36, 39], [39, 40], [39, 42]]}

import pytest
from pymonet.immutable_list import ImmutableList

def test_add_with_non_immutable_list():
    list1 = ImmutableList(1)
    with pytest.raises(ValueError, match='ImmutableList: you can not add any other instace than ImmutableList'):
        list1 + [2]

def test_add_with_empty_tail():
    list1 = ImmutableList(1)
    list2 = ImmutableList(2)
    result = list1 + list2
    assert result.head == 1
    assert result.tail.head == 2
    assert result.tail.tail is None

def test_add_with_non_empty_tail():
    list1 = ImmutableList(1, ImmutableList(2))
    list2 = ImmutableList(3)
    result = list1 + list2
    assert result.head == 1
    assert result.tail.head == 2
    assert result.tail.tail.head == 3
    assert result.tail.tail.tail is None
