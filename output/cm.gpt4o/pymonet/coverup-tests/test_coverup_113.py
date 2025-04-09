# file pymonet/either.py:70-79
# lines [77, 79]
# branches []

import pytest
from pymonet.either import Either
from pymonet.lazy import Lazy

def test_either_to_lazy(mocker):
    # Mock the Lazy class to ensure it is being called correctly
    mock_lazy = mocker.patch('pymonet.lazy.Lazy', autospec=True)
    
    # Create a subclass of Either to instantiate it
    class Right(Either):
        def __init__(self, value):
            self.value = value
    
    # Instantiate the Either subclass with a test value
    either_instance = Right(42)
    
    # Call the to_lazy method
    lazy_instance = either_instance.to_lazy()
    
    # Assert that Lazy was called with a lambda that returns the correct value
    assert mock_lazy.call_count == 1
    assert callable(mock_lazy.call_args[0][0])
    assert mock_lazy.call_args[0][0]() == 42
