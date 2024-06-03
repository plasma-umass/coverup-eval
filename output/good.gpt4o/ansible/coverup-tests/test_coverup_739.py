# file lib/ansible/modules/iptables.py:678-680
# lines [678, 679, 680]
# branches []

import pytest
from unittest.mock import Mock, patch

# Assuming the function append_rule is imported from ansible.modules.iptables
from ansible.modules.iptables import append_rule

@pytest.fixture
def mock_module():
    module = Mock()
    module.run_command = Mock()
    return module

@pytest.fixture
def mock_push_arguments():
    with patch('ansible.modules.iptables.push_arguments') as mock:
        yield mock

def test_append_rule(mock_module, mock_push_arguments):
    iptables_path = '/sbin/iptables'
    params = ['-p', 'tcp', '--dport', '80', '-j', 'ACCEPT']
    
    # Mock the push_arguments to return a specific command
    mock_push_arguments.return_value = ['iptables', '-A', '-p', 'tcp', '--dport', '80', '-j', 'ACCEPT']
    
    append_rule(iptables_path, mock_module, params)
    
    # Verify that push_arguments was called with the correct parameters
    mock_push_arguments.assert_called_once_with(iptables_path, '-A', params)
    
    # Verify that run_command was called with the correct command
    mock_module.run_command.assert_called_once_with(['iptables', '-A', '-p', 'tcp', '--dport', '80', '-j', 'ACCEPT'], check_rc=True)
