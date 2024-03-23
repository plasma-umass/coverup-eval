# file tornado/queues.py:330-331
# lines [330, 331]
# branches []

import pytest
from tornado.queues import Queue

@pytest.fixture
def queue():
    return Queue()

def test_queue_repr(queue):
    repr_string = repr(queue)
    assert type(queue).__name__ in repr_string
    assert hex(id(queue)) in repr_string
    assert 'maxsize=' in repr_string or 'unfinished_tasks=' in repr_string
