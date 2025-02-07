# file: lib/ansible/modules/iptables.py:704-711
# asked: {"lines": [705, 706, 707, 708, 709, 710, 711], "branches": [[709, 710], [709, 711]]}
# gained: {"lines": [705, 706, 707, 708, 709, 710, 711], "branches": [[709, 710], [709, 711]]}

import pytest
import re
from unittest import mock

# Assuming the function get_chain_policy is in a module named iptables
from ansible.modules.iptables import get_chain_policy

@pytest.fixture
def mock_module():
    module = mock.Mock()
    return module

def test_get_chain_policy_with_policy(mock_module):
    iptables_path = '/sbin/iptables'
    params = {'table': 'filter', 'chain': 'INPUT'}
    
    # Mock the output of the run_command method
    mock_module.run_command.return_value = (0, "Chain INPUT (policy ACCEPT)", "")
    
    result = get_chain_policy(iptables_path, mock_module, params)
    
    # Verify the result
    assert result == 'ACCEPT'
    
    # Verify that run_command was called with the correct command
    expected_cmd = [iptables_path, '-t', 'filter', '-L', 'INPUT']
    mock_module.run_command.assert_called_once_with(expected_cmd, check_rc=True)

def test_get_chain_policy_without_policy(mock_module):
    iptables_path = '/sbin/iptables'
    params = {'table': 'filter', 'chain': 'INPUT'}
    
    # Mock the output of the run_command method
    mock_module.run_command.return_value = (0, "Chain INPUT (some other output)", "")
    
    result = get_chain_policy(iptables_path, mock_module, params)
    
    # Verify the result
    assert result is None
    
    # Verify that run_command was called with the correct command
    expected_cmd = [iptables_path, '-t', 'filter', '-L', 'INPUT']
    mock_module.run_command.assert_called_once_with(expected_cmd, check_rc=True)
