# file tornado/queues.py:225-254
# lines [225, 226, 248, 249, 250, 251, 252, 253, 254]
# branches []

import datetime
import pytest
from tornado.queues import Queue, QueueEmpty
from tornado.ioloop import IOLoop
from tornado.concurrent import Future

@pytest.mark.asyncio
async def test_queue_get_with_timeout(mocker):
    # Mock the IOLoop time to control the timeout
    mock_time = mocker.patch('tornado.ioloop.IOLoop.time', return_value=0)
    # Mock the _set_timeout to check if it's called with the correct timeout
    mock_set_timeout = mocker.patch('tornado.queues._set_timeout')

    q = Queue()
    timeout = datetime.timedelta(seconds=1)

    # Ensure the queue is empty to trigger the timeout branch
    with pytest.raises(QueueEmpty):
        q.get_nowait()

    # Call get with a timeout
    future = q.get(timeout=timeout)

    # Check if _set_timeout was called with the correct arguments
    mock_set_timeout.assert_called_once_with(future, timeout)

    # Move the time forward to trigger the timeout
    mock_time.return_value += 1.1

    # Run the IOLoop to process the timeout
    await IOLoop.current().run_sync(lambda: future)

    # Ensure the future was not resolved since the queue is empty and timeout occurred
    assert future.done() and not future.exception() is None

    # Clean up by stopping the IOLoop
    IOLoop.current().stop()
