# file: tornado/concurrent.py:240-244
# asked: {"lines": [240, 241, 244], "branches": []}
# gained: {"lines": [240, 241], "branches": []}

import pytest
import asyncio
from tornado.concurrent import future_add_done_callback

def test_future_add_done_callback():
    future = asyncio.Future()
    callback_called = False

    def callback(fut):
        nonlocal callback_called
        callback_called = True

    future_add_done_callback(future, callback)
    future.set_result(None)

    # Run the event loop to ensure the callback is called
    asyncio.get_event_loop().run_until_complete(future)

    assert callback_called
