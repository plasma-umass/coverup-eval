# file: tornado/locks.py:157-159
# asked: {"lines": [157, 159], "branches": []}
# gained: {"lines": [157], "branches": []}

import pytest
from tornado.locks import Condition
from tornado.ioloop import IOLoop

@pytest.mark.gen_test
async def test_condition_notify_all():
    condition = Condition()
    
    # Create a waiter coroutine that waits on the condition
    async def waiter():
        await condition.wait()
        return "done waiting"
    
    # Start the waiter coroutine
    waiter_future = waiter()
    
    # Ensure the waiter is actually waiting
    await IOLoop.current().add_callback(lambda: None)
    
    # Notify all waiters
    condition.notify_all()
    
    # Check that the waiter has been notified
    result = await waiter_future
    assert result == "done waiting"
