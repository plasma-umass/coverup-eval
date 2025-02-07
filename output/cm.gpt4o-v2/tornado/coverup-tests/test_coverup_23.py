# file: tornado/queues.py:153-166
# asked: {"lines": [153, 154, 155, 157, 158, 160, 161, 162, 163, 164, 165, 166], "branches": [[154, 155], [154, 157], [157, 158], [157, 160]]}
# gained: {"lines": [153, 154, 155, 157, 158, 160, 161, 162, 163, 164, 165, 166], "branches": [[154, 155], [154, 157], [157, 158], [157, 160]]}

import pytest
from tornado.queues import Queue

def test_queue_init_with_none_maxsize():
    with pytest.raises(TypeError, match="maxsize can't be None"):
        Queue(None)

def test_queue_init_with_negative_maxsize():
    with pytest.raises(ValueError, match="maxsize can't be negative"):
        Queue(-1)

def test_queue_init_with_valid_maxsize():
    q = Queue(5)
    assert q._maxsize == 5
    assert q._unfinished_tasks == 0
    assert q._finished.is_set()

def test_queue_init_with_default_maxsize():
    q = Queue()
    assert q._maxsize == 0
    assert q._unfinished_tasks == 0
    assert q._finished.is_set()
