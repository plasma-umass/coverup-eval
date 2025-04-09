# file: pymonet/immutable_list.py:132-150
# asked: {"lines": [132, 141, 142, 144, 145, 147, 148, 150], "branches": [[141, 142], [141, 144], [144, 145], [144, 147], [147, 148], [147, 150]]}
# gained: {"lines": [132, 141, 142, 144, 145, 147, 148, 150], "branches": [[141, 142], [141, 144], [144, 145], [144, 147], [147, 148], [147, 150]]}

import pytest
from pymonet.immutable_list import ImmutableList

def test_find_empty_list():
    lst = ImmutableList()
    assert lst.find(lambda x: x is not None) is None

def test_find_single_element_list_match():
    lst = ImmutableList(1)
    assert lst.find(lambda x: x == 1) == 1

def test_find_single_element_list_no_match():
    lst = ImmutableList(1)
    assert lst.find(lambda x: x == 2) is None

def test_find_multiple_elements_first_match():
    lst = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert lst.find(lambda x: x == 1) == 1

def test_find_multiple_elements_middle_match():
    lst = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert lst.find(lambda x: x == 2) == 2

def test_find_multiple_elements_last_match():
    lst = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert lst.find(lambda x: x == 3) == 3

def test_find_multiple_elements_no_match():
    lst = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert lst.find(lambda x: x == 4) is None
