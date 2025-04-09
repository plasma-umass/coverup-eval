# file: pymonet/immutable_list.py:99-111
# asked: {"lines": [108, 109, 111], "branches": [[108, 109], [108, 111]]}
# gained: {"lines": [108, 109, 111], "branches": [[108, 109], [108, 111]]}

import pytest
from pymonet.immutable_list import ImmutableList

def test_map_with_non_empty_list():
    lst = ImmutableList.of(1, 2, 3)
    mapped_lst = lst.map(lambda x: x * 2)
    assert mapped_lst.head == 2
    assert mapped_lst.tail.head == 4
    assert mapped_lst.tail.tail.head == 6

def test_map_with_empty_list():
    empty_lst = ImmutableList.empty()
    mapped_lst = empty_lst.map(lambda x: x * 2 if x is not None else 0)
    assert mapped_lst.head == 0
    assert mapped_lst.tail is None

def test_map_with_single_element_list():
    single_element_lst = ImmutableList.of(1)
    mapped_lst = single_element_lst.map(lambda x: x * 2)
    assert mapped_lst.head == 2
    assert mapped_lst.tail is None
