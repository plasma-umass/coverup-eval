# file pymonet/lazy.py:106-115
# lines [106, 113, 115]
# branches []

import pytest
from pymonet.lazy import Lazy
from pymonet.box import Box

class TestLazy:
    def test_to_box(self, mocker):
        # Mock the get method of Lazy class
        mock_get = mocker.patch.object(Lazy, 'get', return_value=42)
        
        # Create a dummy constructor function
        def dummy_constructor_fn():
            return 42
        
        # Create an instance of Lazy with the dummy constructor function
        lazy_instance = Lazy(dummy_constructor_fn)
        
        # Call the to_box method
        result = lazy_instance.to_box()
        
        # Assert that the get method was called
        mock_get.assert_called_once()
        
        # Assert that the result is a Box containing the value returned by get
        assert isinstance(result, Box)
        assert result.value == 42
