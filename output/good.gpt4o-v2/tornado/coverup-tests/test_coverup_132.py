# file: tornado/queues.py:168-171
# asked: {"lines": [168, 169, 171], "branches": []}
# gained: {"lines": [168, 169, 171], "branches": []}

import pytest
from tornado.queues import Queue

def test_queue_maxsize():
    q = Queue(maxsize=5)
    assert q.maxsize == 5

    q = Queue(maxsize=0)
    assert q.maxsize == 0

    q = Queue(maxsize=10)
    assert q.maxsize == 10

    with pytest.raises(TypeError):
        Queue(maxsize=None)

    with pytest.raises(ValueError):
        Queue(maxsize=-1)
