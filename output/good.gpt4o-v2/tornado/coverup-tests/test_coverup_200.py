# file: tornado/netutil.py:226-283
# asked: {"lines": [246, 247, 249, 261, 262, 264, 265, 266, 267, 270, 271, 275, 276, 278, 279, 280, 282, 283], "branches": [[261, 0], [261, 262], [262, 264], [262, 265]]}
# gained: {"lines": [246, 247, 249, 261, 262, 265, 266, 267, 270, 276, 278, 279, 280, 282, 283], "branches": [[261, 262], [262, 265]]}

import socket
import pytest
from tornado.ioloop import IOLoop
from tornado.netutil import add_accept_handler, _DEFAULT_BACKLOG

@pytest.fixture
def setup_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('localhost', 0))
    sock.listen(_DEFAULT_BACKLOG)
    sock.setblocking(False)
    yield sock
    sock.close()

def test_add_accept_handler(setup_socket):
    sock = setup_socket
    io_loop = IOLoop.current()
    callback_called = []

    def callback(connection, address):
        callback_called.append(True)
        connection.close()

    remove_handler = add_accept_handler(sock, callback)
    assert callable(remove_handler)

    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(sock.getsockname())
    io_loop.add_callback(io_loop.stop)
    io_loop.start()

    assert callback_called
    remove_handler()
    assert not io_loop.remove_handler(sock)

def test_accept_handler_blockingioerror(mocker, setup_socket):
    sock = setup_socket
    io_loop = IOLoop.current()
    mocker.patch('socket.socket.accept', side_effect=BlockingIOError)
    callback_called = []

    def callback(connection, address):
        callback_called.append(True)

    remove_handler = add_accept_handler(sock, callback)
    assert callable(remove_handler)

    io_loop.add_callback(io_loop.stop)
    io_loop.start()

    assert not callback_called
    remove_handler()
    assert not io_loop.remove_handler(sock)

def test_accept_handler_connectionabortederror(mocker, setup_socket):
    sock = setup_socket
    io_loop = IOLoop.current()
    mocker.patch('socket.socket.accept', side_effect=ConnectionAbortedError)
    callback_called = []

    def callback(connection, address):
        callback_called.append(True)

    remove_handler = add_accept_handler(sock, callback)
    assert callable(remove_handler)

    io_loop.add_callback(io_loop.stop)
    io_loop.start()

    assert not callback_called
    remove_handler()
    assert not io_loop.remove_handler(sock)
