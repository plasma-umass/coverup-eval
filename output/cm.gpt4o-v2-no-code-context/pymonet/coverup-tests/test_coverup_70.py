# file: pymonet/lazy.py:128-137
# asked: {"lines": [128, 135, 137], "branches": []}
# gained: {"lines": [128, 135, 137], "branches": []}

import pytest
from pymonet.lazy import Lazy
from pymonet.maybe import Maybe

class TestLazy:
    def test_to_maybe(self, mocker):
        # Mock the get method to return a specific value
        mock_value = 42
        mock_get = mocker.patch.object(Lazy, 'get', return_value=mock_value)
    
        # Create an instance of Lazy
        lazy_instance = Lazy(lambda x: x + 1)
    
        # Call the to_maybe method
        result = lazy_instance.to_maybe(41)
    
        # Assert that the get method was called with the correct arguments
        mock_get.assert_called_once_with(41)
    
        # Assert that the result is a Maybe.just containing the mock value
        assert isinstance(result, Maybe)
        assert result.get_or_else(None) == mock_value
