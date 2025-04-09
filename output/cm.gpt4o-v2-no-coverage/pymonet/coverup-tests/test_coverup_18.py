# file: pymonet/monad_try.py:66-77
# asked: {"lines": [66, 75, 76, 77], "branches": [[75, 76], [75, 77]]}
# gained: {"lines": [66, 75, 76, 77], "branches": [[75, 76], [75, 77]]}

import pytest
from pymonet.monad_try import Try

def test_on_success_with_success(monkeypatch):
    # Arrange
    value = 42
    is_success = True
    try_instance = Try(value, is_success)
    success_callback_called = False

    def success_callback(val):
        nonlocal success_callback_called
        success_callback_called = True
        assert val == value

    # Act
    result = try_instance.on_success(success_callback)

    # Assert
    assert success_callback_called
    assert result == try_instance

def test_on_success_with_failure(monkeypatch):
    # Arrange
    value = 42
    is_success = False
    try_instance = Try(value, is_success)
    success_callback_called = False

    def success_callback(val):
        nonlocal success_callback_called
        success_callback_called = True

    # Act
    result = try_instance.on_success(success_callback)

    # Assert
    assert not success_callback_called
    assert result == try_instance
