# file tornado/concurrent.py:247-263
# lines [247, 260, 261, 263]
# branches ['260->261', '260->263']

import pytest
from unittest.mock import Mock
from concurrent.futures import Future
from tornado.concurrent import future_add_done_callback

def test_future_add_done_callback_already_done():
    mock_callback = Mock()
    future = Future()
    future.set_result('done')

    future_add_done_callback(future, mock_callback)
    mock_callback.assert_called_once_with(future)

def test_future_add_done_callback_not_done(mocker):
    mock_callback = Mock()
    future = Future()
    mocker.spy(future, 'add_done_callback')

    future_add_done_callback(future, mock_callback)
    future.set_result('done')

    assert future.add_done_callback.call_count == 1
    mock_callback.assert_called_once_with(future)
