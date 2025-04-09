# file: pymonet/lazy.py:128-137
# asked: {"lines": [128, 135, 137], "branches": []}
# gained: {"lines": [128, 135, 137], "branches": []}

import pytest
from pymonet.lazy import Lazy
from pymonet.maybe import Maybe

class TestLazy:
    def test_to_maybe(self, mocker):
        # Arrange
        mock_get = mocker.patch.object(Lazy, 'get', return_value=42)
        constructor_fn = mocker.Mock()
        lazy_instance = Lazy(constructor_fn)
        
        # Act
        result = lazy_instance.to_maybe()
        
        # Assert
        mock_get.assert_called_once()
        assert isinstance(result, Maybe)
        assert result == Maybe.just(42)
