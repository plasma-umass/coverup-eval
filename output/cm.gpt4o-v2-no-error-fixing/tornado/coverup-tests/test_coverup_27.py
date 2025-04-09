# file: tornado/locks.py:216-226
# asked: {"lines": [216, 221, 222, 224, 225, 226], "branches": [[221, 0], [221, 222], [224, 0], [224, 225], [225, 224], [225, 226]]}
# gained: {"lines": [216], "branches": []}

import pytest
from tornado.locks import Event
from tornado.concurrent import Future

@pytest.mark.asyncio
async def test_event_set():
    event = Event()
    
    # Create a future and add it to the event's waiters
    fut = Future()
    event._waiters.add(fut)
    
    # Ensure the event is not set initially
    assert not event.is_set()
    
    # Call set and ensure the future is resolved
    event.set()
    assert event.is_set()
    assert fut.done()
    assert fut.result() is None
    
    # Clean up
    event._waiters.clear()
    event.clear()
