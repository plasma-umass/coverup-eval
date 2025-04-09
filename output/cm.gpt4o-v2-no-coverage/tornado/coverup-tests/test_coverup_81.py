# file: tornado/concurrent.py:173-184
# asked: {"lines": [173, 183, 184], "branches": [[183, 0], [183, 184]]}
# gained: {"lines": [173, 183, 184], "branches": [[183, 0], [183, 184]]}

import pytest
import asyncio
from concurrent import futures
from tornado.concurrent import future_set_result_unless_cancelled

@pytest.mark.asyncio
async def test_future_set_result_unless_cancelled_not_cancelled():
    future = asyncio.Future()
    future_set_result_unless_cancelled(future, "test_value")
    assert future.result() == "test_value"

@pytest.mark.asyncio
async def test_future_set_result_unless_cancelled_cancelled():
    future = asyncio.Future()
    future.cancel()
    future_set_result_unless_cancelled(future, "test_value")
    assert future.cancelled()

def test_future_set_result_unless_cancelled_concurrent_future(mocker):
    future = futures.Future()
    mocker.patch.object(future, 'set_result')
    future_set_result_unless_cancelled(future, "test_value")
    future.set_result.assert_called_once_with("test_value")

def test_future_set_result_unless_cancelled_concurrent_future_cancelled(mocker):
    future = futures.Future()
    mocker.patch.object(future, 'cancelled', return_value=True)
    mocker.patch.object(future, 'set_result')
    future_set_result_unless_cancelled(future, "test_value")
    future.set_result.assert_not_called()
