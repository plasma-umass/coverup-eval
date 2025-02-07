# file: pymonet/immutable_list.py:18-22
# asked: {"lines": [18, 19, 20, 21, 22], "branches": []}
# gained: {"lines": [18, 19, 20, 21, 22], "branches": []}

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_equality():
    # Test equality with same values
    list1 = ImmutableList(1, ImmutableList(2, ImmutableList(3, is_empty=True)))
    list2 = ImmutableList(1, ImmutableList(2, ImmutableList(3, is_empty=True)))
    assert list1 == list2

    # Test inequality with different head
    list3 = ImmutableList(4, ImmutableList(2, ImmutableList(3, is_empty=True)))
    assert list1 != list3

    # Test inequality with different tail
    list4 = ImmutableList(1, ImmutableList(5, ImmutableList(3, is_empty=True)))
    assert list1 != list4

    # Test inequality with different is_empty
    list5 = ImmutableList(1, ImmutableList(2, ImmutableList(3, is_empty=False)))
    assert list1 != list5

    # Test equality with empty lists
    empty_list1 = ImmutableList(is_empty=True)
    empty_list2 = ImmutableList(is_empty=True)
    assert empty_list1 == empty_list2

    # Test inequality with one empty and one non-empty list
    non_empty_list = ImmutableList(1, is_empty=False)
    assert empty_list1 != non_empty_list
