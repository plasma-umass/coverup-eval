# file: tornado/locks.py:31-50
# asked: {"lines": [47, 48, 49, 50], "branches": [[48, 0], [48, 49]]}
# gained: {"lines": [47, 48, 49, 50], "branches": [[48, 0], [48, 49]]}

import pytest
from unittest.mock import Mock
from collections import deque

from tornado.locks import _TimeoutGarbageCollector

@pytest.fixture
def garbage_collector():
    return _TimeoutGarbageCollector()

def test_init(garbage_collector):
    assert isinstance(garbage_collector._waiters, deque)
    assert garbage_collector._timeouts == 0

def test_garbage_collect_no_timeouts(garbage_collector):
    garbage_collector._garbage_collect()
    assert garbage_collector._timeouts == 1

def test_garbage_collect_with_timeouts(garbage_collector, monkeypatch):
    garbage_collector._timeouts = 100
    mock_waiter = Mock()
    mock_waiter.done.return_value = False
    garbage_collector._waiters.append(mock_waiter)
    
    garbage_collector._garbage_collect()
    
    assert garbage_collector._timeouts == 0
    assert len(garbage_collector._waiters) == 1
    assert garbage_collector._waiters[0] == mock_waiter

def test_garbage_collect_removes_done_waiters(garbage_collector, monkeypatch):
    garbage_collector._timeouts = 100
    mock_waiter_done = Mock()
    mock_waiter_done.done.return_value = True
    mock_waiter_not_done = Mock()
    mock_waiter_not_done.done.return_value = False
    garbage_collector._waiters.extend([mock_waiter_done, mock_waiter_not_done])
    
    garbage_collector._garbage_collect()
    
    assert garbage_collector._timeouts == 0
    assert len(garbage_collector._waiters) == 1
    assert garbage_collector._waiters[0] == mock_waiter_not_done
