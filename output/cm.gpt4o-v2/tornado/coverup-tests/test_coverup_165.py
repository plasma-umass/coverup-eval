# file: tornado/queues.py:312-313
# asked: {"lines": [312, 313], "branches": []}
# gained: {"lines": [312], "branches": []}

import pytest
from tornado.queues import Queue

@pytest.mark.asyncio
async def test_queue_put():
    q = Queue(maxsize=2)
    q._queue = []

    item = "test_item"
    q._put(item)

    assert q._queue == [item]
