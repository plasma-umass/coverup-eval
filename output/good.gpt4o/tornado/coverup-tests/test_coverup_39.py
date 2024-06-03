# file tornado/locks.py:31-50
# lines [31, 32, 41, 42, 43, 45, 47, 48, 49, 50]
# branches ['48->exit', '48->49']

import pytest
from tornado.concurrent import Future
from tornado.locks import _TimeoutGarbageCollector
import collections

@pytest.fixture
def timeout_garbage_collector():
    return _TimeoutGarbageCollector()

def test_garbage_collect(timeout_garbage_collector):
    # Create a mix of completed and pending futures
    completed_future = Future()
    completed_future.set_result(None)
    pending_future = Future()

    # Add futures to the waiters deque
    timeout_garbage_collector._waiters.append(completed_future)
    timeout_garbage_collector._waiters.append(pending_future)

    # Simulate the condition where garbage collection should occur
    timeout_garbage_collector._timeouts = 101
    timeout_garbage_collector._garbage_collect()

    # Verify that only the pending future remains
    assert len(timeout_garbage_collector._waiters) == 1
    assert timeout_garbage_collector._waiters[0] is pending_future

    # Verify that the _timeouts counter has been reset
    assert timeout_garbage_collector._timeouts == 0
