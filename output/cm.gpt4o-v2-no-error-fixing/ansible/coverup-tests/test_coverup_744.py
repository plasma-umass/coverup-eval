# file: lib/ansible/module_utils/facts/network/linux.py:47-62
# asked: {"lines": [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], "branches": [[50, 51], [50, 52], [56, 57], [56, 58]]}
# gained: {"lines": [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], "branches": [[50, 51], [50, 52], [56, 57], [56, 58]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.network.linux import LinuxNetwork

@pytest.fixture
def linux_network():
    module = MagicMock()
    network = LinuxNetwork(module)
    return network

def test_populate_no_ip_path(linux_network):
    linux_network.module.get_bin_path = MagicMock(return_value=None)
    result = linux_network.populate()
    assert result == {}

@patch('ansible.module_utils.facts.network.linux.LinuxNetwork.get_default_interfaces')
@patch('ansible.module_utils.facts.network.linux.LinuxNetwork.get_interfaces_info')
def test_populate_with_ip_path(mock_get_interfaces_info, mock_get_default_interfaces, linux_network):
    linux_network.module.get_bin_path = MagicMock(return_value='/sbin/ip')
    mock_get_default_interfaces.return_value = ({'address': '192.168.1.1'}, {'address': 'fe80::1'})
    mock_get_interfaces_info.return_value = (
        {'eth0': {'device': 'eth0', 'macaddress': '00:00:00:00:00:00'}},
        {'all_ipv4_addresses': ['192.168.1.1'], 'all_ipv6_addresses': ['fe80::1']}
    )
    
    result = linux_network.populate()
    
    assert 'interfaces' in result
    assert 'eth0' in result
    assert result['default_ipv4'] == {'address': '192.168.1.1'}
    assert result['default_ipv6'] == {'address': 'fe80::1'}
    assert result['all_ipv4_addresses'] == ['192.168.1.1']
    assert result['all_ipv6_addresses'] == ['fe80::1']
