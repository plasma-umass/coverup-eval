# file: lib/ansible/module_utils/common/network.py:51-61
# asked: {"lines": [51, 53, 54, 56, 57, 58, 59, 61], "branches": [[53, 54], [53, 56], [57, 58], [57, 61]]}
# gained: {"lines": [51, 53, 54, 56, 57, 58, 59, 61], "branches": [[53, 54], [53, 56], [57, 58], [57, 61]]}

import pytest
from ansible.module_utils.common.network import to_masklen

def is_netmask(val):
    # Mock implementation of is_netmask for testing purposes
    valid_netmasks = ['255.255.255.0', '255.255.0.0', '255.0.0.0']
    return val in valid_netmasks

def test_to_masklen_valid_netmask(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.network.is_netmask', is_netmask)
    
    assert to_masklen('255.255.255.0') == 24
    assert to_masklen('255.255.0.0') == 16
    assert to_masklen('255.0.0.0') == 8

def test_to_masklen_invalid_netmask(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.network.is_netmask', is_netmask)
    
    with pytest.raises(ValueError, match='invalid value for netmask: 255.255.255.128'):
        to_masklen('255.255.255.128')
