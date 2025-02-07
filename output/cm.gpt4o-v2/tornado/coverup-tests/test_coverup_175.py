# file: tornado/queues.py:330-331
# asked: {"lines": [330, 331], "branches": []}
# gained: {"lines": [330, 331], "branches": []}

import pytest
from tornado.queues import Queue

def test_queue_repr():
    q = Queue()
    repr_str = repr(q)
    assert repr_str.startswith("<Queue at 0x")
    assert repr_str.endswith(">")
    assert "Queue" in repr_str
