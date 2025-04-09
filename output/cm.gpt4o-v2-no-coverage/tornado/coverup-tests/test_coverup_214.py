# file: tornado/netutil.py:226-283
# asked: {"lines": [276], "branches": [[261, 0]]}
# gained: {"lines": [276], "branches": []}

import socket
import pytest
from tornado.ioloop import IOLoop
from tornado.netutil import add_accept_handler, _DEFAULT_BACKLOG

@pytest.fixture
def mock_socket(monkeypatch):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 0))
    sock.listen(_DEFAULT_BACKLOG)
    sock.setblocking(False)
    yield sock
    sock.close()

@pytest.fixture
def mock_ioloop(monkeypatch):
    io_loop = IOLoop.current()
    yield io_loop
    io_loop.clear_current()
    io_loop.close(all_fds=True)

def test_add_accept_handler(mock_socket, mock_ioloop):
    connections = []

    def callback(connection, address):
        connections.append((connection, address))
        connection.close()

    remove_handler = add_accept_handler(mock_socket, callback)
    assert callable(remove_handler)

    # Simulate incoming connections
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(mock_socket.getsockname())
    client_socket.close()

    mock_ioloop.add_callback(mock_ioloop.stop)
    mock_ioloop.start()

    assert len(connections) == 1
    assert isinstance(connections[0][0], socket.socket)
    assert isinstance(connections[0][1], tuple)

    # Clean up
    remove_handler()
    mock_socket.close()
    assert mock_socket.fileno() == -1
