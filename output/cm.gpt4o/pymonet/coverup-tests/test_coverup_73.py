# file pymonet/lazy.py:50-54
# lines [50, 51, 52, 54]
# branches []

import pytest
from pymonet.lazy import Lazy

class TestLazy:
    def test_compute_value(self, mocker):
        # Mock the constructor function
        mock_constructor_fn = mocker.Mock(return_value=42)
        
        # Create an instance of Lazy with the mocked constructor function
        lazy_instance = Lazy(mock_constructor_fn)
        
        # Ensure the initial state is not evaluated
        assert lazy_instance.is_evaluated is False
        assert lazy_instance.value is None
        
        # Call the _compute_value method
        result = lazy_instance._compute_value(1, 2, 3)
        
        # Verify the state changes and the correct value is returned
        assert lazy_instance.is_evaluated is True
        assert lazy_instance.value == 42
        assert result == 42
        
        # Verify the constructor function was called with the correct arguments
        mock_constructor_fn.assert_called_once_with(1, 2, 3)
