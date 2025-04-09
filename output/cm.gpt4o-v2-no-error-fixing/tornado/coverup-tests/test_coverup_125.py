# file: tornado/queues.py:173-175
# asked: {"lines": [173, 175], "branches": []}
# gained: {"lines": [173, 175], "branches": []}

import pytest
from tornado.queues import Queue

def test_qsize():
    q = Queue()
    q._queue = [1, 2, 3]  # Directly manipulate the protected member for testing
    assert q.qsize() == 3  # Verify the qsize method returns the correct size

    q._queue = []  # Test with an empty queue
    assert q.qsize() == 0  # Verify the qsize method returns 0 for an empty queue
