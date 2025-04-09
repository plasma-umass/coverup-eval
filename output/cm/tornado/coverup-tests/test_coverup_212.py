# file tornado/netutil.py:286-304
# lines [291, 294, 295, 296, 297, 299, 300, 301, 302, 303]
# branches ['291->294', '291->295', '301->302', '301->303']

import pytest
import socket
from tornado.netutil import is_valid_ip

def test_is_valid_ip_with_invalid_inputs(mocker):
    # Test with None and empty string
    assert not is_valid_ip(None)
    assert not is_valid_ip("")

    # Test with string containing null byte
    assert not is_valid_ip("127.0.0.1\x00")

    # Mock socket.getaddrinfo to raise a gaierror with EAI_NONAME
    mocker.patch('socket.getaddrinfo', side_effect=socket.gaierror(socket.EAI_NONAME))
    assert not is_valid_ip("invalid")

    # Mock socket.getaddrinfo to raise a different gaierror
    mocker.patch('socket.getaddrinfo', side_effect=socket.gaierror(socket.EAI_AGAIN))
    with pytest.raises(socket.gaierror):
        is_valid_ip("exception")

def test_is_valid_ip_with_valid_inputs():
    # Test with valid IPv4 address
    assert is_valid_ip("127.0.0.1")

    # Test with valid IPv6 address
    assert is_valid_ip("::1")
