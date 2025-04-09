# file: tornado/concurrent.py:247-263
# asked: {"lines": [261], "branches": [[260, 261]]}
# gained: {"lines": [261], "branches": [[260, 261]]}

import pytest
import asyncio
from tornado.concurrent import future_add_done_callback

def test_future_add_done_callback_done():
    future = asyncio.Future()
    future.set_result(None)
    callback_called = False

    def callback(fut):
        nonlocal callback_called
        callback_called = True
        assert fut is future

    future_add_done_callback(future, callback)
    assert callback_called

@pytest.mark.asyncio
async def test_future_add_done_callback_not_done():
    future = asyncio.Future()
    callback_called = False

    def callback(fut):
        nonlocal callback_called
        callback_called = True
        assert fut is future

    future_add_done_callback(future, callback)
    assert not callback_called
    future.set_result(None)
    await future
    assert callback_called
