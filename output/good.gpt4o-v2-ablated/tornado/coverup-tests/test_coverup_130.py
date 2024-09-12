# file: tornado/queues.py:322-328
# asked: {"lines": [325, 328], "branches": [[324, 325], [327, 328]]}
# gained: {"lines": [325, 328], "branches": [[324, 325], [327, 328]]}

import pytest
from tornado.queues import Queue
from unittest.mock import Mock, MagicMock

@pytest.fixture
def queue():
    return Queue()

def test_consume_expired_putters_done(queue):
    mock_future = MagicMock()
    mock_future.done.return_value = True
    queue._putters.append((None, mock_future))
    
    queue._consume_expired()
    
    assert len(queue._putters) == 0

def test_consume_expired_putters_not_done(queue):
    mock_future = MagicMock()
    mock_future.done.return_value = False
    queue._putters.append((None, mock_future))
    
    queue._consume_expired()
    
    assert len(queue._putters) == 1

def test_consume_expired_getters_done(queue):
    mock_future = MagicMock()
    mock_future.done.return_value = True
    queue._getters.append(mock_future)
    
    queue._consume_expired()
    
    assert len(queue._getters) == 0

def test_consume_expired_getters_not_done(queue):
    mock_future = MagicMock()
    mock_future.done.return_value = False
    queue._getters.append(mock_future)
    
    queue._consume_expired()
    
    assert len(queue._getters) == 1
