# file: tornado/locks.py:206-210
# asked: {"lines": [206, 207, 208, 209], "branches": []}
# gained: {"lines": [206], "branches": []}

import pytest
from tornado.locks import Event

@pytest.mark.asyncio
async def test_event_repr():
    event = Event()
    assert repr(event) == "<Event clear>"
    event.set()
    assert repr(event) == "<Event set>"
    event.clear()
    assert repr(event) == "<Event clear>"
