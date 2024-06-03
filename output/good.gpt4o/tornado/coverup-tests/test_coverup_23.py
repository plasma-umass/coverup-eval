# file tornado/locks.py:235-259
# lines [235, 236, 243, 244, 245, 246, 247, 248, 249, 250, 252, 256, 257, 259]
# branches ['244->245', '244->247', '249->250', '249->252']

import pytest
import datetime
from tornado.locks import Event
from tornado.util import TimeoutError
from tornado import gen
from tornado.concurrent import Future

@pytest.mark.gen_test
async def test_event_wait_with_timeout(mocker):
    event = Event()
    mocker.patch.object(event, '_value', False)
    mocker.patch.object(event, '_waiters', set())

    timeout = datetime.timedelta(seconds=1)
    with pytest.raises(TimeoutError):
        await event.wait(timeout)

    assert len(event._waiters) == 0

@pytest.mark.gen_test
async def test_event_wait_without_timeout(mocker):
    event = Event()
    mocker.patch.object(event, '_value', False)
    mocker.patch.object(event, '_waiters', set())

    fut = event.wait()
    assert isinstance(fut, Future)
    assert not fut.done()

    event._value = True
    event._waiters.add(fut)
    fut.set_result(None)

    await fut
    assert fut.done()
    assert len(event._waiters) == 0
