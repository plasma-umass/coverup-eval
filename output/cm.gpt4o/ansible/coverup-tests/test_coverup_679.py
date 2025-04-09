# file lib/ansible/modules/iptables.py:672-675
# lines [672, 673, 674, 675]
# branches []

import pytest
from unittest import mock
from ansible.module_utils.basic import AnsibleModule
from ansible.modules.iptables import check_present

@pytest.fixture
def mock_module(mocker):
    module = mocker.Mock(spec=AnsibleModule)
    return module

def test_check_present(mocker, mock_module):
    iptables_path = '/sbin/iptables'
    params = ['-A', 'INPUT', '-p', 'tcp', '--dport', '22', '-j', 'ACCEPT']
    
    # Mock the push_arguments function
    mocker.patch('ansible.modules.iptables.push_arguments', return_value=[iptables_path, '-C'] + params)
    
    # Mock the run_command method to simulate the command execution
    mock_module.run_command.return_value = (0, '', '')  # Simulate command success
    
    # Call the function and assert the result
    result = check_present(iptables_path, mock_module, params)
    assert result is True
    
    # Verify that run_command was called with the correct arguments
    mock_module.run_command.assert_called_once_with([iptables_path, '-C'] + params, check_rc=False)
    
    # Simulate command failure
    mock_module.run_command.return_value = (1, '', '')
    
    # Call the function and assert the result
    result = check_present(iptables_path, mock_module, params)
    assert result is False
    
    # Verify that run_command was called again with the correct arguments
    assert mock_module.run_command.call_count == 2
