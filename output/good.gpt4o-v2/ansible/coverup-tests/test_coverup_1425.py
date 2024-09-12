# file: lib/ansible/module_utils/facts/network/linux.py:64-97
# asked: {"lines": [96], "branches": [[95, 96]]}
# gained: {"lines": [96], "branches": [[95, 96]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.network.linux import LinuxNetwork

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def linux_network(mock_module):
    return LinuxNetwork(mock_module)

def test_get_default_interfaces_v4(linux_network, mock_module):
    mock_module.run_command.return_value = (0, "8.8.8.8 dev eth0 src 192.168.1.1 via 192.168.1.254", "")
    v4, v6 = linux_network.get_default_interfaces('/sbin/ip')
    assert v4 == {'interface': 'eth0', 'address': '192.168.1.1', 'gateway': '192.168.1.254'}
    assert v6 == {}

def test_get_default_interfaces_v6(linux_network, mock_module):
    mock_module.run_command.return_value = (0, "2404:6800:400a:800::1012 dev eth0 src 2001:db8::1 via 2001:db8::ff", "")
    with patch('socket.has_ipv6', True):
        v4, v6 = linux_network.get_default_interfaces('/sbin/ip')
    assert v4 == {}
    assert v6 == {'interface': 'eth0', 'address': '2001:db8::1', 'gateway': '2001:db8::ff'}

def test_get_default_interfaces_no_output(linux_network, mock_module):
    mock_module.run_command.return_value = (0, "", "")
    v4, v6 = linux_network.get_default_interfaces('/sbin/ip')
    assert v4 == {}
    assert v6 == {}

def test_get_default_interfaces_invalid_argument(linux_network, mock_module):
    mock_module.run_command.return_value = (0, "RTNETLINK answers: Invalid argument", "")
    v4, v6 = linux_network.get_default_interfaces('/sbin/ip')
    assert v4 == {}
    assert v6 == {}

def test_get_default_interfaces_redhat_v6(linux_network, mock_module):
    collected_facts = {
        'ansible_os_family': 'RedHat',
        'ansible_distribution_version': '4.8'
    }
    mock_module.run_command.return_value = (0, "", "")
    v4, v6 = linux_network.get_default_interfaces('/sbin/ip', collected_facts)
    assert v4 == {}
    assert v6 == {}
