# file pymonet/immutable_list.py:18-22
# lines [18, 19, 20, 21, 22]
# branches []

import pytest
from pymonet.immutable_list import ImmutableList

def test_immutable_list_eq():
    # Create instances of ImmutableList
    list1 = ImmutableList()
    list2 = ImmutableList()
    list3 = ImmutableList()
    
    # Manually set attributes to test equality
    list1.head = 1
    list1.tail = [2, 3]
    list1.is_empty = False
    
    list2.head = 1
    list2.tail = [2, 3]
    list2.is_empty = False
    
    list3.head = 2
    list3.tail = [3, 4]
    list3.is_empty = False
    
    # Test equality
    assert list1 == list2  # Should be True
    assert list1 != list3  # Should be True
    assert list2 != list3  # Should be True
    
    # Test equality with different type
    assert list1 != "not an ImmutableList"  # Should be True
