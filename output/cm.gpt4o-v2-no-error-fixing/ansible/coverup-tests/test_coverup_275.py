# file: lib/ansible/modules/iptables.py:704-711
# asked: {"lines": [704, 705, 706, 707, 708, 709, 710, 711], "branches": [[709, 710], [709, 711]]}
# gained: {"lines": [704, 705, 706, 707, 708, 709, 710, 711], "branches": [[709, 710], [709, 711]]}

import pytest
from unittest.mock import Mock, patch
import re

# Assuming the function get_chain_policy is in a module named iptables
from ansible.modules.iptables import get_chain_policy

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def mock_params():
    return {
        'table': 'filter',
        'chain': 'INPUT'
    }

def test_get_chain_policy_with_policy(mock_module, mock_params):
    mock_module.run_command.return_value = (0, "Chain INPUT (policy ACCEPT)", "")
    
    result = get_chain_policy('/sbin/iptables', mock_module, mock_params)
    
    mock_module.run_command.assert_called_once_with(['/sbin/iptables', '-t', 'filter', '-L', 'INPUT'], check_rc=True)
    assert result == 'ACCEPT'

def test_get_chain_policy_without_policy(mock_module, mock_params):
    mock_module.run_command.return_value = (0, "Chain INPUT (some other text)", "")
    
    result = get_chain_policy('/sbin/iptables', mock_module, mock_params)
    
    mock_module.run_command.assert_called_once_with(['/sbin/iptables', '-t', 'filter', '-L', 'INPUT'], check_rc=True)
    assert result is None
