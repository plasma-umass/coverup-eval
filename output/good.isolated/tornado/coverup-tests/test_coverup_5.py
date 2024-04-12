# file tornado/locks.py:415-441
# lines [415, 416, 423, 424, 425, 426, 428, 429, 431, 432, 433, 434, 436, 437, 438, 439, 441]
# branches ['424->425', '424->428', '429->431', '429->441', '432->433', '432->434']

import datetime
import pytest
from tornado import gen, ioloop
from tornado.locks import Semaphore
from tornado.concurrent import Future
from unittest.mock import Mock

@pytest.mark.asyncio
async def test_semaphore_acquire_with_timeout(mocker):
    # Mock the IOLoop instance and its methods
    mock_ioloop = mocker.Mock(spec=ioloop.IOLoop)
    mocker.patch.object(ioloop, 'IOLoop')
    ioloop.IOLoop.current.return_value = mock_ioloop

    # Create a semaphore with initial value 0 (locked state)
    sem = Semaphore(0)

    # Set a timeout for the acquire method
    timeout = datetime.timedelta(seconds=1)

    # Start acquiring the semaphore with a timeout
    acquire_future = sem.acquire(timeout=timeout)

    # Simulate the timeout by calling the on_timeout callback
    on_timeout = mock_ioloop.add_timeout.call_args[0][1]
    on_timeout()

    # Check that the future was completed with a TimeoutError
    with pytest.raises(gen.TimeoutError):
        await acquire_future

    # Check that the timeout was removed from the IOLoop
    mock_ioloop.remove_timeout.assert_called_once()

    # Cleanup: ensure the semaphore doesn't hold any waiters for other tests
    sem._waiters.clear()
