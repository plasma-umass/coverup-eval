# file tornado/queues.py:333-334
# lines [333, 334]
# branches []

import pytest
from tornado.queues import Queue

class MockQueue(Queue):
    def _format(self):
        return "mock_format"

@pytest.fixture
def mock_queue():
    return MockQueue()

def test_queue_str(mock_queue):
    assert str(mock_queue) == "<MockQueue mock_format>"
