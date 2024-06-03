# file pymonet/box.py:81-90
# lines [88, 90]
# branches []

import pytest
from pymonet.box import Box
from pymonet.lazy import Lazy

def test_box_to_lazy(mocker):
    # Create a mock for the Lazy class in the pymonet.lazy module
    mock_lazy = mocker.patch('pymonet.lazy.Lazy', autospec=True)
    
    # Create an instance of Box with a sample value
    box = Box(42)
    
    # Call the to_lazy method
    lazy_result = box.to_lazy()
    
    # Assert that Lazy was called with a lambda function
    assert mock_lazy.call_count == 1
    assert callable(mock_lazy.call_args[0][0])
    
    # Assert that the lambda function returns the correct value
    assert mock_lazy.call_args[0][0]() == 42
