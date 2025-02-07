# file: tornado/concurrent.py:209-230
# asked: {"lines": [209, 228, 229, 230], "branches": [[228, 229], [228, 230]]}
# gained: {"lines": [209, 228, 229, 230], "branches": [[228, 229], [228, 230]]}

import pytest
from tornado.concurrent import future_set_exc_info
from concurrent import futures
import types

def test_future_set_exc_info_with_exception():
    future = futures.Future()
    exc_info = (Exception, Exception("test exception"), None)
    
    future_set_exc_info(future, exc_info)
    
    assert future.exception() is exc_info[1]

def test_future_set_exc_info_no_exception():
    future = futures.Future()
    exc_info = (None, None, None)
    
    with pytest.raises(Exception, match="future_set_exc_info called with no exception"):
        future_set_exc_info(future, exc_info)
