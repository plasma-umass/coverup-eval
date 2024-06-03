# file tornado/concurrent.py:209-230
# lines [209, 228, 229, 230]
# branches ['228->229', '228->230']

import pytest
from unittest.mock import Mock
from tornado.concurrent import future_set_exc_info, future_set_exception_unless_cancelled
from concurrent import futures
import types

def test_future_set_exc_info_no_exception():
    future = futures.Future()
    exc_info = (None, None, None)
    
    with pytest.raises(Exception, match="future_set_exc_info called with no exception"):
        future_set_exc_info(future, exc_info)

def test_future_set_exc_info_with_exception(mocker):
    future = futures.Future()
    exc = ValueError("test exception")
    exc_info = (ValueError, exc, None)
    
    mock_future_set_exception_unless_cancelled = mocker.patch('tornado.concurrent.future_set_exception_unless_cancelled')
    
    future_set_exc_info(future, exc_info)
    
    mock_future_set_exception_unless_cancelled.assert_called_once_with(future, exc)
