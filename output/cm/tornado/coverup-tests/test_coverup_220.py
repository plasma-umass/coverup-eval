# file tornado/concurrent.py:56-68
# lines [60, 61, 62, 63, 64, 65, 68]
# branches []

import pytest
from concurrent import futures
from tornado.concurrent import DummyExecutor, future_set_result_unless_cancelled
import sys

def test_dummy_executor_submit_and_shutdown():
    def dummy_function():
        return "result"

    def failing_function():
        raise ValueError("Intentional failure")

    # Test successful execution
    executor = DummyExecutor()
    future = executor.submit(dummy_function)
    assert future.result(timeout=1) == "result"

    # Test exception handling
    future = executor.submit(failing_function)
    with pytest.raises(ValueError):
        future.result(timeout=1)

    # Test shutdown method (no-op)
    executor.shutdown()
    assert True  # Just to ensure the shutdown method does not raise an exception

    # Clean up
    del executor
