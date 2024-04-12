# file pymonet/immutable_list.py:88-97
# lines [97]
# branches []

import pytest
from pymonet.immutable_list import ImmutableList

def test_unshift_increases_coverage(mocker):
    # Mock the __add__ method to ensure it is called during the test
    mocker.patch.object(ImmutableList, '__add__', return_value=ImmutableList())

    # Create an ImmutableList instance
    original_list = ImmutableList([1, 2, 3])
    new_element = 0

    # Perform the unshift operation
    new_list = original_list.unshift(new_element)

    # Assert that __add__ was called, which includes the execution of line 97
    ImmutableList.__add__.assert_called_once()

    # Clean up the mock
    mocker.stopall()
