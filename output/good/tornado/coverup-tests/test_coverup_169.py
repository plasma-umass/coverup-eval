# file tornado/locks.py:202-204
# lines [202, 203, 204]
# branches []

import pytest
from tornado.locks import Event
from tornado.ioloop import IOLoop
from tornado import gen
from tornado.concurrent import Future

@pytest.fixture
def event_loop():
    loop = IOLoop.current()
    yield loop
    loop.close(all_fds=True)

@pytest.mark.gen_test
def test_event_set_and_clear(event_loop):
    event = Event()

    @gen.coroutine
    def waiter():
        yield event.wait()
        return 'finished'

    # Ensure the event starts unset
    assert not event.is_set()

    # Start a waiter coroutine
    future = waiter()

    # Set the event and make sure the waiter finishes
    event.set()
    assert event.is_set()
    result = yield future
    assert result == 'finished'

    # Clear the event and ensure it's unset
    event.clear()
    assert not event.is_set()

    # Start another waiter coroutine
    future2 = waiter()

    # This time, do not set the event and ensure the waiter does not finish
    with pytest.raises(gen.TimeoutError):
        yield gen.with_timeout(IOLoop.current().time() + 0.1, future2)

    # Clean up by setting the event to allow the waiter to finish
    event.set()
    result2 = yield future2
    assert result2 == 'finished'
