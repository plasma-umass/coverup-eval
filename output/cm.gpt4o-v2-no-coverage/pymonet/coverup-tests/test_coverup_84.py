# file: pymonet/lazy.py:117-126
# asked: {"lines": [117, 124, 126], "branches": []}
# gained: {"lines": [117, 124, 126], "branches": []}

import pytest
from pymonet.lazy import Lazy
from pymonet.either import Right

class TestLazy:
    def test_to_either(self, mocker):
        # Arrange
        constructor_fn = mocker.Mock(return_value=42)
        lazy_instance = Lazy(constructor_fn)
        mock_get = mocker.patch.object(lazy_instance, 'get', return_value=42)
        
        # Act
        result = lazy_instance.to_either()
        
        # Assert
        mock_get.assert_called_once()
        assert isinstance(result, Right)
        assert result.value == 42
