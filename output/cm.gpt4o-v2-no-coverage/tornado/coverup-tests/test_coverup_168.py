# file: tornado/queues.py:306-307
# asked: {"lines": [306, 307], "branches": []}
# gained: {"lines": [306, 307], "branches": []}

import pytest
import collections
from tornado.queues import Queue

def test_queue_init():
    queue = Queue()
    queue._init()
    assert isinstance(queue._queue, collections.deque)
