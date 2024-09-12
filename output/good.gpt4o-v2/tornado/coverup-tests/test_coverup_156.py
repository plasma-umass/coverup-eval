# file: tornado/concurrent.py:52-53
# asked: {"lines": [52, 53], "branches": []}
# gained: {"lines": [52, 53], "branches": []}

import pytest
from concurrent import futures
from tornado.concurrent import is_future

def test_is_future_with_concurrent_future():
    future = futures.Future()
    assert is_future(future) == True

def test_is_future_with_tornado_future():
    from tornado.concurrent import Future
    future = Future()
    assert is_future(future) == True

def test_is_future_with_non_future():
    non_future = "I am not a future"
    assert is_future(non_future) == False
