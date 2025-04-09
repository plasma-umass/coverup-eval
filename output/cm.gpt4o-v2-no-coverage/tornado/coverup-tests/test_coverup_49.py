# file: tornado/concurrent.py:56-68
# asked: {"lines": [56, 57, 60, 61, 62, 63, 64, 65, 67, 68], "branches": []}
# gained: {"lines": [56, 57, 60, 61, 62, 63, 64, 65, 67, 68], "branches": []}

import pytest
from concurrent import futures
from tornado.concurrent import DummyExecutor, future_set_result_unless_cancelled, future_set_exc_info

def test_dummy_executor_submit_success():
    def sample_function(x):
        return x + 1

    executor = DummyExecutor()
    future = executor.submit(sample_function, 1)
    assert future.result() == 2

def test_dummy_executor_submit_exception():
    def sample_function(x):
        raise ValueError("An error occurred")

    executor = DummyExecutor()
    future = executor.submit(sample_function, 1)
    with pytest.raises(ValueError, match="An error occurred"):
        future.result()

def test_dummy_executor_shutdown():
    executor = DummyExecutor()
    executor.shutdown()  # Should do nothing and not raise any exceptions

