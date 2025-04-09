# file: pymonet/lazy.py:106-115
# asked: {"lines": [106, 113, 115], "branches": []}
# gained: {"lines": [106, 113, 115], "branches": []}

import pytest
from pymonet.lazy import Lazy
from pymonet.box import Box

class TestLazy:
    def test_to_box(self, mocker):
        # Arrange
        lazy_instance = Lazy(lambda x: x + 1)
        mock_get = mocker.patch.object(lazy_instance, 'get', return_value=42)
        
        # Act
        result = lazy_instance.to_box(41)
        
        # Assert
        mock_get.assert_called_once_with(41)
        assert isinstance(result, Box)
        assert result.value == 42
