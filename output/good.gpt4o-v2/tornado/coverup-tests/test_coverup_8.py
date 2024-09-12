# file: tornado/netutil.py:55-186
# asked: {"lines": [55, 57, 58, 59, 60, 61, 86, 87, 89, 90, 91, 92, 98, 99, 100, 101, 102, 103, 104, 105, 107, 108, 110, 112, 113, 114, 115, 116, 117, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138, 139, 140, 141, 150, 151, 155, 156, 157, 159, 160, 161, 162, 163, 164, 165, 166, 179, 180, 182, 183, 184, 185, 186], "branches": [[86, 87], [86, 89], [90, 91], [90, 92], [92, 98], [92, 99], [99, 100], [99, 101], [103, 107], [103, 186], [107, 108], [107, 110], [113, 125], [113, 126], [129, 130], [129, 131], [132, 133], [132, 139], [136, 138], [136, 139], [139, 140], [139, 141], [141, 150], [141, 155], [150, 151], [150, 155], [156, 157], [156, 159], [163, 179], [163, 182]]}
# gained: {"lines": [55, 57, 58, 59, 60, 61, 86, 89, 90, 91, 92, 99, 100, 101, 102, 103, 104, 105, 107, 110, 112, 113, 114, 126, 127, 132, 133, 134, 139, 140, 141, 150, 151, 155, 156, 157, 159, 160, 161, 162, 163, 164, 165, 166, 179, 180, 183, 184, 185, 186], "branches": [[86, 89], [90, 91], [90, 92], [92, 99], [99, 100], [99, 101], [103, 107], [103, 186], [107, 110], [113, 126], [132, 133], [139, 140], [139, 141], [141, 150], [141, 155], [150, 151], [156, 157], [156, 159], [163, 179]]}

import pytest
import socket
from tornado.netutil import bind_sockets

def test_bind_sockets_ipv4():
    sockets = bind_sockets(0, family=socket.AF_INET)
    assert len(sockets) > 0
    for sock in sockets:
        assert sock.family == socket.AF_INET
        sock.close()

def test_bind_sockets_ipv6():
    if not socket.has_ipv6:
        pytest.skip("IPv6 is not supported on this system")
    sockets = bind_sockets(0, family=socket.AF_INET6)
    assert len(sockets) > 0
    for sock in sockets:
        assert sock.family == socket.AF_INET6
        sock.close()

def test_bind_sockets_unspec():
    sockets = bind_sockets(0, family=socket.AF_UNSPEC)
    assert len(sockets) > 0
    for sock in sockets:
        assert sock.family in (socket.AF_INET, socket.AF_INET6)
        sock.close()

def test_bind_sockets_reuse_port():
    if not hasattr(socket, "SO_REUSEPORT"):
        pytest.skip("SO_REUSEPORT is not supported on this system")
    sockets = bind_sockets(0, reuse_port=True)
    assert len(sockets) > 0
    for sock in sockets:
        assert sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT) == 1
        sock.close()

def test_bind_sockets_no_reuse_port():
    sockets = bind_sockets(0, reuse_port=False)
    assert len(sockets) > 0
    for sock in sockets:
        assert sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT) == 0
        sock.close()

def test_bind_sockets_flags():
    sockets = bind_sockets(0, flags=socket.AI_PASSIVE | socket.AI_NUMERICHOST)
    assert len(sockets) > 0
    for sock in sockets:
        sock.close()

def test_bind_sockets_address_localhost():
    sockets = bind_sockets(0, address="localhost")
    assert len(sockets) > 0
    for sock in sockets:
        sock.close()

def test_bind_sockets_address_empty():
    sockets = bind_sockets(0, address="")
    assert len(sockets) > 0
    for sock in sockets:
        sock.close()

def test_bind_sockets_address_none():
    sockets = bind_sockets(0, address=None)
    assert len(sockets) > 0
    for sock in sockets:
        sock.close()

def test_bind_sockets_backlog():
    sockets = bind_sockets(0, backlog=50)
    assert len(sockets) > 0
    for sock in sockets:
        sock.close()

def test_bind_sockets_port_zero():
    sockets = bind_sockets(0)
    assert len(sockets) > 0
    for sock in sockets:
        assert sock.getsockname()[1] != 0
        sock.close()

def test_bind_sockets_port_nonzero():
    port = 12345
    sockets = bind_sockets(port)
    assert len(sockets) > 0
    for sock in sockets:
        assert sock.getsockname()[1] == port
        sock.close()
