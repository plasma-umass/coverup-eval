# file: pymonet/lazy.py:117-126
# asked: {"lines": [124, 126], "branches": []}
# gained: {"lines": [124, 126], "branches": []}

import pytest
from pymonet.lazy import Lazy
from pymonet.either import Right

class TestLazy:
    def test_to_either(self, mocker):
        # Arrange
        lazy_instance = Lazy(lambda x: x + 1)
        mock_get = mocker.patch.object(lazy_instance, 'get', return_value=42)
        
        # Act
        result = lazy_instance.to_either(41)
        
        # Assert
        mock_get.assert_called_once_with(41)
        assert isinstance(result, Right)
        assert result.value == 42
