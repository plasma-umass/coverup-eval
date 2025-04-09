# file: tornado/concurrent.py:173-184
# asked: {"lines": [173, 183, 184], "branches": [[183, 0], [183, 184]]}
# gained: {"lines": [173, 183, 184], "branches": [[183, 0], [183, 184]]}

import pytest
from concurrent import futures
from tornado.concurrent import Future, future_set_result_unless_cancelled

def test_future_set_result_unless_cancelled_with_futures_future():
    future = futures.Future()
    value = "test_value"
    future_set_result_unless_cancelled(future, value)
    assert future.result() == value

def test_future_set_result_unless_cancelled_with_tornado_future():
    future = Future()
    value = "test_value"
    future_set_result_unless_cancelled(future, value)
    assert future.result() == value

def test_future_set_result_unless_cancelled_with_cancelled_futures_future():
    future = futures.Future()
    future.cancel()
    value = "test_value"
    future_set_result_unless_cancelled(future, value)
    assert future.cancelled()

def test_future_set_result_unless_cancelled_with_cancelled_tornado_future():
    future = Future()
    future.cancel()
    value = "test_value"
    future_set_result_unless_cancelled(future, value)
    assert future.cancelled()
