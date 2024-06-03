# file pymonet/box.py:59-68
# lines [66, 68]
# branches []

import pytest
from pymonet.box import Box
from pymonet.maybe import Maybe

def test_box_to_maybe(mocker):
    # Create a mock for the Maybe class
    mock_maybe = mocker.patch('pymonet.maybe.Maybe', autospec=True)
    
    # Create an instance of Box with a sample value
    box = Box(42)
    
    # Call the to_maybe method
    result = box.to_maybe()
    
    # Assert that Maybe.just was called with the correct value
    mock_maybe.just.assert_called_once_with(42)
    
    # Assert that the result is the return value of Maybe.just
    assert result == mock_maybe.just.return_value
