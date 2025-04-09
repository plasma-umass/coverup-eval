# file: tornado/locks.py:228-233
# asked: {"lines": [228, 233], "branches": []}
# gained: {"lines": [228], "branches": []}

import pytest
from tornado.locks import Event

@pytest.mark.asyncio
async def test_event_clear():
    event = Event()
    event.set()
    assert event.is_set() is True  # Ensure the event is set
    event.clear()
    assert event.is_set() is False  # Ensure the event is cleared

@pytest.mark.asyncio
async def test_event_wait_after_clear():
    event = Event()
    event.set()
    assert event.is_set() is True  # Ensure the event is set
    event.clear()
    assert event.is_set() is False  # Ensure the event is cleared

    # Ensure that wait blocks after clear
    waiter = event.wait()
    with pytest.raises(asyncio.TimeoutError):
        await asyncio.wait_for(waiter, timeout=0.1)
