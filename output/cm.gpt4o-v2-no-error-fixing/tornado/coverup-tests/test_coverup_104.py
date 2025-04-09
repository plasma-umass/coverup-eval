# file: tornado/locks.py:202-204
# asked: {"lines": [202, 203, 204], "branches": []}
# gained: {"lines": [202], "branches": []}

import pytest
from tornado.locks import Event

@pytest.mark.asyncio
async def test_event_initialization():
    event = Event()
    assert not event.is_set()
    assert len(event._waiters) == 0
