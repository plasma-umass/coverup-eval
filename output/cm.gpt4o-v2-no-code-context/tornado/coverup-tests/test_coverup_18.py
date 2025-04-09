# file: tornado/queues.py:336-346
# asked: {"lines": [336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346], "branches": [[338, 339], [338, 340], [340, 341], [340, 342], [342, 343], [342, 344], [344, 345], [344, 346]]}
# gained: {"lines": [336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346], "branches": [[338, 339], [338, 340], [340, 341], [340, 342], [342, 343], [342, 344], [344, 345], [344, 346]]}

import pytest
from tornado.queues import Queue

@pytest.fixture
def queue():
    return Queue(maxsize=10)

def test_format_with_maxsize(queue):
    assert queue._format() == "maxsize=10"

def test_format_with_queue(queue):
    queue._queue = [1, 2, 3]
    assert "queue=[1, 2, 3]" in queue._format()

def test_format_with_getters(queue):
    queue._getters.append(None)
    assert "getters[1]" in queue._format()

def test_format_with_putters(queue):
    queue._putters.append(None)
    assert "putters[1]" in queue._format()

def test_format_with_unfinished_tasks(queue):
    queue._unfinished_tasks = 5
    assert "tasks=5" in queue._format()

@pytest.fixture(autouse=True)
def cleanup(queue):
    yield
    queue._queue = []
    queue._getters.clear()
    queue._putters.clear()
    queue._unfinished_tasks = 0
