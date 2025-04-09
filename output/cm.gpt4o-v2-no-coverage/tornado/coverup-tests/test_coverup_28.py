# file: tornado/netutil.py:55-186
# asked: {"lines": [55, 57, 58, 59, 60, 61, 86, 87, 89, 90, 91, 92, 98, 99, 100, 101, 102, 103, 104, 105, 107, 108, 110, 112, 113, 114, 115, 116, 117, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138, 139, 140, 141, 150, 151, 155, 156, 157, 159, 160, 161, 162, 163, 164, 165, 166, 179, 180, 182, 183, 184, 185, 186], "branches": [[86, 87], [86, 89], [90, 91], [90, 92], [92, 98], [92, 99], [99, 100], [99, 101], [103, 107], [103, 186], [107, 108], [107, 110], [113, 125], [113, 126], [129, 130], [129, 131], [132, 133], [132, 139], [136, 138], [136, 139], [139, 140], [139, 141], [141, 150], [141, 155], [150, 151], [150, 155], [156, 157], [156, 159], [163, 179], [163, 182]]}
# gained: {"lines": [55, 57, 58, 59, 60, 61, 86, 87, 89, 90, 92, 99, 100, 101, 102, 103, 104, 105, 107, 110, 112, 113, 114, 126, 127, 132, 133, 134, 135, 136, 139, 140, 141, 150, 151, 155, 156, 157, 159, 160, 161, 162, 163, 164, 165, 166, 182, 183, 184, 185, 186], "branches": [[86, 87], [86, 89], [90, 92], [92, 99], [99, 100], [103, 107], [103, 186], [107, 110], [113, 126], [132, 133], [136, 139], [139, 140], [139, 141], [141, 150], [141, 155], [150, 151], [156, 157], [156, 159], [163, 182]]}

import pytest
import socket
import errno
import sys
from tornado.netutil import bind_sockets
from tornado.util import errno_from_exception

def test_bind_sockets_ipv4():
    sockets = bind_sockets(0, family=socket.AF_INET)
    assert len(sockets) > 0
    for sock in sockets:
        assert sock.family == socket.AF_INET
        sock.close()

def test_bind_sockets_ipv6():
    if not socket.has_ipv6:
        pytest.skip("IPv6 is not supported on this platform")
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

def test_bind_sockets_reuse_port(monkeypatch):
    if not hasattr(socket, "SO_REUSEPORT"):
        pytest.skip("SO_REUSEPORT is not supported on this platform")
    sockets = bind_sockets(0, reuse_port=True)
    assert len(sockets) > 0
    for sock in sockets:
        assert sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT) == 1
        sock.close()

def test_bind_sockets_no_reuse_port(monkeypatch):
    monkeypatch.delattr(socket, "SO_REUSEPORT", raising=False)
    with pytest.raises(ValueError, match="the platform doesn't support SO_REUSEPORT"):
        bind_sockets(0, reuse_port=True)

def test_bind_sockets_errno_from_exception():
    try:
        raise OSError(errno.EADDRNOTAVAIL, "Address not available")
    except OSError as e:
        assert errno_from_exception(e) == errno.EADDRNOTAVAIL

def test_bind_sockets_address_localhost_ipv6(monkeypatch):
    if sys.platform != "darwin":
        pytest.skip("This test is specific to macOS")
    def mock_getaddrinfo(*args, **kwargs):
        return [(socket.AF_INET6, socket.SOCK_STREAM, 0, '', ('::1', 0, 0, 1))]
    monkeypatch.setattr(socket, "getaddrinfo", mock_getaddrinfo)
    sockets = bind_sockets(0, address="localhost")
    assert len(sockets) == 0

def test_bind_sockets_bind_error(monkeypatch):
    def mock_bind(*args, **kwargs):
        raise OSError(errno.EADDRNOTAVAIL, "Address not available")
    monkeypatch.setattr(socket.socket, "bind", mock_bind)
    with pytest.raises(OSError, match="Address not available"):
        bind_sockets(0, address="localhost")

def test_bind_sockets_reuseaddr_not_supported(monkeypatch):
    def mock_setsockopt(sock, level, optname, value):
        if level == socket.SOL_SOCKET and optname == socket.SO_REUSEADDR:
            raise OSError(errno.ENOPROTOOPT, "Protocol not available")
        original_setsockopt(sock, level, optname, value)
    
    original_setsockopt = socket.socket.setsockopt
    monkeypatch.setattr(socket.socket, "setsockopt", mock_setsockopt)
    
    sockets = bind_sockets(0)
    assert len(sockets) > 0
    for sock in sockets:
        sock.close()
