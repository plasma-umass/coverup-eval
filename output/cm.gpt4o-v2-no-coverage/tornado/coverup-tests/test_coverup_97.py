# file: tornado/concurrent.py:209-230
# asked: {"lines": [209, 228, 229, 230], "branches": [[228, 229], [228, 230]]}
# gained: {"lines": [209, 228, 229, 230], "branches": [[228, 229], [228, 230]]}

import pytest
import asyncio
from tornado.concurrent import future_set_exc_info
from tornado.log import app_log

def test_future_set_exc_info_with_exception():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    future = asyncio.Future()
    exc_info = (Exception, Exception("test exception"), None)
    
    future_set_exc_info(future, exc_info)
    
    assert future.exception() is exc_info[1]
    loop.close()

def test_future_set_exc_info_no_exception():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    future = asyncio.Future()
    exc_info = (None, None, None)
    
    with pytest.raises(Exception, match="future_set_exc_info called with no exception"):
        future_set_exc_info(future, exc_info)
    
    loop.close()

def test_future_set_exc_info_future_cancelled(mocker):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    future = asyncio.Future()
    future.cancel()
    exc_info = (Exception, Exception("test exception"), None)
    
    mocker.patch.object(app_log, 'error')
    
    future_set_exc_info(future, exc_info)
    
    app_log.error.assert_called_once_with('Exception after Future was cancelled', exc_info=exc_info[1])
    loop.close()
