# file: tornado/concurrent.py:187-206
# asked: {"lines": [187, 203, 204, 206], "branches": [[203, 204], [203, 206]]}
# gained: {"lines": [187, 203, 204, 206], "branches": [[203, 204], [203, 206]]}

import pytest
from tornado.concurrent import future_set_exception_unless_cancelled
from concurrent import futures
import asyncio
from tornado.log import app_log
from unittest.mock import patch

@pytest.fixture
def mock_future():
    return futures.Future()

@pytest.fixture
def mock_asyncio_future():
    return asyncio.Future()

def test_future_set_exception_unless_cancelled_not_cancelled(mock_future):
    exc = Exception("Test Exception")
    future_set_exception_unless_cancelled(mock_future, exc)
    assert mock_future.exception() == exc

def test_future_set_exception_unless_cancelled_cancelled(mock_future, mocker):
    exc = Exception("Test Exception")
    mock_future.cancel()
    with patch.object(app_log, 'error') as mock_log_error:
        future_set_exception_unless_cancelled(mock_future, exc)
        mock_log_error.assert_called_once_with("Exception after Future was cancelled", exc_info=exc)

@pytest.mark.asyncio
async def test_future_set_exception_unless_cancelled_asyncio_not_cancelled(mock_asyncio_future):
    exc = Exception("Test Exception")
    future_set_exception_unless_cancelled(mock_asyncio_future, exc)
    assert mock_asyncio_future.exception() == exc

@pytest.mark.asyncio
async def test_future_set_exception_unless_cancelled_asyncio_cancelled(mock_asyncio_future, mocker):
    exc = Exception("Test Exception")
    mock_asyncio_future.cancel()
    with patch.object(app_log, 'error') as mock_log_error:
        future_set_exception_unless_cancelled(mock_asyncio_future, exc)
        mock_log_error.assert_called_once_with("Exception after Future was cancelled", exc_info=exc)
