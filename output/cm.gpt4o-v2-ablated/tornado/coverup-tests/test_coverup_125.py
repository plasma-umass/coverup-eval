# file: tornado/concurrent.py:247-263
# asked: {"lines": [261], "branches": [[260, 261]]}
# gained: {"lines": [261], "branches": [[260, 261]]}

import pytest
from concurrent import futures
from tornado.concurrent import Future, future_add_done_callback

def test_future_add_done_callback_future_done(mocker):
    future = mocker.Mock(spec=futures.Future)
    future.done.return_value = True
    callback = mocker.Mock()

    future_add_done_callback(future, callback)

    callback.assert_called_once_with(future)

def test_future_add_done_callback_future_not_done(mocker):
    future = mocker.Mock(spec=futures.Future)
    future.done.return_value = False
    callback = mocker.Mock()

    future_add_done_callback(future, callback)

    future.add_done_callback.assert_called_once_with(callback)

def test_tornado_future_add_done_callback_future_done(mocker):
    future = mocker.Mock(spec=Future)
    future.done.return_value = True
    callback = mocker.Mock()

    future_add_done_callback(future, callback)

    callback.assert_called_once_with(future)

def test_tornado_future_add_done_callback_future_not_done(mocker):
    future = mocker.Mock(spec=Future)
    future.done.return_value = False
    callback = mocker.Mock()

    future_add_done_callback(future, callback)

    future.add_done_callback.assert_called_once_with(callback)
