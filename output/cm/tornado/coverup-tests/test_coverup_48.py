# file tornado/locks.py:31-50
# lines [31, 32, 41, 42, 43, 45, 47, 48, 49, 50]
# branches ['48->exit', '48->49']

import collections
from tornado.locks import _TimeoutGarbageCollector
from tornado.concurrent import Future
import pytest

@pytest.fixture
def gc_collector():
    return _TimeoutGarbageCollector()

@pytest.fixture
def mock_future(mocker):
    future = mocker.Mock(spec=Future)
    future.done.return_value = False
    return future

def test_timeout_garbage_collector_cleanup(gc_collector, mock_future):
    # Add mock futures to the collector's waiters
    for _ in range(101):
        gc_collector._waiters.append(mock_future)
    
    # Simulate timeouts to trigger the garbage collection
    for _ in range(101):
        gc_collector._garbage_collect()
    
    # Assert that the garbage collection has been triggered
    assert gc_collector._timeouts == 0
    # Assert that the waiters deque has been cleaned up
    assert all(not w.done() for w in gc_collector._waiters)

    # Now simulate that one future is done
    mock_future.done.return_value = True
    gc_collector._garbage_collect()  # This should not trigger cleanup yet
    assert gc_collector._timeouts == 1
    assert len(gc_collector._waiters) == 101  # No cleanup happened

    # Trigger the cleanup
    for _ in range(100):
        gc_collector._garbage_collect()
    assert gc_collector._timeouts == 0
    assert len(gc_collector._waiters) == 0  # Cleanup should have removed the done future
