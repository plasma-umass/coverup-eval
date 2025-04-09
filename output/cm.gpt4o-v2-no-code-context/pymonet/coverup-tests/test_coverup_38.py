# file: pymonet/lazy.py:50-54
# asked: {"lines": [50, 51, 52, 54], "branches": []}
# gained: {"lines": [50, 51, 52, 54], "branches": []}

import pytest
from pymonet.lazy import Lazy

class TestLazy:
    def test_compute_value(self, mocker):
        # Arrange
        constructor_fn = mocker.Mock(return_value=42)
        lazy_instance = Lazy(constructor_fn)
        lazy_instance.is_evaluated = False
        lazy_instance.value = None

        # Act
        result = lazy_instance._compute_value(1, 2, 3)

        # Assert
        constructor_fn.assert_called_once_with(1, 2, 3)
        assert lazy_instance.is_evaluated is True
        assert lazy_instance.value == 42
        assert result == 42
