# file pymonet/lazy.py:117-126
# lines [117, 124, 126]
# branches []

import pytest
from pymonet.lazy import Lazy
from pymonet.either import Right

class TestLazy:
    def test_to_either(self, mocker):
        # Mock the get method to ensure it returns a predictable value
        mock_get = mocker.patch.object(Lazy, 'get', return_value=42)
        
        # Create a dummy constructor function
        def dummy_constructor():
            return 42
        
        # Create an instance of Lazy with the dummy constructor function
        lazy_instance = Lazy(dummy_constructor)
        
        # Call the to_either method and capture the result
        result = lazy_instance.to_either()
        
        # Assert that the result is a Right monad with the expected value
        assert isinstance(result, Right)
        assert result.value == 42
        
        # Ensure the get method was called with the expected arguments
        mock_get.assert_called_once_with()
