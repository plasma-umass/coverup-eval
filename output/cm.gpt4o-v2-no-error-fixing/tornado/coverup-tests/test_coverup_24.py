# file: tornado/tcpclient.py:75-98
# asked: {"lines": [75, 76, 90, 91, 92, 93, 94, 95, 97, 98], "branches": [[93, 94], [93, 98], [94, 95], [94, 97]]}
# gained: {"lines": [75, 76, 90, 91, 92, 93, 94, 95, 97, 98], "branches": [[93, 94], [93, 98], [94, 95], [94, 97]]}

import pytest
import socket
from typing import List, Tuple
from tornado.tcpclient import _Connector

def test_split_ipv4_ipv6():
    addrinfo = [
        (socket.AF_INET, ('192.168.1.1', 80)),
        (socket.AF_INET6, ('::1', 80)),
        (socket.AF_INET, ('192.168.1.2', 80)),
        (socket.AF_INET6, ('::2', 80)),
    ]
    primary, secondary = _Connector.split(addrinfo)
    assert primary == [
        (socket.AF_INET, ('192.168.1.1', 80)),
        (socket.AF_INET, ('192.168.1.2', 80)),
    ]
    assert secondary == [
        (socket.AF_INET6, ('::1', 80)),
        (socket.AF_INET6, ('::2', 80)),
    ]

def test_split_single_family():
    addrinfo = [
        (socket.AF_INET, ('192.168.1.1', 80)),
        (socket.AF_INET, ('192.168.1.2', 80)),
    ]
    primary, secondary = _Connector.split(addrinfo)
    assert primary == [
        (socket.AF_INET, ('192.168.1.1', 80)),
        (socket.AF_INET, ('192.168.1.2', 80)),
    ]
    assert secondary == []

def test_split_non_standard_family():
    addrinfo = [
        (socket.AF_INET, ('192.168.1.1', 80)),
        (socket.AF_INET, ('192.168.1.2', 80)),
        (socket.AF_UNIX, ('/tmp/socket',)),
    ]
    primary, secondary = _Connector.split(addrinfo)
    assert primary == [
        (socket.AF_INET, ('192.168.1.1', 80)),
        (socket.AF_INET, ('192.168.1.2', 80)),
    ]
    assert secondary == [
        (socket.AF_UNIX, ('/tmp/socket',)),
    ]
