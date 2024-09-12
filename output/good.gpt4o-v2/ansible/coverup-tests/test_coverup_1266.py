# file: lib/ansible/module_utils/common/network.py:39-48
# asked: {"lines": [42], "branches": [[41, 42]]}
# gained: {"lines": [42], "branches": [[41, 42]]}

import pytest
from ansible.module_utils.common.network import to_netmask

def test_to_netmask_valid():
    assert to_netmask(24) == '255.255.255.0'
    assert to_netmask(16) == '255.255.0.0'
    assert to_netmask(0) == '0.0.0.0'

def test_to_netmask_invalid():
    with pytest.raises(ValueError, match='invalid value for masklen'):
        to_netmask(33)
    with pytest.raises(ValueError, match='invalid value for masklen'):
        to_netmask(-1)
    with pytest.raises(ValueError, match='invalid value for masklen'):
        to_netmask('invalid')

