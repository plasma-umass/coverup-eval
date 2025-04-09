# file: pymonet/lazy.py:151-160
# asked: {"lines": [151, 158, 160], "branches": []}
# gained: {"lines": [151, 158, 160], "branches": []}

import pytest
from pymonet.lazy import Lazy
from pymonet.validation import Validation

class TestLazy:
    def test_to_validation(self, mocker):
        # Mock the get method to return a specific value
        mock_value = "test_value"
        mock_get = mocker.patch.object(Lazy, 'get', return_value=mock_value)
    
        # Create a dummy constructor function
        def dummy_constructor():
            return mock_value
    
        # Create an instance of Lazy with the dummy constructor function
        lazy_instance = Lazy(dummy_constructor)
    
        # Call the to_validation method
        result = lazy_instance.to_validation()
    
        # Assert that the get method was called
        mock_get.assert_called_once()
    
        # Assert that the result is a Validation.success with the mock value
        assert isinstance(result, Validation)
        assert result.is_success()
        assert result.value == mock_value
