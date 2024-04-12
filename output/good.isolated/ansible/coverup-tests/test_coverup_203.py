# file lib/ansible/module_utils/facts/network/linux.py:47-62
# lines [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]
# branches ['50->51', '50->52', '56->57', '56->58']

import pytest
from unittest.mock import MagicMock

# Assuming the LinuxNetwork class is part of the module ansible.module_utils.facts.network.linux
from ansible.module_utils.facts.network.linux import LinuxNetwork

@pytest.fixture
def mock_linux_network(mocker):
    mock_module = MagicMock()
    mock_module.get_bin_path = MagicMock(return_value='/usr/sbin/ip')
    linux_network = LinuxNetwork(module=mock_module)
    linux_network.get_default_interfaces = MagicMock(return_value=({}, {}))
    linux_network.get_interfaces_info = MagicMock(return_value=({'eth0': {}}, {'all_ipv4_addresses': [], 'all_ipv6_addresses': []}))
    return linux_network

def test_populate(mock_linux_network):
    collected_facts = {}
    network_facts = mock_linux_network.populate(collected_facts=collected_facts)

    # Assertions to verify postconditions
    assert isinstance(network_facts, dict)
    assert 'interfaces' in network_facts
    assert 'default_ipv4' in network_facts
    assert 'default_ipv6' in network_facts
    assert 'all_ipv4_addresses' in network_facts
    assert 'all_ipv6_addresses' in network_facts
    assert set(network_facts['interfaces']) == {'eth0'}  # Convert dict_keys to set before comparison
    assert network_facts['default_ipv4'] == {}
    assert network_facts['default_ipv6'] == {}
    assert network_facts['all_ipv4_addresses'] == []
    assert network_facts['all_ipv6_addresses'] == []
    assert 'eth0' in network_facts
    assert network_facts['eth0'] == {}

    # Verify that the mocks were called as expected
    mock_linux_network.module.get_bin_path.assert_called_once_with('ip')
    mock_linux_network.get_default_interfaces.assert_called_once()
    mock_linux_network.get_interfaces_info.assert_called_once()

    # No need to explicitly stop mocks, pytest will handle cleanup
