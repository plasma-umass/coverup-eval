# file: pymonet/monad_try.py:66-77
# asked: {"lines": [66, 75, 76, 77], "branches": [[75, 76], [75, 77]]}
# gained: {"lines": [66, 75, 76, 77], "branches": [[75, 76], [75, 77]]}

import pytest
from pymonet.monad_try import Try

class TestTry:
    def test_on_success_called_when_success(self):
        # Arrange
        success_value = 42
        success_callback_called = False

        def success_callback(value):
            nonlocal success_callback_called
            success_callback_called = True
            assert value == success_value

        try_instance = Try(success_value, is_success=True)

        # Act
        result = try_instance.on_success(success_callback)

        # Assert
        assert success_callback_called
        assert result is try_instance

    def test_on_success_not_called_when_failure(self):
        # Arrange
        success_callback_called = False

        def success_callback(value):
            nonlocal success_callback_called
            success_callback_called = True

        try_instance = Try(Exception("failure"), is_success=False)

        # Act
        result = try_instance.on_success(success_callback)

        # Assert
        assert not success_callback_called
        assert result is try_instance
