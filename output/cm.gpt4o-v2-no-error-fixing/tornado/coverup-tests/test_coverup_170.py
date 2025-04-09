# file: tornado/netutil.py:226-283
# asked: {"lines": [246, 247, 249, 261, 262, 264, 265, 266, 267, 270, 271, 275, 276, 278, 279, 280, 282, 283], "branches": [[261, 0], [261, 262], [262, 264], [262, 265]]}
# gained: {"lines": [246, 247, 249, 261, 262, 264, 265, 266, 267, 270, 271, 275, 276, 278, 279, 280, 282, 283], "branches": [[261, 0], [261, 262], [262, 264], [262, 265]]}

import socket
import pytest
from tornado.ioloop import IOLoop
from unittest.mock import Mock

from tornado.netutil import add_accept_handler

_DEFAULT_BACKLOG = 128

@pytest.fixture
def mock_socket():
    sock = Mock(spec=socket.socket)
    sock.accept = Mock()
    return sock

@pytest.fixture
def mock_ioloop(monkeypatch):
    ioloop = Mock(spec=IOLoop)
    monkeypatch.setattr(IOLoop, 'current', Mock(return_value=ioloop))
    return ioloop

def test_add_accept_handler_normal(mock_socket, mock_ioloop):
    callback = Mock()
    remove_handler = add_accept_handler(mock_socket, callback)
    
    assert mock_ioloop.add_handler.called
    fd, handler, events = mock_ioloop.add_handler.call_args[0]
    assert fd == mock_socket
    assert events == IOLoop.READ
    
    # Simulate an accept call
    connection = Mock()
    address = ('127.0.0.1', 12345)
    mock_socket.accept.return_value = (connection, address)
    
    handler(mock_socket, IOLoop.READ)
    
    assert callback.called_with(connection, address)
    
    # Test remove_handler
    remove_handler()
    assert mock_ioloop.remove_handler.called_with(mock_socket)

def test_add_accept_handler_blockingioerror(mock_socket, mock_ioloop):
    callback = Mock()
    remove_handler = add_accept_handler(mock_socket, callback)
    
    fd, handler, events = mock_ioloop.add_handler.call_args[0]
    
    # Simulate BlockingIOError
    mock_socket.accept.side_effect = BlockingIOError
    
    handler(mock_socket, IOLoop.READ)
    
    assert not callback.called

def test_add_accept_handler_connectionabortederror(mock_socket, mock_ioloop):
    callback = Mock()
    remove_handler = add_accept_handler(mock_socket, callback)
    
    fd, handler, events = mock_ioloop.add_handler.call_args[0]
    
    # Simulate ConnectionAbortedError
    mock_socket.accept.side_effect = ConnectionAbortedError
    
    handler(mock_socket, IOLoop.READ)
    
    assert not callback.called

def test_add_accept_handler_removed(mock_socket, mock_ioloop):
    callback = Mock()
    remove_handler = add_accept_handler(mock_socket, callback)
    
    fd, handler, events = mock_ioloop.add_handler.call_args[0]
    
    # Simulate handler removal
    remove_handler()
    handler(mock_socket, IOLoop.READ)
    
    assert not callback.called
