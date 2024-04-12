# file tornado/queues.py:317-320
# lines [317, 318, 319, 320]
# branches []

import pytest
from tornado.queues import Queue
from unittest.mock import patch
from tornado.ioloop import IOLoop
from tornado import gen

@pytest.fixture
def io_loop():
    loop = IOLoop.current()
    yield loop
    loop.clear_current()
    loop.close(all_fds=True)

@pytest.mark.gen_test
def test_queue_put_internal(io_loop):
    q = Queue(maxsize=1)

    # Ensure the queue is empty and unfinished_tasks is 0
    assert q.qsize() == 0
    assert q._unfinished_tasks == 0

    # Use mock to replace the _put method to avoid actual put operation
    with patch.object(q, '_put') as mock_put:
        item = object()
        # Access the private method using its mangled name
        q._Queue__put_internal(item)

        # Check if _put was called with the correct item
        mock_put.assert_called_once_with(item)

        # Check if _unfinished_tasks was incremented
        assert q._unfinished_tasks == 1

        # Check if _finished was cleared
        assert not q._finished.is_set()
