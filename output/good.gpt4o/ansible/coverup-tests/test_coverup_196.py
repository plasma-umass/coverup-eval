# file lib/ansible/module_utils/facts/network/linux.py:47-62
# lines [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]
# branches ['50->51', '50->52', '56->57', '56->58']

import pytest
from unittest.mock import MagicMock, patch

# Assuming the LinuxNetwork class is imported from ansible.module_utils.facts.network.linux
from ansible.module_utils.facts.network.linux import LinuxNetwork

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.get_bin_path = MagicMock()
    return module

@pytest.fixture
def linux_network(mock_module):
    return LinuxNetwork(module=mock_module)

def test_populate_no_ip_path(linux_network, mock_module):
    mock_module.get_bin_path.return_value = None
    result = linux_network.populate()
    assert result == {}

def test_populate_with_ip_path(linux_network, mock_module):
    mock_module.get_bin_path.return_value = '/sbin/ip'
    
    with patch.object(linux_network, 'get_default_interfaces', return_value=('eth0', 'eth1')) as mock_get_default_interfaces, \
         patch.object(linux_network, 'get_interfaces_info', return_value=({'eth0': {'mtu': 1500}, 'eth1': {'mtu': 1500}}, {'all_ipv4_addresses': ['192.168.1.1'], 'all_ipv6_addresses': ['fe80::1']})) as mock_get_interfaces_info:
        
        result = linux_network.populate()
        
        mock_get_default_interfaces.assert_called_once_with('/sbin/ip', collected_facts=None)
        mock_get_interfaces_info.assert_called_once_with('/sbin/ip', 'eth0', 'eth1')
        
        assert list(result['interfaces']) == ['eth0', 'eth1']
        assert result['eth0'] == {'mtu': 1500}
        assert result['eth1'] == {'mtu': 1500}
        assert result['default_ipv4'] == 'eth0'
        assert result['default_ipv6'] == 'eth1'
        assert result['all_ipv4_addresses'] == ['192.168.1.1']
        assert result['all_ipv6_addresses'] == ['fe80::1']
