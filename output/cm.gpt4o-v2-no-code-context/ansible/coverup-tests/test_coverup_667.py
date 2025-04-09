# file: lib/ansible/modules/iptables.py:688-690
# asked: {"lines": [688, 689, 690], "branches": []}
# gained: {"lines": [688, 689, 690], "branches": []}

import pytest
from unittest.mock import Mock, patch

# Assuming the function remove_rule is part of a class or module named iptables_module
from ansible.modules import iptables as iptables_module

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def mock_push_arguments():
    with patch('ansible.modules.iptables.push_arguments') as mock:
        yield mock

@pytest.fixture
def mock_run_command():
    with patch.object(Mock(), 'run_command') as mock:
        yield mock

def test_remove_rule(mock_module, mock_push_arguments, mock_run_command):
    iptables_path = '/sbin/iptables'
    params = ['-p', 'tcp', '--dport', '80', '-j', 'ACCEPT']

    # Mock the push_arguments to return a specific command
    mock_push_arguments.return_value = ['iptables', '-D', '-p', 'tcp', '--dport', '80', '-j', 'ACCEPT']

    # Assign the mock run_command to the module
    mock_module.run_command = mock_run_command

    # Call the function
    iptables_module.remove_rule(iptables_path, mock_module, params)

    # Assert push_arguments was called correctly
    mock_push_arguments.assert_called_once_with(iptables_path, '-D', params)

    # Assert run_command was called with the correct command
    mock_run_command.assert_called_once_with(['iptables', '-D', '-p', 'tcp', '--dport', '80', '-j', 'ACCEPT'], check_rc=True)
