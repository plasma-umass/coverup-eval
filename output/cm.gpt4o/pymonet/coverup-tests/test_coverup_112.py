# file pymonet/immutable_list.py:77-86
# lines [86]
# branches []

import pytest
from pymonet.immutable_list import ImmutableList

def test_append_method(mocker):
    # Create a mock for the ImmutableList class
    mock_immutable_list = mocker.Mock(spec=ImmutableList)
    
    # Mock the __add__ method to return a new ImmutableList instance
    mock_immutable_list.__add__ = mocker.Mock(return_value=ImmutableList())
    
    # Call the append method
    new_element = 42
    result = ImmutableList.append(mock_immutable_list, new_element)
    
    # Assert that the __add__ method was called with the correct parameters
    mock_immutable_list.__add__.assert_called_once_with(ImmutableList(new_element))
    
    # Assert that the result is an instance of ImmutableList
    assert isinstance(result, ImmutableList)
