# file tornado/queues.py:292-300
# lines [292, 293, 300]
# branches []

import pytest
import asyncio
from tornado.queues import Queue
from tornado.util import TimeoutError
from datetime import timedelta

@pytest.mark.asyncio
async def test_queue_join_timeout(mocker):
    queue = Queue()
    
    # Mock the _finished.wait method to simulate a timeout
    mock_wait = mocker.patch.object(queue._finished, 'wait', side_effect=TimeoutError)
    
    with pytest.raises(TimeoutError):
        await queue.join(timeout=timedelta(seconds=1))
    
    mock_wait.assert_called_once_with(timedelta(seconds=1))

@pytest.mark.asyncio
async def test_queue_join_no_timeout(mocker):
    queue = Queue()
    
    # Mock the _finished.wait method to simulate no timeout
    mock_wait = mocker.patch.object(queue._finished, 'wait', return_value=asyncio.Future())
    mock_wait.return_value.set_result(None)
    
    await queue.join(timeout=None)
    
    mock_wait.assert_called_once_with(None)
