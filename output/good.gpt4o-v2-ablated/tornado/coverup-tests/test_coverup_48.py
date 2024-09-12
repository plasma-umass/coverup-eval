# file: tornado/queues.py:349-381
# asked: {"lines": [349, 350, 374, 375, 377, 378, 380, 381], "branches": []}
# gained: {"lines": [349, 350, 374, 375, 377, 378, 380, 381], "branches": []}

import pytest
from tornado.queues import PriorityQueue
import heapq

@pytest.fixture
def priority_queue():
    return PriorityQueue()

def test_priority_queue_init(priority_queue):
    assert priority_queue._queue == []

def test_priority_queue_put(priority_queue):
    priority_queue._put((1, 'medium-priority item'))
    priority_queue._put((0, 'high-priority item'))
    priority_queue._put((10, 'low-priority item'))
    assert priority_queue._queue == [(0, 'high-priority item'), (1, 'medium-priority item'), (10, 'low-priority item')]

def test_priority_queue_get(priority_queue):
    priority_queue._put((1, 'medium-priority item'))
    priority_queue._put((0, 'high-priority item'))
    priority_queue._put((10, 'low-priority item'))
    assert priority_queue._get() == (0, 'high-priority item')
    assert priority_queue._get() == (1, 'medium-priority item')
    assert priority_queue._get() == (10, 'low-priority item')

def test_priority_queue_integration(priority_queue):
    priority_queue.put((1, 'medium-priority item'))
    priority_queue.put((0, 'high-priority item'))
    priority_queue.put((10, 'low-priority item'))
    assert priority_queue.get_nowait() == (0, 'high-priority item')
    assert priority_queue.get_nowait() == (1, 'medium-priority item')
    assert priority_queue.get_nowait() == (10, 'low-priority item')
