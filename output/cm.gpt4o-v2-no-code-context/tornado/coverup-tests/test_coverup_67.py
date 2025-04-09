# file: tornado/queues.py:349-381
# asked: {"lines": [349, 350, 374, 375, 377, 378, 380, 381], "branches": []}
# gained: {"lines": [349, 350, 374, 375, 377, 378, 380, 381], "branches": []}

import pytest
from tornado.queues import PriorityQueue
import heapq

def test_priority_queue_put_get():
    q = PriorityQueue()
    q.put((1, 'medium-priority item'))
    q.put((0, 'high-priority item'))
    q.put((10, 'low-priority item'))

    assert q.get_nowait() == (0, 'high-priority item')
    assert q.get_nowait() == (1, 'medium-priority item')
    assert q.get_nowait() == (10, 'low-priority item')

def test_priority_queue_init(monkeypatch):
    q = PriorityQueue()
    assert q._queue == []

def test_priority_queue_put(monkeypatch):
    q = PriorityQueue()
    q.put((1, 'medium-priority item'))
    assert q._queue == [(1, 'medium-priority item')]

def test_priority_queue_get(monkeypatch):
    q = PriorityQueue()
    q.put((1, 'medium-priority item'))
    q.put((0, 'high-priority item'))
    q.put((10, 'low-priority item'))
    assert q._get() == (0, 'high-priority item')
    assert q._get() == (1, 'medium-priority item')
    assert q._get() == (10, 'low-priority item')
