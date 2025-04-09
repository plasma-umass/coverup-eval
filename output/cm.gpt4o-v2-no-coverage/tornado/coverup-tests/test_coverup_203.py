# file: tornado/queues.py:333-334
# asked: {"lines": [334], "branches": []}
# gained: {"lines": [334], "branches": []}

import pytest
from tornado.queues import Queue

@pytest.fixture
def queue():
    return Queue()

def test_queue_str_empty(queue):
    assert str(queue) == "<Queue maxsize=0>"

def test_queue_str_with_maxsize():
    queue = Queue(maxsize=10)
    assert str(queue) == "<Queue maxsize=10>"

def test_queue_str_with_queue(monkeypatch):
    queue = Queue()
    monkeypatch.setattr(queue, '_queue', [1, 2, 3])
    assert str(queue) == "<Queue maxsize=0 queue=[1, 2, 3]>"

def test_queue_str_with_getters(monkeypatch):
    queue = Queue()
    monkeypatch.setattr(queue, '_getters', [1, 2])
    assert str(queue) == "<Queue maxsize=0 getters[2]>"

def test_queue_str_with_putters(monkeypatch):
    queue = Queue()
    monkeypatch.setattr(queue, '_putters', [1, 2, 3])
    assert str(queue) == "<Queue maxsize=0 putters[3]>"

def test_queue_str_with_unfinished_tasks(monkeypatch):
    queue = Queue()
    monkeypatch.setattr(queue, '_unfinished_tasks', 5)
    assert str(queue) == "<Queue maxsize=0 tasks=5>"

def test_queue_str_with_all_attributes(monkeypatch):
    queue = Queue(maxsize=10)
    monkeypatch.setattr(queue, '_queue', [1, 2, 3])
    monkeypatch.setattr(queue, '_getters', [1, 2])
    monkeypatch.setattr(queue, '_putters', [1, 2, 3])
    monkeypatch.setattr(queue, '_unfinished_tasks', 5)
    expected_str = "<Queue maxsize=10 queue=[1, 2, 3] getters[2] putters[3] tasks=5>"
    assert str(queue) == expected_str
