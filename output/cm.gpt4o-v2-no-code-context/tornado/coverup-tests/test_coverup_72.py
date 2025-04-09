# file: tornado/netutil.py:374-386
# asked: {"lines": [374, 375, 382, 383, 384, 385, 386], "branches": [[384, 385], [384, 386]]}
# gained: {"lines": [374, 375, 382, 383, 384, 385, 386], "branches": [[384, 385], [384, 386]]}

import socket
import pytest
from tornado.netutil import _resolve_addr

def test_resolve_addr_ipv4():
    result = _resolve_addr('localhost', 80, socket.AF_INET)
    assert len(result) > 0
    for fam, address in result:
        assert fam == socket.AF_INET

def test_resolve_addr_ipv6():
    result = _resolve_addr('localhost', 80, socket.AF_INET6)
    assert len(result) > 0
    for fam, address in result:
        assert fam == socket.AF_INET6

def test_resolve_addr_unspec():
    result = _resolve_addr('localhost', 80, socket.AF_UNSPEC)
    assert len(result) > 0
    families = {fam for fam, address in result}
    assert socket.AF_INET in families or socket.AF_INET6 in families

def test_resolve_addr_invalid_host():
    with pytest.raises(socket.gaierror):
        _resolve_addr('invalid_host', 80, socket.AF_UNSPEC)

def test_resolve_addr_invalid_port():
    with pytest.raises(socket.gaierror):
        _resolve_addr('localhost', 'invalid_port', socket.AF_UNSPEC)
