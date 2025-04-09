# file: pymonet/immutable_list.py:56-64
# asked: {"lines": [56, 57, 58, 59, 61, 62, 63], "branches": [[58, 59], [58, 61]]}
# gained: {"lines": [56, 57, 58, 59, 61, 62, 63], "branches": [[58, 59], [58, 61]]}

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_of_single_element():
    lst = ImmutableList.of(1)
    assert lst.head == 1
    assert lst.tail is None

def test_immutable_list_of_multiple_elements():
    lst = ImmutableList.of(1, 2, 3)
    assert lst.head == 1
    assert lst.tail.head == 2
    assert lst.tail.tail.head == 3
    assert lst.tail.tail.tail is None
