# file: tornado/queues.py:173-175
# asked: {"lines": [173, 175], "branches": []}
# gained: {"lines": [173], "branches": []}

import pytest
from tornado.queues import Queue

@pytest.mark.asyncio
async def test_qsize():
    q = Queue()
    assert q.qsize() == 0  # Queue should be empty initially

    await q.put(1)
    assert q.qsize() == 1  # Queue should have one item

    await q.put(2)
    assert q.qsize() == 2  # Queue should have two items

    await q.get()
    assert q.qsize() == 1  # Queue should have one item after one get

    await q.get()
    assert q.qsize() == 0  # Queue should be empty after getting all items
