# file: tornado/queues.py:309-310
# asked: {"lines": [309, 310], "branches": []}
# gained: {"lines": [309, 310], "branches": []}

import pytest
from tornado.queues import Queue

def test_queue_get():
    q = Queue()
    q._init()
    q._queue.extend([1, 2, 3])
    
    assert q._get() == 1
    assert list(q._queue) == [2, 3]
