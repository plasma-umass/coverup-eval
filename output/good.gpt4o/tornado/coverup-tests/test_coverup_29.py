# file tornado/queues.py:153-166
# lines [153, 154, 155, 157, 158, 160, 161, 162, 163, 164, 165, 166]
# branches ['154->155', '154->157', '157->158', '157->160']

import pytest
from tornado.queues import Queue

def test_queue_init_maxsize_none():
    with pytest.raises(TypeError, match="maxsize can't be None"):
        Queue(maxsize=None)

def test_queue_init_maxsize_negative():
    with pytest.raises(ValueError, match="maxsize can't be negative"):
        Queue(maxsize=-1)

def test_queue_init_maxsize_zero():
    q = Queue(maxsize=0)
    assert q._maxsize == 0
    assert q._unfinished_tasks == 0
    assert q._finished.is_set()

def test_queue_init_maxsize_positive():
    q = Queue(maxsize=10)
    assert q._maxsize == 10
    assert q._unfinished_tasks == 0
    assert q._finished.is_set()
