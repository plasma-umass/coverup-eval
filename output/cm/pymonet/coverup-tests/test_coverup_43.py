# file pymonet/monad_try.py:79-90
# lines [79, 88, 89, 90]
# branches ['88->89', '88->90']

import pytest
from pymonet.monad_try import Try

class FailureTry(Try):
    def __init__(self, value):
        self.is_success = False
        self.value = value

class SuccessTry(Try):
    def __init__(self, value):
        self.is_success = True
        self.value = value

def test_try_on_fail_executes_callback_on_failure():
    def fail_callback(value):
        assert value == "error"
        callback_results.append(value)

    callback_results = []
    failed_try = FailureTry("error")
    failed_try.on_fail(fail_callback)

    assert len(callback_results) == 1
    assert callback_results[0] == "error"

def test_try_on_fail_does_not_execute_callback_on_success():
    def fail_callback(value):
        callback_results.append(value)

    callback_results = []
    successful_try = SuccessTry("success")
    successful_try.on_fail(fail_callback)

    assert len(callback_results) == 0
