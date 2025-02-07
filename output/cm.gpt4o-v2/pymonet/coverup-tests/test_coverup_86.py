# file: pymonet/lazy.py:117-126
# asked: {"lines": [117, 124, 126], "branches": []}
# gained: {"lines": [117, 124, 126], "branches": []}

import pytest
from pymonet.lazy import Lazy
from pymonet.either import Right

class TestLazy:
    def test_to_either(self, mocker):
        # Arrange
        mock_get = mocker.patch.object(Lazy, 'get', return_value='test_value')
        constructor_fn = mocker.Mock()
        lazy_instance = Lazy(constructor_fn)

        # Act
        result = lazy_instance.to_either()

        # Assert
        mock_get.assert_called_once_with()
        assert isinstance(result, Right)
        assert result.value == 'test_value'
