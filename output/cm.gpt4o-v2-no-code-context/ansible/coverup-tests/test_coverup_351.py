# file: lib/ansible/module_utils/common/network.py:39-48
# asked: {"lines": [39, 41, 42, 44, 45, 46, 48], "branches": [[41, 42], [41, 44], [45, 46], [45, 48]]}
# gained: {"lines": [39, 41, 42, 44, 45, 46, 48], "branches": [[41, 42], [41, 44], [45, 46], [45, 48]]}

import pytest
from ansible.module_utils.common.network import to_netmask
from socket import inet_ntoa
from struct import pack

def is_masklen(val):
    # Mock implementation of is_masklen for testing purposes
    return isinstance(val, int) and 0 <= val <= 32

def test_to_netmask_valid(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.network.is_masklen', is_masklen)
    
    assert to_netmask(24) == '255.255.255.0'
    assert to_netmask(16) == '255.255.0.0'
    assert to_netmask(0) == '0.0.0.0'

def test_to_netmask_invalid(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.network.is_masklen', is_masklen)
    
    with pytest.raises(ValueError, match='invalid value for masklen'):
        to_netmask(33)
    
    with pytest.raises(ValueError, match='invalid value for masklen'):
        to_netmask(-1)
    
    with pytest.raises(ValueError, match='invalid value for masklen'):
        to_netmask('invalid')
