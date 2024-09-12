# file: lib/ansible/module_utils/common/network.py:51-61
# asked: {"lines": [51, 53, 54, 56, 57, 58, 59, 61], "branches": [[53, 54], [53, 56], [57, 58], [57, 61]]}
# gained: {"lines": [51, 53, 54, 56, 57, 58, 59, 61], "branches": [[53, 54], [53, 56], [57, 58], [57, 61]]}

import pytest
from ansible.module_utils.common.network import to_masklen

def is_netmask(val):
    """Mocked is_netmask function for testing purposes."""
    parts = val.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
    return True

def test_to_masklen_valid_netmask(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.network.is_netmask', is_netmask)
    assert to_masklen('255.255.255.0') == 24
    assert to_masklen('255.255.0.0') == 16
    assert to_masklen('255.0.0.0') == 8
    assert to_masklen('255.255.255.255') == 32

def test_to_masklen_invalid_netmask(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.common.network.is_netmask', is_netmask)
    with pytest.raises(ValueError, match='invalid value for netmask: 255.255.255.256'):
        to_masklen('255.255.255.256')
    with pytest.raises(ValueError, match='invalid value for netmask: 255.255.255'):
        to_masklen('255.255.255')
    with pytest.raises(ValueError, match='invalid value for netmask: 255.255.255.-1'):
        to_masklen('255.255.255.-1')
    with pytest.raises(ValueError, match='invalid value for netmask: 255.255.255.abc'):
        to_masklen('255.255.255.abc')
