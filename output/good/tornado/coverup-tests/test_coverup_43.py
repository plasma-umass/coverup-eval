# file tornado/queues.py:59-70
# lines [59, 62, 64, 65, 66, 68, 69, 70]
# branches ['62->exit', '62->64', '65->exit', '65->66']

import datetime
import pytest
from tornado import gen, ioloop
from tornado.concurrent import Future
from tornado.queues import Queue

@pytest.mark.asyncio
async def test_set_timeout(mocker):
    # Mock the IOLoop instance and its methods
    mock_ioloop = mocker.Mock(spec=ioloop.IOLoop)
    mocker.patch.object(ioloop.IOLoop, 'current', return_value=mock_ioloop)

    # Create a future and a queue instance
    future = Future()
    queue = Queue()

    # Use the private method _set_timeout from the queue instance
    timeout = datetime.timedelta(milliseconds=100)
    queue._set_timeout(future, timeout)

    # Simulate the timeout
    on_timeout = mock_ioloop.add_timeout.call_args[0][1]
    on_timeout()

    # Assert that the future received a TimeoutError
    with pytest.raises(gen.TimeoutError):
        await future

    # Assert that the timeout was added and then removed
    mock_ioloop.add_timeout.assert_called_once_with(timeout, on_timeout)
    mock_ioloop.remove_timeout.assert_called_once()

    # Clean up by ensuring the future is done
    if not future.done():
        future.set_result(None)
