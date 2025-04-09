# file: tornado/queues.py:312-313
# asked: {"lines": [312, 313], "branches": []}
# gained: {"lines": [312, 313], "branches": []}

import pytest
from tornado.queues import Queue

@pytest.fixture
def queue():
    return Queue()

def test_put_method(queue):
    item = "test_item"
    queue._put(item)
    assert list(queue._queue)[-1] == item

def test_put_method_with_multiple_items(queue):
    items = ["item1", "item2", "item3"]
    for item in items:
        queue._put(item)
    assert list(queue._queue)[-3:] == items
