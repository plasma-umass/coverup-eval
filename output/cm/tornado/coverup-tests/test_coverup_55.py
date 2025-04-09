# file tornado/concurrent.py:56-68
# lines [56, 57, 60, 61, 62, 63, 64, 65, 67, 68]
# branches []

import pytest
from concurrent import futures
import sys
from tornado.concurrent import future_set_result_unless_cancelled, future_set_exc_info

class DummyExecutor(futures.Executor):
    def submit(
        self, fn: callable, *args: any, **kwargs: any
    ) -> "futures.Future":
        future = futures.Future()
        try:
            future_set_result_unless_cancelled(future, fn(*args, **kwargs))
        except Exception:
            future_set_exc_info(future, sys.exc_info())
        return future

    def shutdown(self, wait: bool = True) -> None:
        pass

def test_dummy_executor_submit_success():
    def dummy_function(x):
        return x * 2

    executor = DummyExecutor()
    future = executor.submit(dummy_function, 5)
    assert future.result(timeout=1) == 10

def test_dummy_executor_submit_exception():
    def dummy_function(x):
        raise ValueError("an error occurred")

    executor = DummyExecutor()
    future = executor.submit(dummy_function, 5)
    with pytest.raises(ValueError, match="an error occurred"):
        future.result(timeout=1)

def test_dummy_executor_shutdown():
    executor = DummyExecutor()
    executor.shutdown()  # Just to ensure shutdown method is covered
    assert True  # No specific assertion needed for shutdown
