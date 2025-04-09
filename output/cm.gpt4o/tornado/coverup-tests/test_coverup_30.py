# file tornado/netutil.py:286-304
# lines [286, 291, 294, 295, 296, 297, 299, 300, 301, 302, 303]
# branches ['291->294', '291->295', '301->302', '301->303']

import pytest
import socket
from tornado.netutil import is_valid_ip

def test_is_valid_ip_valid_ipv4():
    assert is_valid_ip("192.168.1.1") is True

def test_is_valid_ip_valid_ipv6():
    assert is_valid_ip("::1") is True

def test_is_valid_ip_empty_string():
    assert is_valid_ip("") is False

def test_is_valid_ip_null_byte():
    assert is_valid_ip("192.168.1.1\x00") is False

def test_is_valid_ip_invalid_ip(mocker):
    mocker.patch('socket.getaddrinfo', side_effect=socket.gaierror(socket.EAI_NONAME, ''))
    assert is_valid_ip("invalid_ip") is False

def test_is_valid_ip_gaierror_other(mocker):
    mocker.patch('socket.getaddrinfo', side_effect=socket.gaierror(socket.EAI_AGAIN, ''))
    with pytest.raises(socket.gaierror):
        is_valid_ip("another_invalid_ip")
