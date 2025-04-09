# file: tornado/queues.py:274-290
# asked: {"lines": [274, 286, 287, 288, 289, 290], "branches": [[286, 287], [286, 288], [289, 0], [289, 290]]}
# gained: {"lines": [274, 286, 287, 288, 289, 290], "branches": [[286, 287], [286, 288], [289, 0], [289, 290]]}

import pytest
import re
from tornado.queues import Queue
from tornado.ioloop import IOLoop

@pytest.fixture
def queue():
    return Queue()

def test_task_done_decrements_unfinished_tasks(queue):
    queue.put(1)
    queue.get_nowait()
    queue.task_done()
    assert queue._unfinished_tasks == 0

def test_task_done_raises_value_error(queue):
    with pytest.raises(ValueError, match=re.escape("task_done() called too many times")):
        queue.task_done()

def test_task_done_sets_finished_event(queue):
    queue.put(1)
    queue.get_nowait()
    queue.task_done()
    assert queue._finished.is_set()

def test_task_done_with_multiple_tasks(queue):
    queue.put(1)
    queue.put(2)
    queue.get_nowait()
    queue.task_done()
    assert queue._unfinished_tasks == 1
    queue.get_nowait()
    queue.task_done()
    assert queue._unfinished_tasks == 0
    assert queue._finished.is_set()
