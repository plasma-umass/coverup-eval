# file tornado/queues.py:186-207
# lines [186, 187, 199, 200, 201, 202, 203, 204, 206, 207]
# branches []

import datetime
import pytest
from tornado.queues import Queue, QueueFull
from tornado.ioloop import IOLoop
from tornado.concurrent import Future

@pytest.fixture
def mock_ioloop(mocker):
    loop = mocker.Mock(spec=IOLoop)
    mocker.patch('tornado.ioloop.IOLoop.current', return_value=loop)
    return loop

@pytest.mark.gen_test
async def test_queue_put_with_timeout(mock_ioloop):
    q = Queue(maxsize=1)
    await q.put('first_item')  # Fill the queue to trigger the timeout on next put

    with pytest.raises(QueueFull):
        q.put_nowait('second_item')  # This should raise QueueFull

    timeout = 0.1  # seconds
    future = q.put('second_item', timeout=timeout)

    # Simulate the IOLoop's timeout mechanism
    callback_time = mock_ioloop.time() + timeout
    mock_ioloop.add_timeout.assert_called_once()
    timeout_args = mock_ioloop.add_timeout.call_args[0]
    assert timeout_args[0] == callback_time

    # Execute the timeout callback to simulate the passage of time
    timeout_callback = timeout_args[1]
    timeout_callback()

    with pytest.raises(tornado.util.TimeoutError):
        await future  # This should raise TimeoutError after the timeout

    # Clean up: make sure the queue is empty for other tests
    q.get_nowait()  # Remove 'first_item'
    assert q.empty()
