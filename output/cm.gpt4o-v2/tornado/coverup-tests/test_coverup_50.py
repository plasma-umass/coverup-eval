# file: tornado/concurrent.py:56-68
# asked: {"lines": [56, 57, 60, 61, 62, 63, 64, 65, 67, 68], "branches": []}
# gained: {"lines": [56, 57, 60, 61, 62, 63, 64, 65, 67, 68], "branches": []}

import pytest
from concurrent import futures
from tornado.concurrent import DummyExecutor, future_set_result_unless_cancelled, future_set_exc_info

def test_dummy_executor_submit_success():
    def fn_success():
        return "success"

    executor = DummyExecutor()
    future = executor.submit(fn_success)
    assert future.result() == "success"

def test_dummy_executor_submit_exception():
    def fn_exception():
        raise ValueError("error")

    executor = DummyExecutor()
    future = executor.submit(fn_exception)
    with pytest.raises(ValueError) as excinfo:
        future.result()
    assert str(excinfo.value) == "error"

def test_dummy_executor_shutdown():
    executor = DummyExecutor()
    executor.shutdown()  # This should simply pass without any effect

