# file tornado/concurrent.py:56-68
# lines [56, 57, 60, 61, 62, 63, 64, 65, 67, 68]
# branches []

import pytest
from concurrent import futures
from tornado.concurrent import future_set_result_unless_cancelled, future_set_exc_info
import sys

class DummyExecutor(futures.Executor):
    def submit(
        self, fn, *args, **kwargs
    ):
        future = futures.Future()
        try:
            future_set_result_unless_cancelled(future, fn(*args, **kwargs))
        except Exception:
            future_set_exc_info(future, sys.exc_info())
        return future

    def shutdown(self, wait: bool = True) -> None:
        pass

def test_dummy_executor_success():
    def sample_function(x, y):
        return x + y

    executor = DummyExecutor()
    future = executor.submit(sample_function, 1, 2)
    assert future.result() == 3

def test_dummy_executor_exception():
    def sample_function(x, y):
        raise ValueError("An error occurred")

    executor = DummyExecutor()
    future = executor.submit(sample_function, 1, 2)
    with pytest.raises(ValueError, match="An error occurred"):
        future.result()
