# file tornado/concurrent.py:173-184
# lines [173, 183, 184]
# branches ['183->exit', '183->184']

import pytest
from concurrent import futures
from tornado.concurrent import future_set_result_unless_cancelled

def test_future_set_result_unless_cancelled():
    # Test with a non-cancelled future
    future = futures.Future()
    value = 42
    future_set_result_unless_cancelled(future, value)
    assert future.result() == value

    # Test with a cancelled future
    future = futures.Future()
    future.cancel()
    value = 42
    future_set_result_unless_cancelled(future, value)
    assert future.cancelled()

    # Clean up
    del future
    del value
