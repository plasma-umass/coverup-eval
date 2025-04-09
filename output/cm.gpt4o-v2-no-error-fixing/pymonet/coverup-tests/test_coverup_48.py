# file: pymonet/lazy.py:128-137
# asked: {"lines": [128, 135, 137], "branches": []}
# gained: {"lines": [128, 135, 137], "branches": []}

import pytest
from pymonet.lazy import Lazy
from pymonet.maybe import Maybe

class TestLazy:
    
    def test_to_maybe(self, mocker):
        # Arrange
        lazy_instance = Lazy(lambda x: x + 1)
        mock_get = mocker.patch.object(lazy_instance, 'get', return_value=42)
        
        # Act
        result = lazy_instance.to_maybe(41)
        
        # Assert
        mock_get.assert_called_once_with(41)
        assert isinstance(result, Maybe)
        assert result == Maybe.just(42)
