# file: pymonet/immutable_list.py:56-64
# asked: {"lines": [56, 57, 58, 59, 61, 62, 63], "branches": [[58, 59], [58, 61]]}
# gained: {"lines": [56, 57, 58, 59, 61, 62, 63], "branches": [[58, 59], [58, 61]]}

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_of_single_element():
    result = ImmutableList.of(1)
    assert isinstance(result, ImmutableList)
    assert result.head == 1
    assert result.tail is None

def test_immutable_list_of_multiple_elements():
    result = ImmutableList.of(1, 2, 3)
    assert isinstance(result, ImmutableList)
    assert result.head == 1
    assert isinstance(result.tail, ImmutableList)
    assert result.tail.head == 2
    assert isinstance(result.tail.tail, ImmutableList)
    assert result.tail.tail.head == 3
    assert result.tail.tail.tail is None
