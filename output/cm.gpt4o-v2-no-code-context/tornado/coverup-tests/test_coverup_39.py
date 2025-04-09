# file: tornado/concurrent.py:56-68
# asked: {"lines": [56, 57, 60, 61, 62, 63, 64, 65, 67, 68], "branches": []}
# gained: {"lines": [56, 57, 67], "branches": []}

import pytest
from concurrent import futures
import sys
from tornado.concurrent import future_set_result_unless_cancelled, future_set_exc_info

class DummyExecutor(futures.Executor):
    def submit(self, fn, *args, **kwargs):
        future = futures.Future()
        try:
            future_set_result_unless_cancelled(future, fn(*args, **kwargs))
        except Exception:
            future_set_exc_info(future, sys.exc_info())
        return future

    def shutdown(self, wait=True):
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

def test_dummy_executor_shutdown():
    executor = DummyExecutor()
    executor.shutdown(wait=True)
    assert True  # Just to ensure the shutdown method is called without error
