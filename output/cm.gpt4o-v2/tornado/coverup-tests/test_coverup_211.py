# file: tornado/queues.py:274-290
# asked: {"lines": [286, 287, 288, 289, 290], "branches": [[286, 287], [286, 288], [289, 0], [289, 290]]}
# gained: {"lines": [286, 287, 288, 289, 290], "branches": [[286, 287], [286, 288], [289, 290]]}

import pytest
import re
from tornado.queues import Queue
from tornado.locks import Event

@pytest.fixture
def queue():
    return Queue()

def test_task_done_raises_value_error(queue):
    with pytest.raises(ValueError, match=re.escape("task_done() called too many times")):
        queue.task_done()

def test_task_done_decrements_unfinished_tasks(queue):
    queue._unfinished_tasks = 1
    queue.task_done()
    assert queue._unfinished_tasks == 0

def test_task_done_sets_finished_event(queue):
    queue._unfinished_tasks = 1
    queue._finished = Event()
    queue._finished.clear()
    queue.task_done()
    assert queue._finished.is_set()
