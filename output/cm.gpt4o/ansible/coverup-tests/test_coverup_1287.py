# file lib/ansible/module_utils/facts/sysctl.py:24-62
# lines [42]
# branches ['41->42']

import pytest
from unittest.mock import Mock, patch

# Assuming the function get_sysctl is imported from ansible.module_utils.facts.sysctl
from ansible.module_utils.facts.sysctl import get_sysctl

@pytest.fixture
def mock_module():
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    return module

def test_get_sysctl_empty_line(mock_module):
    prefixes = ['net.ipv4.ip_forward']
    
    # Mocking the run_command method to return a response with an empty line
    mock_module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\n\nnet.ipv4.conf.all.forwarding = 1\n', '')

    result = get_sysctl(mock_module, prefixes)
    
    # Assertions to verify the correct parsing of sysctl output
    assert result == {
        'net.ipv4.ip_forward': '1',
        'net.ipv4.conf.all.forwarding': '1'
    }

    # Ensure the run_command was called with the correct parameters
    mock_module.run_command.assert_called_once_with(['/sbin/sysctl', 'net.ipv4.ip_forward'])

def test_get_sysctl_cleanup(mock_module):
    prefixes = ['net.ipv4.ip_forward']
    
    # Mocking the run_command method to return a response with an empty line
    mock_module.run_command.return_value = (0, 'net.ipv4.ip_forward = 1\n\nnet.ipv4.conf.all.forwarding = 1\n', '')

    result = get_sysctl(mock_module, prefixes)
    
    # Assertions to verify the correct parsing of sysctl output
    assert result == {
        'net.ipv4.ip_forward': '1',
        'net.ipv4.conf.all.forwarding': '1'
    }

    # Ensure the run_command was called with the correct parameters
    mock_module.run_command.assert_called_once_with(['/sbin/sysctl', 'net.ipv4.ip_forward'])

    # Clean up mock
    mock_module.reset_mock()
