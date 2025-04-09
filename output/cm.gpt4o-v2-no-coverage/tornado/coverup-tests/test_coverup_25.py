# file: tornado/netutil.py:286-304
# asked: {"lines": [286, 291, 294, 295, 296, 297, 299, 300, 301, 302, 303], "branches": [[291, 294], [291, 295], [301, 302], [301, 303]]}
# gained: {"lines": [286, 291, 294, 295, 296, 297, 299, 300, 301, 302, 303], "branches": [[291, 294], [291, 295], [301, 302], [301, 303]]}

import pytest
import socket
from tornado.netutil import is_valid_ip

def test_is_valid_ip_empty_string():
    assert not is_valid_ip("")

def test_is_valid_ip_null_byte():
    assert not is_valid_ip("127.0.0.1\x00")

def test_is_valid_ip_valid_ipv4():
    assert is_valid_ip("127.0.0.1")

def test_is_valid_ip_valid_ipv6():
    assert is_valid_ip("::1")

def test_is_valid_ip_invalid_ip(monkeypatch):
    def mock_getaddrinfo(ip, *args, **kwargs):
        raise socket.gaierror(socket.EAI_NONAME, 'mocked error')
    monkeypatch.setattr(socket, 'getaddrinfo', mock_getaddrinfo)
    assert not is_valid_ip("invalid_ip")

def test_is_valid_ip_raises_other_gaierror(monkeypatch):
    def mock_getaddrinfo(ip, *args, **kwargs):
        raise socket.gaierror(socket.EAI_AGAIN, 'mocked error')
    monkeypatch.setattr(socket, 'getaddrinfo', mock_getaddrinfo)
    with pytest.raises(socket.gaierror):
        is_valid_ip("127.0.0.1")
