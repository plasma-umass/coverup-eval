# file tornado/queues.py:274-290
# lines [286, 287, 288, 289, 290]
# branches ['286->287', '286->288', '289->exit', '289->290']

import pytest
from tornado.queues import Queue

@pytest.fixture
def queue():
    return Queue()

def test_task_done_called_too_many_times(queue):
    with pytest.raises(ValueError) as exc_info:
        queue.task_done()
    assert "task_done() called too many times" in str(exc_info.value)
