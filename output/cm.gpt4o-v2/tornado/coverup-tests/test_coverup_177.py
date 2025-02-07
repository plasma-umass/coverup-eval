# file: tornado/locks.py:212-214
# asked: {"lines": [212, 214], "branches": []}
# gained: {"lines": [212], "branches": []}

import pytest
from tornado.locks import Event

@pytest.mark.asyncio
async def test_event_is_set():
    event = Event()
    
    # Initially, the event should not be set
    assert not event.is_set()
    
    # Set the event and check if it is set
    event.set()
    assert event.is_set()
    
    # Clear the event and check if it is not set
    event.clear()
    assert not event.is_set()
