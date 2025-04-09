# file: pymonet/monad_try.py:66-77
# asked: {"lines": [66, 75, 76, 77], "branches": [[75, 76], [75, 77]]}
# gained: {"lines": [66, 75, 76, 77], "branches": [[75, 76], [75, 77]]}

import pytest
from pymonet.monad_try import Try

def test_on_success_executes_callback():
    # Arrange
    value = 42
    is_success = True
    try_instance = Try(value, is_success)
    callback_executed = False

    def success_callback(val):
        nonlocal callback_executed
        callback_executed = True
        assert val == value

    # Act
    result = try_instance.on_success(success_callback)

    # Assert
    assert callback_executed
    assert result == try_instance

def test_on_success_does_not_execute_callback():
    # Arrange
    value = 42
    is_success = False
    try_instance = Try(value, is_success)
    callback_executed = False

    def success_callback(val):
        nonlocal callback_executed
        callback_executed = True

    # Act
    result = try_instance.on_success(success_callback)

    # Assert
    assert not callback_executed
    assert result == try_instance
