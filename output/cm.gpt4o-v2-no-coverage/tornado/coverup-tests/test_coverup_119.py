# file: tornado/queues.py:47-50
# asked: {"lines": [47, 48, 50], "branches": []}
# gained: {"lines": [47, 48, 50], "branches": []}

import pytest
from tornado.queues import QueueEmpty

def test_queue_empty_exception():
    with pytest.raises(QueueEmpty):
        raise QueueEmpty()
