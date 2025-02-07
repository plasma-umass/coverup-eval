# file: pymonet/monad_try.py:79-90
# asked: {"lines": [79, 88, 89, 90], "branches": [[88, 89], [88, 90]]}
# gained: {"lines": [79, 88, 89, 90], "branches": [[88, 89], [88, 90]]}

import pytest
from pymonet.monad_try import Try

def test_on_fail_executes_fail_callback():
    # Arrange
    fail_callback_called = False

    def fail_callback(value):
        nonlocal fail_callback_called
        fail_callback_called = True
        assert value == "error"

    try_instance = Try("error", is_success=False)

    # Act
    result = try_instance.on_fail(fail_callback)

    # Assert
    assert fail_callback_called
    assert result == try_instance

def test_on_fail_does_not_execute_fail_callback():
    # Arrange
    fail_callback_called = False

    def fail_callback(value):
        nonlocal fail_callback_called
        fail_callback_called = True

    try_instance = Try("success", is_success=True)

    # Act
    result = try_instance.on_fail(fail_callback)

    # Assert
    assert not fail_callback_called
    assert result == try_instance
