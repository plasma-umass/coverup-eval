# file: lib/ansible/module_utils/facts/network/linux.py:64-97
# asked: {"lines": [81], "branches": [[80, 81]]}
# gained: {"lines": [81], "branches": [[80, 81]]}

import pytest
import socket
from unittest.mock import patch, MagicMock

# Assuming the LinuxNetwork class is imported from the module
from ansible.module_utils.facts.network.linux import LinuxNetwork

@pytest.fixture
def linux_network():
    # Mock the module argument required by the Network class
    mock_module = MagicMock()
    return LinuxNetwork(mock_module)

def test_get_default_interfaces_v6_no_ipv6_support(linux_network, monkeypatch):
    # Mock socket.has_ipv6 to be False to ensure line 81 is executed
    monkeypatch.setattr(socket, 'has_ipv6', False)
    
    # Mock the run_command method to avoid actual command execution
    with patch.object(linux_network.module, 'run_command', return_value=(0, '', '')) as mock_run_command:
        v4_interface, v6_interface = linux_network.get_default_interfaces('/sbin/ip')
        
        # Assertions to verify the expected behavior
        assert v4_interface == {}
        assert v6_interface == {}
        mock_run_command.assert_called_once_with(['/sbin/ip', '-4', 'route', 'get', '8.8.8.8'], errors='surrogate_then_replace')

def test_get_default_interfaces_v6_with_ipv6_support(linux_network, monkeypatch):
    # Mock socket.has_ipv6 to be True to ensure line 81 is not executed
    monkeypatch.setattr(socket, 'has_ipv6', True)
    
    # Mock the run_command method to return a valid IPv6 route
    mock_output_v6 = "2404:6800:400a:800::1012 dev eth0 src 2001:db8::1"
    with patch.object(linux_network.module, 'run_command', side_effect=[(0, '', ''), (0, mock_output_v6, '')]) as mock_run_command:
        v4_interface, v6_interface = linux_network.get_default_interfaces('/sbin/ip')
        
        # Assertions to verify the expected behavior
        assert v4_interface == {}
        assert v6_interface == {
            'interface': 'eth0',
            'address': '2001:db8::1'
        }
        mock_run_command.assert_any_call(['/sbin/ip', '-4', 'route', 'get', '8.8.8.8'], errors='surrogate_then_replace')
        mock_run_command.assert_any_call(['/sbin/ip', '-6', 'route', 'get', '2404:6800:400a:800::1012'], errors='surrogate_then_replace')
