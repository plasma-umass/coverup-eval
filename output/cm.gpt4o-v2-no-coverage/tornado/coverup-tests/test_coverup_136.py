# file: tornado/queues.py:292-300
# asked: {"lines": [292, 293, 300], "branches": []}
# gained: {"lines": [292, 293], "branches": []}

import pytest
import datetime
from tornado.queues import Queue
from tornado.util import TimeoutError
from unittest.mock import Mock

@pytest.mark.asyncio
async def test_queue_join_no_timeout(monkeypatch):
    queue = Queue()
    mock_wait = Mock()
    monkeypatch.setattr(queue._finished, 'wait', mock_wait)
    
    await queue.join()
    
    mock_wait.assert_called_once_with(None)

@pytest.mark.asyncio
async def test_queue_join_with_timeout(monkeypatch):
    queue = Queue()
    mock_wait = Mock()
    monkeypatch.setattr(queue._finished, 'wait', mock_wait)
    
    timeout = 5.0
    await queue.join(timeout=timeout)
    
    mock_wait.assert_called_once_with(timeout)

@pytest.mark.asyncio
async def test_queue_join_with_timedelta_timeout(monkeypatch):
    queue = Queue()
    mock_wait = Mock()
    monkeypatch.setattr(queue._finished, 'wait', mock_wait)
    
    timeout = datetime.timedelta(seconds=5)
    await queue.join(timeout=timeout)
    
    mock_wait.assert_called_once_with(timeout)

@pytest.mark.asyncio
async def test_queue_join_timeout_error(monkeypatch):
    queue = Queue()
    mock_wait = Mock(side_effect=TimeoutError)
    monkeypatch.setattr(queue._finished, 'wait', mock_wait)
    
    with pytest.raises(TimeoutError):
        await queue.join(timeout=1)
    
    mock_wait.assert_called_once_with(1)
