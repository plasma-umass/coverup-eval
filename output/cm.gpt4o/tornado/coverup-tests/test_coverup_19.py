# file tornado/queues.py:336-346
# lines [336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346]
# branches ['338->339', '338->340', '340->341', '340->342', '342->343', '342->344', '344->345', '344->346']

import pytest
from tornado.queues import Queue

@pytest.fixture
def queue():
    q = Queue(maxsize=10)
    yield q
    # Clean up if necessary

def test_queue_format_empty(queue):
    assert queue._format() == "maxsize=10"

def test_queue_format_with_elements(queue):
    queue._queue = [1, 2, 3]
    queue._getters = [None, None]
    queue._putters = [None]
    queue._unfinished_tasks = 5
    expected_result = "maxsize=10 queue=[1, 2, 3] getters[2] putters[1] tasks=5"
    assert queue._format() == expected_result
