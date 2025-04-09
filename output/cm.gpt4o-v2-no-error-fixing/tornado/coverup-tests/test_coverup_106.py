# file: tornado/queues.py:292-300
# asked: {"lines": [292, 293, 300], "branches": []}
# gained: {"lines": [292, 293], "branches": []}

import pytest
import datetime
from tornado.queues import Queue
from tornado.util import TimeoutError

@pytest.mark.asyncio
async def test_queue_join_with_timeout():
    queue = Queue()
    queue._finished = asyncio.Event()

    # Test with timeout as float
    with pytest.raises(TimeoutError):
        await queue.join(timeout=0.1)

    # Test with timeout as timedelta
    with pytest.raises(TimeoutError):
        await queue.join(timeout=datetime.timedelta(seconds=0.1))

    # Test without timeout
    queue._finished.set()
    await queue.join()

    # Clean up
    queue._finished.clear()
