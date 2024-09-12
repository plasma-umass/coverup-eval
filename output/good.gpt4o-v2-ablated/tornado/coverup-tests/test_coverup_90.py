# file: tornado/concurrent.py:52-53
# asked: {"lines": [52, 53], "branches": []}
# gained: {"lines": [52, 53], "branches": []}

import pytest
from tornado.concurrent import Future
from tornado.concurrent import is_future

def test_is_future_with_future_instance():
    future = Future()
    assert is_future(future) == True

def test_is_future_with_non_future_instance():
    non_future = "not a future"
    assert is_future(non_future) == False

def test_is_future_with_none():
    assert is_future(None) == False
