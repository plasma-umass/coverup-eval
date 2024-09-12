# file: tornado/concurrent.py:209-230
# asked: {"lines": [228, 229, 230], "branches": [[228, 229], [228, 230]]}
# gained: {"lines": [228, 229, 230], "branches": [[228, 229], [228, 230]]}

import pytest
from unittest import mock
from tornado.concurrent import future_set_exc_info

def test_future_set_exc_info_no_exception():
    future = mock.Mock()
    exc_info = (None, None, None)
    with pytest.raises(Exception, match="future_set_exc_info called with no exception"):
        future_set_exc_info(future, exc_info)

def test_future_set_exc_info_with_exception():
    future = mock.Mock()
    exc_info = (Exception, Exception("test exception"), None)
    with mock.patch('tornado.concurrent.future_set_exception_unless_cancelled') as mock_set_exception:
        future_set_exc_info(future, exc_info)
        mock_set_exception.assert_called_once_with(future, exc_info[1])

def test_future_set_exc_info_future_cancelled():
    future = mock.Mock()
    future.cancelled.return_value = True
    exc_info = (Exception, Exception("test exception"), None)
    with mock.patch('tornado.concurrent.future_set_exception_unless_cancelled') as mock_set_exception:
        future_set_exc_info(future, exc_info)
        mock_set_exception.assert_called_once_with(future, exc_info[1])
