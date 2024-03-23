# file tornado/queues.py:292-300
# lines [292, 293, 300]
# branches []

import datetime
import pytest
from tornado.queues import Queue
from tornado.util import TimeoutError
from tornado.ioloop import IOLoop
from concurrent.futures import ThreadPoolExecutor

@pytest.mark.asyncio
async def test_queue_join_timeout():
    # Create a Queue instance
    queue = Queue()

    # Set a timeout for the join operation
    timeout_duration = 0.1
    timeout = datetime.timedelta(seconds=timeout_duration)

    # Start a background task to simulate work
    async def background_task():
        await queue.put(1)
        await queue.get()
        queue.task_done()

    IOLoop.current().spawn_callback(background_task)

    # Wait for the queue to join with a timeout
    with pytest.raises(TimeoutError):
        await queue.join(timeout)

    # Clean up: ensure the queue is empty and all tasks are done
    assert queue.qsize() == 0
    assert queue.join().done()
