# file: tornado/queues.py:322-328
# asked: {"lines": [322, 324, 325, 327, 328], "branches": [[324, 325], [324, 327], [327, 0], [327, 328]]}
# gained: {"lines": [322, 324, 325, 327, 328], "branches": [[324, 325], [324, 327], [327, 0], [327, 328]]}

import pytest
from unittest.mock import MagicMock
from collections import deque
from tornado.queues import Queue

@pytest.fixture
def queue():
    q = Queue()
    q._putters = deque()
    q._getters = deque()
    return q

def test_consume_expired_putters(queue):
    mock_future = MagicMock()
    mock_future.done.return_value = True
    queue._putters.append((None, mock_future))
    
    queue._consume_expired()
    
    assert len(queue._putters) == 0

def test_consume_expired_getters(queue):
    mock_future = MagicMock()
    mock_future.done.return_value = True
    queue._getters.append(mock_future)
    
    queue._consume_expired()
    
    assert len(queue._getters) == 0

def test_consume_expired_no_expired_putters(queue, monkeypatch):
    mock_future = MagicMock()
    mock_future.done.return_value = False
    queue._putters.append((None, mock_future))
    
    queue._consume_expired()
    
    assert len(queue._putters) == 1

def test_consume_expired_no_expired_getters(queue, monkeypatch):
    mock_future = MagicMock()
    mock_future.done.return_value = False
    queue._getters.append(mock_future)
    
    queue._consume_expired()
    
    assert len(queue._getters) == 1
