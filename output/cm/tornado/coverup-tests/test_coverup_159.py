# file tornado/concurrent.py:52-53
# lines [52, 53]
# branches []

import pytest
from tornado.concurrent import is_future
from concurrent.futures import Future

# Assuming FUTURES is a collection of valid future types, we need to test with a valid future and a non-future object.

def test_is_future_with_future_object():
    future = Future()
    assert is_future(future) == True

def test_is_future_with_non_future_object():
    non_future = object()
    assert is_future(non_future) == False
