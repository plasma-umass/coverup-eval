# file lib/ansible/module_utils/common/network.py:51-61
# lines [51, 53, 54, 56, 57, 58, 59, 61]
# branches ['53->54', '53->56', '57->58', '57->61']

import pytest
from ansible.module_utils.common.network import to_masklen

def test_to_masklen_valid_netmask():
    assert to_masklen('255.255.255.0') == 24
    assert to_masklen('255.255.0.0') == 16
    assert to_masklen('255.0.0.0') == 8
    assert to_masklen('255.255.255.255') == 32

def test_to_masklen_invalid_netmask():
    with pytest.raises(ValueError, match='invalid value for netmask: 256.256.256.256'):
        to_masklen('256.256.256.256')
    with pytest.raises(ValueError, match='invalid value for netmask: 255.255.255.255.0'):
        to_masklen('255.255.255.255.0')
    with pytest.raises(ValueError, match='invalid value for netmask: 255.255.255'):
        to_masklen('255.255.255')
    with pytest.raises(ValueError, match='invalid value for netmask: abc.def.ghi.jkl'):
        to_masklen('abc.def.ghi.jkl')

def is_netmask(val):
    """ Dummy implementation for testing purposes """
    parts = val.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        try:
            num = int(part)
            if num < 0 or num > 255:
                return False
        except ValueError:
            return False
    return True

@pytest.fixture(autouse=True)
def mock_is_netmask(mocker):
    mocker.patch('ansible.module_utils.common.network.is_netmask', side_effect=is_netmask)
