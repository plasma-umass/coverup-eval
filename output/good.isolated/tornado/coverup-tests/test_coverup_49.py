# file tornado/locks.py:216-226
# lines [216, 221, 222, 224, 225, 226]
# branches ['221->exit', '221->222', '224->exit', '224->225', '225->224', '225->226']

import pytest
from tornado.locks import Event
from tornado.ioloop import IOLoop
from tornado import gen

@pytest.mark.gen_test
def test_event_set():
    event = Event()
    assert not event.is_set()

    @gen.coroutine
    def waiter():
        yield event.wait()
        raise gen.Return(True)

    # Start a waiter that will wait for the event to be set.
    future1 = waiter()
    IOLoop.current().add_future(future1, lambda f: f.result())

    # Set the event and make sure the waiter is notified.
    event.set()
    assert event.is_set()
    assert (yield future1)

    # Start another waiter, which should not block because the event is already set.
    future2 = waiter()
    IOLoop.current().add_future(future2, lambda f: f.result())
    assert (yield future2)

    # Clean up by stopping the IOLoop after the test
    IOLoop.current().stop()
