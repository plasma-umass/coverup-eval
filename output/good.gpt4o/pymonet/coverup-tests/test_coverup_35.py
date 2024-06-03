# file pymonet/monad_try.py:66-77
# lines [66, 75, 76, 77]
# branches ['75->76', '75->77']

import pytest
from pymonet.monad_try import Try

class TestTry:
    def test_on_success_executes_callback_on_success(self, mocker):
        # Arrange
        success_callback = mocker.Mock()
        try_instance = Try("test_value", True)

        # Act
        result = try_instance.on_success(success_callback)

        # Assert
        success_callback.assert_called_once_with("test_value")
        assert result is try_instance

    def test_on_success_does_not_execute_callback_on_failure(self, mocker):
        # Arrange
        success_callback = mocker.Mock()
        try_instance = Try("test_value", False)

        # Act
        result = try_instance.on_success(success_callback)

        # Assert
        success_callback.assert_not_called()
        assert result is try_instance
