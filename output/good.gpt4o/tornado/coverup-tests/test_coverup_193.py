# file tornado/locks.py:162-201
# lines [162, 163]
# branches []

import pytest
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.locks import Event

@pytest.mark.asyncio
async def test_event():
    event = Event()

    async def waiter():
        await event.wait()
        assert event.is_set()
        event.clear()
        assert not event.is_set()
        await event.wait()
        assert event.is_set()

    async def setter():
        event.set()
        await gen.sleep(0.1)  # Ensure the waiter has time to proceed
        event.set()

    await gen.multi([waiter(), setter()])

@pytest.fixture(autouse=True)
def cleanup():
    yield
    IOLoop.current().stop()
