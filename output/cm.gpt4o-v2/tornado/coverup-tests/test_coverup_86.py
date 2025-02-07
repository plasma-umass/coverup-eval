# file: tornado/concurrent.py:187-206
# asked: {"lines": [187, 203, 204, 206], "branches": [[203, 204], [203, 206]]}
# gained: {"lines": [187], "branches": []}

import pytest
from unittest.mock import Mock, patch
from tornado.concurrent import future_set_exception_unless_cancelled
from tornado.log import app_log
import asyncio

@pytest.mark.asyncio
async def test_future_set_exception_unless_cancelled_not_cancelled():
    future = asyncio.Future()
    exc = Exception("Test exception")
    
    future_set_exception_unless_cancelled(future, exc)
    
    assert future.exception() == exc

@pytest.mark.asyncio
async def test_future_set_exception_unless_cancelled_cancelled(mocker):
    future = asyncio.Future()
    future.cancel()
    exc = Exception("Test exception")
    
    mock_log_error = mocker.patch.object(app_log, 'error')
    
    future_set_exception_unless_cancelled(future, exc)
    
    mock_log_error.assert_called_once_with("Exception after Future was cancelled", exc_info=exc)
