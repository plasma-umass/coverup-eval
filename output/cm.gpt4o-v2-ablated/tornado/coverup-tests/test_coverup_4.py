# file: tornado/netutil.py:226-283
# asked: {"lines": [226, 246, 247, 249, 261, 262, 264, 265, 266, 267, 270, 271, 275, 276, 278, 279, 280, 282, 283], "branches": [[261, 0], [261, 262], [262, 264], [262, 265]]}
# gained: {"lines": [226, 246, 247, 249, 261, 262, 264, 265, 266, 267, 270, 271, 275, 276, 278, 279, 280, 282, 283], "branches": [[261, 0], [261, 262], [262, 264], [262, 265]]}

import socket
import pytest
from tornado.ioloop import IOLoop
from tornado.netutil import add_accept_handler

_DEFAULT_BACKLOG = 128

@pytest.fixture
def mock_socket(mocker):
    sock = mocker.Mock(spec=socket.socket)
    sock.accept = mocker.Mock()
    return sock

@pytest.fixture
def mock_ioloop(mocker):
    io_loop = mocker.Mock(spec=IOLoop)
    mocker.patch.object(IOLoop, 'current', return_value=io_loop)
    return io_loop

def test_add_accept_handler_normal(mock_socket, mock_ioloop):
    def callback(connection, address):
        pass

    remove_handler = add_accept_handler(mock_socket, callback)
    assert callable(remove_handler)

    # Simulate an accepted connection
    connection = mock_socket
    address = ('127.0.0.1', 12345)
    mock_socket.accept.return_value = (connection, address)

    # Trigger the accept handler
    accept_handler = mock_ioloop.add_handler.call_args[0][1]
    accept_handler(mock_socket, IOLoop.READ)

    mock_socket.accept.assert_called()
    mock_ioloop.add_handler.assert_called_with(mock_socket, accept_handler, IOLoop.READ)

    # Clean up
    remove_handler()
    mock_ioloop.remove_handler.assert_called_with(mock_socket)

def test_add_accept_handler_blockingioerror(mock_socket, mock_ioloop):
    def callback(connection, address):
        pass

    remove_handler = add_accept_handler(mock_socket, callback)
    assert callable(remove_handler)

    # Simulate BlockingIOError
    mock_socket.accept.side_effect = BlockingIOError

    # Trigger the accept handler
    accept_handler = mock_ioloop.add_handler.call_args[0][1]
    accept_handler(mock_socket, IOLoop.READ)

    mock_socket.accept.assert_called()
    mock_ioloop.add_handler.assert_called_with(mock_socket, accept_handler, IOLoop.READ)

    # Clean up
    remove_handler()
    mock_ioloop.remove_handler.assert_called_with(mock_socket)

def test_add_accept_handler_connectionabortederror(mock_socket, mock_ioloop):
    def callback(connection, address):
        pass

    remove_handler = add_accept_handler(mock_socket, callback)
    assert callable(remove_handler)

    # Simulate ConnectionAbortedError
    mock_socket.accept.side_effect = ConnectionAbortedError

    # Trigger the accept handler
    accept_handler = mock_ioloop.add_handler.call_args[0][1]
    accept_handler(mock_socket, IOLoop.READ)

    mock_socket.accept.assert_called()
    mock_ioloop.add_handler.assert_called_with(mock_socket, accept_handler, IOLoop.READ)

    # Clean up
    remove_handler()
    mock_ioloop.remove_handler.assert_called_with(mock_socket)

def test_add_accept_handler_removed(mock_socket, mock_ioloop):
    def callback(connection, address):
        pass

    remove_handler = add_accept_handler(mock_socket, callback)
    assert callable(remove_handler)

    # Simulate removal
    remove_handler()

    # Trigger the accept handler
    accept_handler = mock_ioloop.add_handler.call_args[0][1]
    accept_handler(mock_socket, IOLoop.READ)

    mock_socket.accept.assert_not_called()
    mock_ioloop.add_handler.assert_called_with(mock_socket, accept_handler, IOLoop.READ)
    mock_ioloop.remove_handler.assert_called_with(mock_socket)
