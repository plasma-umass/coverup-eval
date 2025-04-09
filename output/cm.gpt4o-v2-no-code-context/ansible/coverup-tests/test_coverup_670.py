# file: lib/ansible/modules/iptables.py:683-685
# asked: {"lines": [683, 684, 685], "branches": []}
# gained: {"lines": [683, 684, 685], "branches": []}

import pytest
from unittest.mock import Mock

# Assuming the function insert_rule is imported from the module
from ansible.modules.iptables import insert_rule, push_arguments

def test_insert_rule(mocker):
    iptables_path = '/sbin/iptables'
    params = ['INPUT', '1', '-s', '192.168.1.1', '-j', 'ACCEPT']
    
    # Mock the module and its run_command method
    module = Mock()
    module.run_command = Mock(return_value=(0, '', ''))

    # Mock the push_arguments function
    mock_push_arguments = mocker.patch('ansible.modules.iptables.push_arguments', return_value=['/sbin/iptables', '-I', 'INPUT', '1', '-s', '192.168.1.1', '-j', 'ACCEPT'])

    # Call the function
    insert_rule(iptables_path, module, params)

    # Assert that push_arguments was called with the correct parameters
    mock_push_arguments.assert_called_once_with(iptables_path, '-I', params)

    # Assert that run_command was called with the correct command
    module.run_command.assert_called_once_with(['/sbin/iptables', '-I', 'INPUT', '1', '-s', '192.168.1.1', '-j', 'ACCEPT'], check_rc=True)
