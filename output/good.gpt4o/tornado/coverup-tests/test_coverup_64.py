# file tornado/queues.py:349-381
# lines [349, 350, 374, 375, 377, 378, 380, 381]
# branches []

import pytest
from tornado.queues import PriorityQueue
import heapq

def test_priority_queue():
    q = PriorityQueue()
    
    # Test the _init method
    q._init()
    assert q._queue == []

    # Test the _put method
    q._put((1, 'medium-priority item'))
    q._put((0, 'high-priority item'))
    q._put((10, 'low-priority item'))
    assert q._queue == [(0, 'high-priority item'), (1, 'medium-priority item'), (10, 'low-priority item')]

    # Test the _get method
    assert q._get() == (0, 'high-priority item')
    assert q._get() == (1, 'medium-priority item')
    assert q._get() == (10, 'low-priority item')

    # Ensure the queue is empty after all gets
    assert q._queue == []
