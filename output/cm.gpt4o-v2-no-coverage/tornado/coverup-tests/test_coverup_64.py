# file: tornado/queues.py:225-254
# asked: {"lines": [225, 226, 248, 249, 250, 251, 252, 253, 254], "branches": []}
# gained: {"lines": [225, 226], "branches": []}

import pytest
import datetime
from tornado.concurrent import Future
from tornado.queues import Queue, QueueEmpty
from unittest.mock import patch

@pytest.mark.asyncio
async def test_queue_get_no_timeout():
    queue = Queue()
    queue._getters = []
    queue._putters = []
    queue._consume_expired = lambda: None
    queue.qsize = lambda: 1
    queue._get = lambda: "item"
    
    result = await queue.get()
    assert result == "item"
    assert len(queue._getters) == 0

@pytest.mark.asyncio
async def test_queue_get_with_timeout():
    queue = Queue()
    queue._getters = []
    queue._putters = []
    queue._consume_expired = lambda: None
    queue.qsize = lambda: 0
    
    with patch.object(queue, '_set_timeout') as mock_set_timeout:
        future = queue.get(timeout=1.0)
        assert future.done() == False
        assert len(queue._getters) == 1
        mock_set_timeout.assert_called_once_with(queue._getters[0], 1.0)

@pytest.mark.asyncio
async def test_queue_get_nowait_raises_queue_empty():
    queue = Queue()
    queue._getters = []
    queue._putters = []
    queue._consume_expired = lambda: None
    queue.qsize = lambda: 0
    
    with pytest.raises(QueueEmpty):
        queue.get_nowait()

@pytest.mark.asyncio
async def test_queue_get_nowait_with_item():
    queue = Queue()
    queue._getters = []
    queue._putters = []
    queue._consume_expired = lambda: None
    queue.qsize = lambda: 1
    queue._get = lambda: "item"
    
    result = queue.get_nowait()
    assert result == "item"
