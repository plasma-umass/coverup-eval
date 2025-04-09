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

def test_is_valid_ip_invalid_ip(mocker):
    mocker.patch('socket.getaddrinfo', side_effect=socket.gaierror(socket.EAI_NONAME, ''))
    assert not is_valid_ip("invalid_ip")

def test_is_valid_ip_gaierror_other(mocker):
    mocker.patch('socket.getaddrinfo', side_effect=socket.gaierror(socket.EAI_AGAIN, ''))
    with pytest.raises(socket.gaierror):
        is_valid_ip("another_invalid_ip")
