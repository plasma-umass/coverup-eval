# file: tornado/locks.py:228-233
# asked: {"lines": [228, 233], "branches": []}
# gained: {"lines": [228], "branches": []}

import pytest
from tornado.locks import Event
from tornado.ioloop import IOLoop

@pytest.mark.gen_test
async def test_event_clear():
    event = Event()
    event.set()
    assert event.is_set() is True

    event.clear()
    assert event.is_set() is False

@pytest.mark.gen_test
async def test_event_wait_after_clear():
    event = Event()
    event.set()
    assert event.is_set() is True

    event.clear()
    assert event.is_set() is False

    async def waiter():
        await event.wait()
        return True

    waiter_task = IOLoop.current().run_in_executor(None, waiter)
    with pytest.raises(TimeoutError):
        await IOLoop.current().run_in_executor(None, waiter_task, timeout=0.1)
