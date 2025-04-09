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

def test_queue_str_with_elements():
    queue = Queue()
    queue._queue = [1, 2, 3]
    assert str(queue) == "<Queue maxsize=0 queue=[1, 2, 3]>"

def test_queue_str_with_getters():
    queue = Queue()
    queue._getters.append(None)
    assert str(queue) == "<Queue maxsize=0 getters[1]>"

def test_queue_str_with_putters():
    queue = Queue()
    queue._putters.append(None)
    assert str(queue) == "<Queue maxsize=0 putters[1]>"

def test_queue_str_with_unfinished_tasks():
    queue = Queue()
    queue._unfinished_tasks = 5
    assert str(queue) == "<Queue maxsize=0 tasks=5>"

def test_queue_str_with_all_attributes():
    queue = Queue()
    queue._queue = [1, 2, 3]
    queue._getters.append(None)
    queue._putters.append(None)
    queue._unfinished_tasks = 5
    expected_str = "<Queue maxsize=0 queue=[1, 2, 3] getters[1] putters[1] tasks=5>"
    assert str(queue) == expected_str
