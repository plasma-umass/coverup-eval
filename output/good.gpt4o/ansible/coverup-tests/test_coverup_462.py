# file lib/ansible/modules/iptables.py:704-711
# lines [704, 705, 706, 707, 708, 709, 710, 711]
# branches ['709->710', '709->711']

import pytest
import re
from unittest.mock import Mock

# Assuming the function get_chain_policy is imported from the module
from ansible.modules.iptables import get_chain_policy

def test_get_chain_policy(mocker):
    iptables_path = '/sbin/iptables'
    params = {'chain': 'INPUT', 'table': 'filter'}
    
    # Mocking the module and its run_command method
    module = Mock()
    mocker.patch.object(module, 'run_command', return_value=(0, 'Chain INPUT (policy ACCEPT)', ''))
    
    # Call the function
    policy = get_chain_policy(iptables_path, module, params)
    
    # Assertions to verify the postconditions
    assert policy == 'ACCEPT'
    
    # Clean up
    module.run_command.assert_called_once_with(['/sbin/iptables', '-t', 'filter', '-L', 'INPUT'], check_rc=True)

def test_get_chain_policy_no_policy(mocker):
    iptables_path = '/sbin/iptables'
    params = {'chain': 'INPUT', 'table': 'filter'}
    
    # Mocking the module and its run_command method
    module = Mock()
    mocker.patch.object(module, 'run_command', return_value=(0, 'Chain INPUT', ''))
    
    # Call the function
    policy = get_chain_policy(iptables_path, module, params)
    
    # Assertions to verify the postconditions
    assert policy is None
    
    # Clean up
    module.run_command.assert_called_once_with(['/sbin/iptables', '-t', 'filter', '-L', 'INPUT'], check_rc=True)
