# file: tornado/queues.py:274-290
# asked: {"lines": [274, 286, 287, 288, 289, 290], "branches": [[286, 287], [286, 288], [289, 0], [289, 290]]}
# gained: {"lines": [274], "branches": []}

import pytest
from tornado.queues import Queue

@pytest.mark.asyncio
async def test_task_done():
    q = Queue(maxsize=2)
    
    # Test normal task_done call
    await q.put(1)
    await q.get()
    q.task_done()
    assert q._unfinished_tasks == 0
    
    # Test task_done called too many times
    with pytest.raises(ValueError, match="task_done() called too many times"):
        q.task_done()
    
    # Test task_done with multiple tasks
    await q.put(2)
    await q.put(3)
    await q.get()
    await q.get()
    q.task_done()
    assert q._unfinished_tasks == 1
    q.task_done()
    assert q._unfinished_tasks == 0
