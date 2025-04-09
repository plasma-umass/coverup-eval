# file: tornado/queues.py:312-313
# asked: {"lines": [312, 313], "branches": []}
# gained: {"lines": [312], "branches": []}

import pytest
from tornado.queues import Queue

@pytest.mark.asyncio
async def test_queue_put():
    q = Queue()
    q._queue = []
    q._put(1)
    assert q._queue == [1]
