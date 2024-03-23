# file pymonet/immutable_list.py:77-86
# lines [86]
# branches []

import pytest
from pymonet.immutable_list import ImmutableList

def test_append_to_immutable_list():
    # Initial ImmutableList
    initial_list = ImmutableList([1, 2, 3])
    
    # Append a new element
    new_element = 4
    result_list = initial_list.append(new_element)
    
    # Assertions to verify postconditions
    assert isinstance(result_list, ImmutableList)
    assert result_list != initial_list  # Ensure a new ImmutableList is returned
    assert len(result_list) == len(initial_list) + 1  # Length should be increased by 1
    assert result_list.to_list()[-1] == new_element  # The last element should be the new element
    assert all(result_list.to_list()[i] == initial_list.to_list()[i] for i in range(len(initial_list)))  # Previous elements are unchanged
