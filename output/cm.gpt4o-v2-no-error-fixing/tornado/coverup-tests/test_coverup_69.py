# file: tornado/concurrent.py:173-184
# asked: {"lines": [173, 183, 184], "branches": [[183, 0], [183, 184]]}
# gained: {"lines": [173], "branches": []}

import pytest
import asyncio
from tornado.concurrent import future_set_result_unless_cancelled

@pytest.mark.asyncio
async def test_future_set_result_unless_cancelled():
    future = asyncio.Future()
    value = "test_value"
    
    # Ensure the future is not cancelled and set the result
    future_set_result_unless_cancelled(future, value)
    assert future.result() == value

    # Ensure the future is cancelled and does not set the result
    future = asyncio.Future()
    future.cancel()
    future_set_result_unless_cancelled(future, value)
    assert future.cancelled()
    with pytest.raises(asyncio.CancelledError):
        future.result()
