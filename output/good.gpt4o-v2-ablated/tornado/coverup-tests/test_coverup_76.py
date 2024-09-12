# file: tornado/concurrent.py:233-237
# asked: {"lines": [233, 234, 237], "branches": []}
# gained: {"lines": [233, 234], "branches": []}

import pytest
from concurrent import futures
from tornado.concurrent import future_add_done_callback

def test_future_add_done_callback(monkeypatch):
    # Create a mock future and callback
    future = futures.Future()
    callback_called = False

    def mock_callback(fut):
        nonlocal callback_called
        callback_called = True

    # Use monkeypatch to ensure the callback is called
    monkeypatch.setattr(future, 'add_done_callback', lambda cb: cb(future))

    # Call the function under test
    future_add_done_callback(future, mock_callback)

    # Assert that the callback was called
    assert callback_called

    # Clean up
    future.cancel()

