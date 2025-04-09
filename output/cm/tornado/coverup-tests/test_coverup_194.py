# file tornado/locks.py:162-201
# lines [162, 163]
# branches []

import pytest
from tornado.locks import Event
from tornado import gen
from tornado.ioloop import IOLoop

@pytest.mark.gen_test
async def test_event_set_and_clear():
    event = Event()

    @gen.coroutine
    def waiter():
        yield event.wait()
        event.clear()  # This line is to ensure that clear() is called
        assert not event.is_set()
        yield event.wait()

    @gen.coroutine
    def setter():
        event.set()
        assert event.is_set()

    yield [waiter(), setter()]
