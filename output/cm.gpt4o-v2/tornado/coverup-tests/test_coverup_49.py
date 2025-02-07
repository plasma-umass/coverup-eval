# file: tornado/queues.py:274-290
# asked: {"lines": [274, 286, 287, 288, 289, 290], "branches": [[286, 287], [286, 288], [289, 0], [289, 290]]}
# gained: {"lines": [274], "branches": []}

import pytest
from tornado.queues import Queue
from tornado.locks import Event

@pytest.mark.asyncio
async def test_task_done():
    q = Queue(maxsize=2)
    
    # Test normal task_done call
    await q.put(1)
    await q.get()
    q.task_done()
    assert q._unfinished_tasks == 0
    assert q._finished.is_set()

    # Test task_done call with no unfinished tasks
    with pytest.raises(ValueError, match="task_done() called too many times"):
        q.task_done()

    # Test task_done call with multiple unfinished tasks
    await q.put(1)
    await q.put(2)
    await q.get()
    await q.get()
    q.task_done()
    assert q._unfinished_tasks == 1
    assert not q._finished.is_set()
    q.task_done()
    assert q._unfinished_tasks == 0
    assert q._finished.is_set()
