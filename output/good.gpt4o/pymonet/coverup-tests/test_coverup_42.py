# file pymonet/utils.py:54-56
# lines [54, 55, 56]
# branches []

import pytest
from pymonet.utils import curried_map

def test_curried_map(mocker):
    # Mock the mapper function
    mock_mapper = mocker.Mock(side_effect=lambda x: x * 2)
    
    # Test the curried_map function
    curried_function = curried_map(mock_mapper)
    result = curried_function([1, 2, 3])
    
    # Assertions to verify the postconditions
    assert result == [2, 4, 6]
    mock_mapper.assert_has_calls([mocker.call(1), mocker.call(2), mocker.call(3)])
