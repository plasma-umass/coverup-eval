# file: tornado/concurrent.py:52-53
# asked: {"lines": [52, 53], "branches": []}
# gained: {"lines": [52, 53], "branches": []}

import pytest
from concurrent import futures
from tornado.concurrent import is_future

def test_is_future_with_concurrent_future():
    future = futures.Future()
    assert is_future(future) == True

def test_is_future_with_non_future():
    non_future = "not a future"
    assert is_future(non_future) == False

def test_is_future_with_tornado_future(monkeypatch):
    class MockFuture:
        pass

    monkeypatch.setattr("tornado.concurrent.FUTURES", (futures.Future, MockFuture))
    mock_future = MockFuture()
    assert is_future(mock_future) == True
