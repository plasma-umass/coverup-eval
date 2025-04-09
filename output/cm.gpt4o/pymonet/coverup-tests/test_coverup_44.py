# file pymonet/lazy.py:80-93
# lines [80, 89, 90, 91, 93]
# branches []

import pytest
from unittest.mock import Mock

# Assuming the Lazy class is defined in pymonet.lazy
from pymonet.lazy import Lazy

class TestLazy:
    def test_bind_executes_fn(self):
        # Mock the constructor function and the function to bind
        constructor_fn = Mock(return_value=42)
        fn = Mock()
        
        # Create a Lazy instance with the mocked constructor function
        lazy_instance = Lazy(constructor_fn)
        
        # Mock the return value of fn to be another Lazy instance
        fn.return_value = Lazy(constructor_fn)
        
        # Bind the function to the Lazy instance
        bound_lazy = lazy_instance.bind(fn)
        
        # Call the bound Lazy instance to trigger the computation
        result = bound_lazy._compute_value()
        
        # Assertions to verify the behavior
        constructor_fn.assert_called_once()
        fn.assert_called_once_with(42)
        assert result() == 42
