# file: pymonet/immutable_list.py:71-75
# asked: {"lines": [71, 72, 73, 75], "branches": [[72, 73], [72, 75]]}
# gained: {"lines": [71, 72, 73, 75], "branches": [[72, 73], [72, 75]]}

import pytest
from pymonet.immutable_list import ImmutableList

def test_to_list_single_element():
    # Create an ImmutableList with a single element
    single_element_list = ImmutableList(1, None)
    result = single_element_list.to_list()
    assert result == [1]

def test_to_list_multiple_elements():
    # Create an ImmutableList with multiple elements
    tail_list = ImmutableList(2, None)
    head_list = ImmutableList(1, tail_list)
    result = head_list.to_list()
    assert result == [1, 2]
