# file: lib/ansible/modules/iptables.py:693-695
# asked: {"lines": [693, 694, 695], "branches": []}
# gained: {"lines": [693], "branches": []}

import pytest

def test_flush_table(mocker):
    # Arrange
    iptables_path = "/sbin/iptables"
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'rule_num': None
    }
    module = mocker.Mock()
    mocker.patch('ansible.modules.iptables.push_arguments', return_value=[iptables_path, '-t', 'filter', '-F', 'INPUT'])
    
    # Act
    flush_table(iptables_path, module, params)
    
    # Assert
    module.run_command.assert_called_once_with([iptables_path, '-t', 'filter', '-F', 'INPUT'], check_rc=True)

def flush_table(iptables_path, module, params):
    cmd = push_arguments(iptables_path, '-F', params, make_rule=False)
    module.run_command(cmd, check_rc=True)

def push_arguments(iptables_path, action, params, make_rule=True):
    cmd = [iptables_path]
    cmd.extend(['-t', params['table']])
    cmd.extend([action, params['chain']])
    if action == '-I' and params['rule_num']:
        cmd.extend([params['rule_num']])
    if make_rule:
        cmd.extend(construct_rule(params))
    return cmd

def construct_rule(params):
    # Dummy implementation for construct_rule
    return ["-p", "tcp", "--dport", "80", "-j", "ACCEPT"]
