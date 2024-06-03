# file tornado/queues.py:322-328
# lines [322, 324, 325, 327, 328]
# branches ['324->325', '324->327', '327->exit', '327->328']

import pytest
from tornado.queues import Queue
from unittest.mock import Mock, patch
from collections import deque

@pytest.fixture
def mock_queue():
    queue = Queue()
    queue._putters = deque()
    queue._getters = deque()
    return queue

def test_consume_expired_putters(mock_queue):
    mock_future = Mock()
    mock_future.done.return_value = True
    mock_queue._putters.append((None, mock_future))
    
    mock_queue._consume_expired()
    
    assert len(mock_queue._putters) == 0

def test_consume_expired_getters(mock_queue):
    mock_future = Mock()
    mock_future.done.return_value = True
    mock_queue._getters.append(mock_future)
    
    mock_queue._consume_expired()
    
    assert len(mock_queue._getters) == 0

def test_consume_expired_mixed(mock_queue):
    mock_putter_future = Mock()
    mock_putter_future.done.return_value = True
    mock_queue._putters.append((None, mock_putter_future))
    
    mock_getter_future = Mock()
    mock_getter_future.done.return_value = True
    mock_queue._getters.append(mock_getter_future)
    
    mock_queue._consume_expired()
    
    assert len(mock_queue._putters) == 0
    assert len(mock_queue._getters) == 0
