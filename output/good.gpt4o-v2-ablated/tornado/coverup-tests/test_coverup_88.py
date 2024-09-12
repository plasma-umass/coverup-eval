# file: tornado/locks.py:202-204
# asked: {"lines": [202, 203, 204], "branches": []}
# gained: {"lines": [202, 203, 204], "branches": []}

import pytest
from tornado.concurrent import Future
from tornado.locks import Event

@pytest.fixture
def event():
    return Event()

def test_event_initial_state(event):
    assert not event._value
    assert isinstance(event._waiters, set)
    assert len(event._waiters) == 0

def test_event_set(event):
    event.set()
    assert event._value
    assert all(future.done() for future in event._waiters)

def test_event_clear(event):
    event.set()
    event.clear()
    assert not event._value

@pytest.mark.asyncio
async def test_event_wait(event):
    future = event.wait()
    assert isinstance(future, Future)
    assert not future.done()
    event.set()
    await future
    assert future.done()

@pytest.mark.asyncio
async def test_event_wait_with_set(event):
    event.set()
    future = event.wait()
    assert future.done()

def test_event_is_set(event):
    assert not event.is_set()
    event.set()
    assert event.is_set()

def test_event_set_multiple_times(event):
    event.set()
    event.set()
    assert event._value

def test_event_clear_without_set(event):
    event.clear()
    assert not event._value
