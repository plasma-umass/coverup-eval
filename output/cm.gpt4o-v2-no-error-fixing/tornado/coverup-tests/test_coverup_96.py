# file: tornado/queues.py:47-50
# asked: {"lines": [47, 48, 50], "branches": []}
# gained: {"lines": [47, 48, 50], "branches": []}

import pytest
from tornado.queues import QueueEmpty

def test_queue_empty_exception():
    with pytest.raises(QueueEmpty):
        raise QueueEmpty()

    assert QueueEmpty.__doc__ == "Raised by `.Queue.get_nowait` when the queue has no items."
