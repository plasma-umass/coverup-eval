# file: tornado/netutil.py:374-386
# asked: {"lines": [374, 375, 382, 383, 384, 385, 386], "branches": [[384, 385], [384, 386]]}
# gained: {"lines": [374, 375, 382, 383, 384, 385, 386], "branches": [[384, 385], [384, 386]]}

import pytest
import socket
from unittest import mock
from tornado.netutil import _resolve_addr

def test_resolve_addr_ipv4():
    host = 'localhost'
    port = 80
    family = socket.AF_INET

    with mock.patch('socket.getaddrinfo') as mock_getaddrinfo:
        mock_getaddrinfo.return_value = [
            (socket.AF_INET, socket.SOCK_STREAM, 6, '', ('127.0.0.1', port))
        ]
        result = _resolve_addr(host, port, family)
        assert result == [(socket.AF_INET, ('127.0.0.1', port))]

def test_resolve_addr_ipv6():
    host = 'localhost'
    port = 80
    family = socket.AF_INET6

    with mock.patch('socket.getaddrinfo') as mock_getaddrinfo:
        mock_getaddrinfo.return_value = [
            (socket.AF_INET6, socket.SOCK_STREAM, 6, '', ('::1', port, 0, 0))
        ]
        result = _resolve_addr(host, port, family)
        assert result == [(socket.AF_INET6, ('::1', port, 0, 0))]

def test_resolve_addr_unspec():
    host = 'localhost'
    port = 80
    family = socket.AF_UNSPEC

    with mock.patch('socket.getaddrinfo') as mock_getaddrinfo:
        mock_getaddrinfo.return_value = [
            (socket.AF_INET, socket.SOCK_STREAM, 6, '', ('127.0.0.1', port)),
            (socket.AF_INET6, socket.SOCK_STREAM, 6, '', ('::1', port, 0, 0))
        ]
        result = _resolve_addr(host, port, family)
        assert result == [
            (socket.AF_INET, ('127.0.0.1', port)),
            (socket.AF_INET6, ('::1', port, 0, 0))
        ]
