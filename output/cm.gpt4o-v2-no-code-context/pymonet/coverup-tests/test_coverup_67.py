# file: pymonet/lazy.py:117-126
# asked: {"lines": [117, 124, 126], "branches": []}
# gained: {"lines": [117, 124, 126], "branches": []}

import pytest
from pymonet.lazy import Lazy
from pymonet.either import Right

class TestLazy:
    def test_to_either(self, mocker):
        # Mock the get method to control its output
        mock_get = mocker.patch.object(Lazy, 'get', return_value=42)
        
        # Create an instance of Lazy
        lazy_instance = Lazy(lambda x: x + 1)
        
        # Call to_either and verify the result
        result = lazy_instance.to_either(41)
        
        # Assert that the result is a Right monad with the expected value
        assert isinstance(result, Right)
        assert result.value == 42
        
        # Verify that the get method was called with the correct arguments
        mock_get.assert_called_once_with(41)
