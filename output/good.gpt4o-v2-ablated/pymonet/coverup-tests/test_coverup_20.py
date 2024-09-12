# file: pymonet/immutable_list.py:71-75
# asked: {"lines": [71, 72, 73, 75], "branches": [[72, 73], [72, 75]]}
# gained: {"lines": [71, 72, 73, 75], "branches": [[72, 73], [72, 75]]}

import pytest
from pymonet.immutable_list import ImmutableList

class TestImmutableList:
    def test_to_list_single_element(self):
        # Create an ImmutableList with a single element
        single_element_list = ImmutableList()
        single_element_list.head = 1
        single_element_list.tail = None
        
        # Verify the to_list method returns the correct list
        result = single_element_list.to_list()
        assert result == [1]

    def test_to_list_multiple_elements(self):
        # Create an ImmutableList with multiple elements
        tail_list = ImmutableList()
        tail_list.head = 2
        tail_list.tail = None
        
        head_list = ImmutableList()
        head_list.head = 1
        head_list.tail = tail_list
        
        # Verify the to_list method returns the correct list
        result = head_list.to_list()
        assert result == [1, 2]
