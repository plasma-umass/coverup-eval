# file lib/ansible/module_utils/common/network.py:64-83
# lines [64, 66, 67, 68, 69, 70, 71, 72, 74, 75, 77, 78, 79, 81, 82, 83]
# branches ['67->68', '67->69', '78->79', '78->81', '81->82', '81->83']

import pytest
from ansible.module_utils.common.network import to_subnet

def test_to_subnet_with_dotted_notation(mocker):
    # Mock the is_masklen and to_netmask functions
    mocker.patch('ansible.module_utils.common.network.is_masklen', return_value=False)
    mocker.patch('ansible.module_utils.common.network.to_netmask', side_effect=lambda x: '255.255.255.0' if x == 24 else '255.255.0.0')
    mocker.patch('ansible.module_utils.common.network.to_masklen', return_value=24)

    # Test with dotted_notation=True
    subnet = to_subnet('192.168.1.1', '255.255.255.0', dotted_notation=True)
    assert subnet == '192.168.1.0 255.255.255.0', "The subnet should be in dotted notation with a space separator"

def test_to_subnet_with_cidr_notation(mocker):
    # Mock the is_masklen and to_netmask functions
    mocker.patch('ansible.module_utils.common.network.is_masklen', return_value=True)
    mocker.patch('ansible.module_utils.common.network.to_netmask', return_value='255.255.255.0')
    mocker.patch('ansible.module_utils.common.network.to_masklen', return_value=24)

    # Test with dotted_notation=False
    subnet = to_subnet('192.168.1.1', '24', dotted_notation=False)
    assert subnet == '192.168.1.0/24', "The subnet should be in CIDR notation with a slash separator"
