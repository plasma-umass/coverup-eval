# file: tornado/queues.py:168-171
# asked: {"lines": [168, 169, 171], "branches": []}
# gained: {"lines": [168, 169, 171], "branches": []}

import pytest
from tornado.queues import Queue

def test_queue_maxsize_property():
    q = Queue(maxsize=10)
    assert q.maxsize == 10

    q = Queue(maxsize=0)
    assert q.maxsize == 0

    with pytest.raises(ValueError, match="maxsize can't be negative"):
        Queue(maxsize=-1)
