# file: tornado/queues.py:333-334
# asked: {"lines": [333, 334], "branches": []}
# gained: {"lines": [333, 334], "branches": []}

import pytest
from tornado.queues import Queue

def test_queue_str():
    q = Queue(maxsize=2)
    q.put_nowait(1)
    q.put_nowait(2)
    expected_str = "<Queue maxsize=2 queue=deque([1, 2]) tasks=2>"
    assert str(q) == expected_str
