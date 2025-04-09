# file: tornado/concurrent.py:240-244
# asked: {"lines": [240, 241, 244], "branches": []}
# gained: {"lines": [240, 241], "branches": []}

import pytest
from unittest.mock import Mock
from concurrent.futures import Future
from tornado.concurrent import future_add_done_callback

def test_future_add_done_callback():
    future = Future()
    callback = Mock()

    # Test that the callback is added to the future
    future_add_done_callback(future, callback)
    future.set_result(None)
    callback.assert_called_once_with(future)
