# file: tornado/netutil.py:226-283
# asked: {"lines": [226, 246, 247, 249, 261, 262, 264, 265, 266, 267, 270, 271, 275, 276, 278, 279, 280, 282, 283], "branches": [[261, 0], [261, 262], [262, 264], [262, 265]]}
# gained: {"lines": [226, 246, 247, 249, 261, 262, 264, 265, 266, 267, 270, 271, 275, 278, 279, 280, 282, 283], "branches": [[261, 262], [262, 264], [262, 265]]}

import pytest
import socket
from tornado.ioloop import IOLoop
from tornado.netutil import add_accept_handler

_DEFAULT_BACKLOG = 5

@pytest.fixture
def mock_socket(mocker):
    sock = mocker.Mock(spec=socket.socket)
    sock.accept = mocker.Mock()
    return sock

@pytest.fixture
def mock_ioloop(mocker):
    ioloop = mocker.Mock(spec=IOLoop)
    mocker.patch('tornado.ioloop.IOLoop.current', return_value=ioloop)
    return ioloop

def test_add_accept_handler_normal(mock_socket, mock_ioloop, mocker):
    def callback(connection, address):
        pass

    remove_handler = add_accept_handler(mock_socket, callback)
    assert callable(remove_handler)
    mock_ioloop.add_handler.assert_called_once_with(mock_socket, mocker.ANY, IOLoop.READ)

    remove_handler()
    mock_ioloop.remove_handler.assert_called_once_with(mock_socket)

def test_add_accept_handler_blockingioerror(mock_socket, mock_ioloop):
    def callback(connection, address):
        pass

    mock_socket.accept.side_effect = BlockingIOError
    remove_handler = add_accept_handler(mock_socket, callback)
    handler = mock_ioloop.add_handler.call_args[0][1]
    handler(mock_socket, IOLoop.READ)
    mock_socket.accept.assert_called_once()
    mock_ioloop.remove_handler.assert_not_called()

def test_add_accept_handler_connectionabortederror(mock_socket, mock_ioloop):
    def callback(connection, address):
        pass

    mock_socket.accept.side_effect = [ConnectionAbortedError, BlockingIOError]
    remove_handler = add_accept_handler(mock_socket, callback)
    handler = mock_ioloop.add_handler.call_args[0][1]
    handler(mock_socket, IOLoop.READ)
    assert mock_socket.accept.call_count == 2
    mock_ioloop.remove_handler.assert_not_called()

def test_add_accept_handler_removed(mock_socket, mock_ioloop):
    def callback(connection, address):
        pass

    remove_handler = add_accept_handler(mock_socket, callback)
    handler = mock_ioloop.add_handler.call_args[0][1]
    remove_handler()
    handler(mock_socket, IOLoop.READ)
    mock_socket.accept.assert_not_called()
    mock_ioloop.remove_handler.assert_called_once_with(mock_socket)
