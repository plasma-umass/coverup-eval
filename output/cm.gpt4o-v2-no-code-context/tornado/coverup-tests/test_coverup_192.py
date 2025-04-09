# file: tornado/concurrent.py:247-263
# asked: {"lines": [261], "branches": [[260, 261]]}
# gained: {"lines": [261], "branches": [[260, 261]]}

import pytest
from concurrent import futures
from tornado.concurrent import future_add_done_callback

def test_future_add_done_callback_with_done_future():
    # Create a future that is already done
    future = futures.Future()
    future.set_result(None)
    
    # Define a callback function
    callback_called = []

    def callback(fut):
        callback_called.append(True)
        assert fut is future

    # Call the function under test
    future_add_done_callback(future, callback)

    # Assert that the callback was called
    assert callback_called == [True]

def test_future_add_done_callback_with_not_done_future(mocker):
    # Create a future that is not done
    future = futures.Future()
    
    # Define a callback function
    callback_called = []

    def callback(fut):
        callback_called.append(True)
        assert fut is future

    # Mock the add_done_callback method to call the callback immediately
    mocker.patch.object(future, 'add_done_callback', side_effect=lambda cb: cb(future))

    # Call the function under test
    future_add_done_callback(future, callback)

    # Assert that the callback was called
    assert callback_called == [True]
