# file: tornado/queues.py:53-56
# asked: {"lines": [53, 54, 56], "branches": []}
# gained: {"lines": [53, 54, 56], "branches": []}

import pytest
from tornado.queues import QueueFull

def test_queue_full_exception():
    with pytest.raises(QueueFull):
        raise QueueFull()
