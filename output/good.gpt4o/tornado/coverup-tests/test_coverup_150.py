# file tornado/queues.py:168-171
# lines [168, 169, 171]
# branches []

import pytest
from tornado.queues import Queue

def test_queue_maxsize_property():
    queue = Queue(maxsize=10)
    assert queue.maxsize == 10

    queue = Queue(maxsize=0)
    assert queue.maxsize == 0

    with pytest.raises(ValueError, match="maxsize can't be negative"):
        queue = Queue(maxsize=-1)
