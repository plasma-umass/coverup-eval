# file pymonet/box.py:92-101
# lines [92, 99, 101]
# branches []

import pytest
from pymonet.box import Box
from pymonet.monad_try import Try

def test_box_to_try(mocker):
    # Mock the Try class to ensure it is called correctly
    mock_try = mocker.patch('pymonet.monad_try.Try', autospec=True)
    
    # Create a Box instance with a test value
    test_value = 42
    box = Box(test_value)
    
    # Call the to_try method
    result = box.to_try()
    
    # Assert that Try was called with the correct arguments
    mock_try.assert_called_once_with(test_value, is_success=True)
    
    # Assert that the result is the mocked Try instance
    assert result == mock_try.return_value
