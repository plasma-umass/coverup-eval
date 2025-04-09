# file: lib/ansible/module_utils/common/network.py:39-48
# asked: {"lines": [39, 41, 42, 44, 45, 46, 48], "branches": [[41, 42], [41, 44], [45, 46], [45, 48]]}
# gained: {"lines": [39, 41, 42, 44, 45, 46, 48], "branches": [[41, 42], [41, 44], [45, 46], [45, 48]]}

import pytest
from struct import pack
from socket import inet_ntoa
from ansible.module_utils.common.network import to_netmask, is_masklen

def test_to_netmask_valid_masklen():
    assert to_netmask(24) == '255.255.255.0'
    assert to_netmask(16) == '255.255.0.0'
    assert to_netmask(0) == '0.0.0.0'

def test_to_netmask_invalid_masklen():
    with pytest.raises(ValueError, match='invalid value for masklen'):
        to_netmask(33)
    with pytest.raises(ValueError, match='invalid value for masklen'):
        to_netmask(-1)
    with pytest.raises(ValueError, match='invalid value for masklen'):
        to_netmask('invalid')

def test_is_masklen():
    assert is_masklen(24) is True
    assert is_masklen(0) is True
    assert is_masklen(32) is True
    assert is_masklen(33) is False
    assert is_masklen(-1) is False
    assert is_masklen('invalid') is False
