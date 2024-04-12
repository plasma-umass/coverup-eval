# file tornado/queues.py:274-290
# lines [274, 286, 287, 288, 289, 290]
# branches ['286->287', '286->288', '289->exit', '289->290']

import pytest
from tornado.queues import Queue

@pytest.mark.asyncio
async def test_queue_task_done_too_many_times():
    q = Queue(maxsize=1)

    # Put an item into the queue
    await q.put(1)

    # Get the item from the queue
    item = await q.get()
    assert item == 1

    # Mark the task as done
    q.task_done()

    # Now, calling task_done again should raise ValueError
    with pytest.raises(ValueError):
        q.task_done()

    # Clean up
    del q
