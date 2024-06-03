# file pymonet/monad_try.py:79-90
# lines [79, 88, 89, 90]
# branches ['88->89', '88->90']

import pytest
from pymonet.monad_try import Try

class MockTry(Try):
    def __init__(self, is_success, value):
        self.is_success = is_success
        self.value = value

def test_on_fail_executes_fail_callback(mocker):
    fail_callback = mocker.Mock()
    try_instance = MockTry(is_success=False, value="error")

    result = try_instance.on_fail(fail_callback)

    fail_callback.assert_called_once_with("error")
    assert result is try_instance

def test_on_fail_does_not_execute_fail_callback(mocker):
    fail_callback = mocker.Mock()
    try_instance = MockTry(is_success=True, value="success")

    result = try_instance.on_fail(fail_callback)

    fail_callback.assert_not_called()
    assert result is try_instance
