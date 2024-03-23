# file lib/ansible/modules/iptables.py:688-690
# lines [689, 690]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.modules.iptables import remove_rule

@pytest.fixture
def mock_module(mocker):
    module_mock = MagicMock()
    module_mock.run_command = MagicMock(return_value=(0, "", ""))
    return module_mock

@pytest.fixture
def mock_push_arguments(mocker):
    return mocker.patch('ansible.modules.iptables.push_arguments', return_value='fake_command')

def test_remove_rule_executes_lines(mock_module, mock_push_arguments):
    iptables_path = '/sbin/iptables'
    params = {'chain': 'INPUT', 'protocol': 'tcp', 'jump': 'ACCEPT'}
    
    remove_rule(iptables_path, mock_module, params)
    
    mock_push_arguments.assert_called_once_with(iptables_path, '-D', params)
    mock_module.run_command.assert_called_once_with('fake_command', check_rc=True)

    # Cleanup is not necessary here as we are mocking the external interactions
