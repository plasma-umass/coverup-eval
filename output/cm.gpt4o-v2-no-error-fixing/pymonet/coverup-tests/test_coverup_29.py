# file: pymonet/monad_try.py:79-90
# asked: {"lines": [79, 88, 89, 90], "branches": [[88, 89], [88, 90]]}
# gained: {"lines": [79, 88, 89, 90], "branches": [[88, 89], [88, 90]]}

import pytest
from pymonet.monad_try import Try

def test_on_fail_executes_fail_callback_when_not_success():
    # Arrange
    value = "error"
    is_success = False
    try_instance = Try(value, is_success)
    fail_callback_called = False

    def fail_callback(val):
        nonlocal fail_callback_called
        fail_callback_called = True
        assert val == value

    # Act
    result = try_instance.on_fail(fail_callback)

    # Assert
    assert fail_callback_called
    assert result == try_instance

def test_on_fail_does_not_execute_fail_callback_when_success():
    # Arrange
    value = "success"
    is_success = True
    try_instance = Try(value, is_success)
    fail_callback_called = False

    def fail_callback(val):
        nonlocal fail_callback_called
        fail_callback_called = True

    # Act
    result = try_instance.on_fail(fail_callback)

    # Assert
    assert not fail_callback_called
    assert result == try_instance
