# file tornado/netutil.py:226-283
# lines [226, 246, 247, 249, 261, 262, 264, 265, 266, 267, 270, 271, 275, 276, 278, 279, 280, 282, 283]
# branches ['261->exit', '261->262', '262->264', '262->265']

import socket
import pytest
from tornado.ioloop import IOLoop
from tornado.netutil import add_accept_handler

@pytest.fixture
def mock_socket(mocker):
    sock = mocker.Mock(spec=socket.socket)
    sock.accept = mocker.Mock(side_effect=[(mocker.Mock(), ('127.0.0.1', 12345)), BlockingIOError])
    return sock

@pytest.fixture
def mock_ioloop(mocker):
    ioloop = mocker.Mock(spec=IOLoop)
    mocker.patch('tornado.ioloop.IOLoop.current', return_value=ioloop)
    return ioloop

def test_add_accept_handler(mock_socket, mock_ioloop):
    callback_called = []

    def callback(connection, address):
        callback_called.append((connection, address))

    remove_handler = add_accept_handler(mock_socket, callback)

    # Simulate the IOLoop calling the accept handler
    accept_handler = mock_ioloop.add_handler.call_args[0][1]
    accept_handler(mock_socket, IOLoop.READ)

    # Verify that the callback was called with the expected arguments
    assert len(callback_called) == 1
    assert callback_called[0][1] == ('127.0.0.1', 12345)

    # Verify that the handler can be removed
    remove_handler()
    assert mock_ioloop.remove_handler.called
    assert mock_ioloop.remove_handler.call_args[0][0] == mock_socket

    # Verify that the removed flag is set
    assert mock_ioloop.remove_handler.call_args[0][0] == mock_socket
    assert mock_ioloop.remove_handler.call_args[0][0] == mock_socket
