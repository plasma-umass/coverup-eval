# file: tornado/locks.py:117-121
# asked: {"lines": [117, 118, 119, 120, 121], "branches": [[119, 120], [119, 121]]}
# gained: {"lines": [117], "branches": []}

import pytest
from tornado.locks import Condition
from tornado.ioloop import IOLoop

@pytest.mark.asyncio
async def test_condition_repr_no_waiters():
    condition = Condition()
    assert repr(condition) == "<Condition>"

@pytest.mark.asyncio
async def test_condition_repr_with_waiters():
    condition = Condition()
    
    async def waiter():
        await condition.wait()
    
    async def runner():
        # Start the waiter coroutine
        io_loop = IOLoop.current()
        io_loop.add_callback(waiter)
        await io_loop.run_in_executor(None, lambda: None)  # Yield control to let waiter start
        assert repr(condition) == "<Condition waiters[1]>"
        condition.notify()
    
    await runner()
