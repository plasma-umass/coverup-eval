# file: lib/ansible/modules/iptables.py:678-680
# asked: {"lines": [678, 679, 680], "branches": []}
# gained: {"lines": [678, 679, 680], "branches": []}

import pytest
from unittest.mock import Mock, patch

# Assuming the function append_rule is imported from ansible/modules/iptables.py
from ansible.modules.iptables import append_rule

@patch('ansible.modules.iptables.push_arguments')
def test_append_rule(mock_push_arguments):
    # Mock the module and its run_command method
    module = Mock()
    module.run_command = Mock()

    # Define the parameters for the test
    iptables_path = '/sbin/iptables'
    params = {'chain': 'INPUT', 'protocol': 'tcp', 'dport': '22', 'jump': 'ACCEPT'}

    # Mock the return value of push_arguments
    expected_cmd = ['/sbin/iptables', '-A', 'INPUT', '-p', 'tcp', '--dport', '22', '-j', 'ACCEPT']
    mock_push_arguments.return_value = expected_cmd

    # Call the function with the mocked module
    append_rule(iptables_path, module, params)

    # Verify that push_arguments was called correctly
    mock_push_arguments.assert_called_once_with(iptables_path, '-A', params)

    # Verify that run_command was called correctly
    module.run_command.assert_called_once_with(expected_cmd, check_rc=True)
