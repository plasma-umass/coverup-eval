# file tornado/queues.py:274-290
# lines [274, 286, 287, 288, 289, 290]
# branches ['286->287', '286->288', '289->exit', '289->290']

import pytest
import re
from tornado.queues import Queue
from unittest.mock import Mock

@pytest.fixture
def queue():
    q = Queue()
    q._unfinished_tasks = 0
    q._finished = Mock()
    return q

def test_task_done_raises_value_error(queue):
    with pytest.raises(ValueError, match=re.escape("task_done() called too many times")):
        queue.task_done()

def test_task_done_decrements_unfinished_tasks(queue):
    queue._unfinished_tasks = 1
    queue.task_done()
    assert queue._unfinished_tasks == 0
    queue._finished.set.assert_called_once()

def test_task_done_sets_finished_event(queue):
    queue._unfinished_tasks = 1
    queue.task_done()
    assert queue._unfinished_tasks == 0
    queue._finished.set.assert_called_once()
