# file: tornado/locks.py:235-259
# asked: {"lines": [235, 236, 243, 244, 245, 246, 247, 248, 249, 250, 252, 256, 257, 259], "branches": [[244, 245], [244, 247], [249, 250], [249, 252]]}
# gained: {"lines": [235, 236], "branches": []}

import pytest
import datetime
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.locks import Event
from tornado.util import TimeoutError

@pytest.mark.gen_test
async def test_event_wait_no_timeout():
    event = Event()
    result = []

    async def waiter():
        await event.wait()
        result.append("done")

    async def setter():
        event.set()

    await gen.multi([waiter(), setter()])
    assert result == ["done"]

@pytest.mark.gen_test
async def test_event_wait_with_timeout():
    event = Event()
    result = []

    async def waiter():
        try:
            await event.wait(timeout=0.1)
        except TimeoutError:
            result.append("timeout")

    await waiter()
    assert result == ["timeout"]

@pytest.mark.gen_test
async def test_event_wait_with_timeout_then_set():
    event = Event()
    result = []

    async def waiter():
        try:
            await event.wait(timeout=0.1)
        except TimeoutError:
            result.append("timeout")
        await event.wait()
        result.append("done")

    async def setter():
        await gen.sleep(0.2)
        event.set()

    await gen.multi([waiter(), setter()])
    assert result == ["timeout", "done"]

@pytest.mark.gen_test
async def test_event_wait_set_before_timeout():
    event = Event()
    result = []

    async def waiter():
        await event.wait(timeout=0.2)
        result.append("done")

    async def setter():
        await gen.sleep(0.1)
        event.set()

    await gen.multi([waiter(), setter()])
    assert result == ["done"]
