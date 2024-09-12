# file: tornado/locks.py:216-226
# asked: {"lines": [216, 221, 222, 224, 225, 226], "branches": [[221, 0], [221, 222], [224, 0], [224, 225], [225, 224], [225, 226]]}
# gained: {"lines": [216], "branches": []}

import pytest
from tornado.locks import Event
from tornado.ioloop import IOLoop
from tornado import gen

@pytest.mark.gen_test
async def test_event_set():
    event = Event()

    # Ensure the event is initially not set
    assert not event.is_set()

    # Create a future to wait on the event
    waiter = IOLoop.current().run_in_executor(None, event.wait)

    # Set the event
    event.set()

    # Ensure the event is set
    assert event.is_set()

    # Ensure the waiter future is done
    await waiter

    # Clean up
    event.clear()
    assert not event.is_set()

@pytest.mark.gen_test
async def test_event_set_multiple_waiters():
    event = Event()

    # Ensure the event is initially not set
    assert not event.is_set()

    # Create multiple futures to wait on the event
    waiter1 = IOLoop.current().run_in_executor(None, event.wait)
    waiter2 = IOLoop.current().run_in_executor(None, event.wait)

    # Set the event
    event.set()

    # Ensure the event is set
    assert event.is_set()

    # Ensure all waiter futures are done
    await waiter1
    await waiter2

    # Clean up
    event.clear()
    assert not event.is_set()
