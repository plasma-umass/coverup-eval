# file: lib/ansible/modules/iptables.py:698-701
# asked: {"lines": [699, 700, 701], "branches": []}
# gained: {"lines": [699, 700, 701], "branches": []}

import pytest
from unittest import mock

# Mocking the push_arguments function
def mock_push_arguments(iptables_path, action, params, make_rule=True):
    cmd = [iptables_path]
    cmd.extend(['-t', params['table']])
    cmd.extend([action, params['chain']])
    if action == '-I' and params['rule_num']:
        cmd.extend([params['rule_num']])
    if make_rule:
        cmd.extend(['--mock-rule'])
    return cmd

# Mocking the module with run_command method
class MockModule:
    def run_command(self, cmd, check_rc):
        assert cmd == ['/sbin/iptables', '-t', 'filter', '-P', 'INPUT', 'ACCEPT']
        assert check_rc is True
        return 0, '', ''

def test_set_chain_policy(monkeypatch):
    from ansible.modules.iptables import set_chain_policy

    # Mocking push_arguments and module.run_command
    monkeypatch.setattr('ansible.modules.iptables.push_arguments', mock_push_arguments)
    module = MockModule()

    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'policy': 'ACCEPT',
        'rule_num': None
    }

    set_chain_policy('/sbin/iptables', module, params)
