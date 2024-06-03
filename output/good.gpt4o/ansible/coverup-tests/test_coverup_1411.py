# file lib/ansible/module_utils/common/network.py:39-48
# lines [41, 42, 44, 45, 46, 48]
# branches ['41->42', '41->44', '45->46', '45->48']

import pytest
from unittest.mock import patch
from socket import inet_ntoa
from struct import pack

# Assuming the is_masklen function is defined somewhere in the module
from ansible.module_utils.common.network import to_netmask, is_masklen

def test_to_netmask_invalid_masklen(mocker):
    mocker.patch('ansible.module_utils.common.network.is_masklen', return_value=False)
    with pytest.raises(ValueError, match='invalid value for masklen'):
        to_netmask('invalid')

def test_to_netmask_valid_masklen(mocker):
    mocker.patch('ansible.module_utils.common.network.is_masklen', return_value=True)
    result = to_netmask(24)
    expected = inet_ntoa(pack('>I', 0xFFFFFF00))
    assert result == expected

@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
