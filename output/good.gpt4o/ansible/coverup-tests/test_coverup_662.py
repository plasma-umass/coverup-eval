# file lib/ansible/modules/iptables.py:698-701
# lines [698, 699, 700, 701]
# branches []

import pytest
from unittest.mock import Mock, patch

# Assuming the function set_chain_policy is imported from ansible.modules.iptables
from ansible.modules.iptables import set_chain_policy

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def iptables_path():
    return '/sbin/iptables'

@pytest.fixture
def params():
    return {
        'policy': 'ACCEPT',
        'chain': 'INPUT'
    }

@patch('ansible.modules.iptables.push_arguments')
def test_set_chain_policy(mock_push_arguments, mock_module, iptables_path, params):
    mock_push_arguments.return_value = [iptables_path, '-P', params['chain']]
    
    set_chain_policy(iptables_path, mock_module, params)
    
    mock_push_arguments.assert_called_once_with(iptables_path, '-P', params, make_rule=False)
    mock_module.run_command.assert_called_once_with([iptables_path, '-P', params['chain'], params['policy']], check_rc=True)
