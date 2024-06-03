# file lib/ansible/module_utils/common/network.py:39-48
# lines [39, 41, 42, 44, 45, 46, 48]
# branches ['41->42', '41->44', '45->46', '45->48']

import pytest
from socket import inet_ntoa
from struct import pack

def is_masklen(val):
    try:
        val = int(val)
        return 0 <= val <= 32
    except ValueError:
        return False

def to_netmask(val):
    """ converts a masklen to a netmask """
    if not is_masklen(val):
        raise ValueError('invalid value for masklen')

    bits = 0
    for i in range(32 - int(val), 32):
        bits |= (1 << i)

    return inet_ntoa(pack('>I', bits))

def test_to_netmask_valid(mocker):
    mocker.patch('ansible.module_utils.common.network.is_masklen', side_effect=is_masklen)
    assert to_netmask(24) == '255.255.255.0'
    assert to_netmask(16) == '255.255.0.0'
    assert to_netmask(0) == '0.0.0.0'

def test_to_netmask_invalid(mocker):
    mocker.patch('ansible.module_utils.common.network.is_masklen', side_effect=is_masklen)
    with pytest.raises(ValueError, match='invalid value for masklen'):
        to_netmask(33)
    with pytest.raises(ValueError, match='invalid value for masklen'):
        to_netmask(-1)
    with pytest.raises(ValueError, match='invalid value for masklen'):
        to_netmask('invalid')
