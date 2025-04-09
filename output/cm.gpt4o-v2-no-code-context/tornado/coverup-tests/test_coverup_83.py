# file: tornado/concurrent.py:173-184
# asked: {"lines": [173, 183, 184], "branches": [[183, 0], [183, 184]]}
# gained: {"lines": [173, 183, 184], "branches": [[183, 0], [183, 184]]}

import pytest
from concurrent import futures
from tornado.concurrent import future_set_result_unless_cancelled

def test_future_set_result_unless_cancelled_not_cancelled():
    future = futures.Future()
    value = 42
    future_set_result_unless_cancelled(future, value)
    assert future.result() == value

def test_future_set_result_unless_cancelled_cancelled():
    future = futures.Future()
    future.cancel()
    value = 42
    future_set_result_unless_cancelled(future, value)
    assert future.cancelled()
    with pytest.raises(futures.CancelledError):
        future.result()
