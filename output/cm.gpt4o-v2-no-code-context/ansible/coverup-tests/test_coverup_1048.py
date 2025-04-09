# file: lib/ansible/modules/iptables.py:698-701
# asked: {"lines": [699, 700, 701], "branches": []}
# gained: {"lines": [699, 700, 701], "branches": []}

import pytest
from unittest.mock import Mock

# Assuming the function set_chain_policy is imported from the module
from ansible.modules.iptables import set_chain_policy

def test_set_chain_policy(monkeypatch):
    # Mocking the push_arguments function
    def mock_push_arguments(iptables_path, *args, **kwargs):
        return [iptables_path] + list(args)
    
    monkeypatch.setattr('ansible.modules.iptables.push_arguments', mock_push_arguments)
    
    # Mocking the module and its run_command method
    mock_module = Mock()
    mock_module.run_command = Mock()
    
    iptables_path = '/sbin/iptables'
    params = {
        'policy': 'ACCEPT'
    }
    
    set_chain_policy(iptables_path, mock_module, params)
    
    # Assertions to verify the correct command was constructed and run
    expected_cmd = ['/sbin/iptables', '-P', params]
    expected_cmd.append('ACCEPT')
    mock_module.run_command.assert_called_once_with(expected_cmd, check_rc=True)
