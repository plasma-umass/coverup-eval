# file: tornado/queues.py:330-331
# asked: {"lines": [330, 331], "branches": []}
# gained: {"lines": [330, 331], "branches": []}

import pytest
from tornado.queues import Queue

def test_queue_repr():
    queue = Queue()
    repr_str = repr(queue)
    assert repr_str.startswith("<Queue at ")
    assert repr_str.endswith(">")
    assert "Queue" in repr_str
    assert hex(id(queue)) in repr_str
