# file: lib/ansible/modules/iptables.py:698-701
# asked: {"lines": [698, 699, 700, 701], "branches": []}
# gained: {"lines": [698, 699, 700, 701], "branches": []}

import pytest
from unittest.mock import MagicMock

def test_set_chain_policy(monkeypatch):
    from ansible.modules.iptables import set_chain_policy, push_arguments

    # Mocking the module and its run_command method
    module = MagicMock()
    module.run_command = MagicMock()

    # Mocking the push_arguments function
    def mock_push_arguments(iptables_path, action, params, make_rule=True):
        return [iptables_path, '-t', params['table'], action, params['chain']]

    monkeypatch.setattr('ansible.modules.iptables.push_arguments', mock_push_arguments)

    iptables_path = '/sbin/iptables'
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'policy': 'DROP'
    }

    set_chain_policy(iptables_path, module, params)

    # Assertions to verify the correct command was run
    expected_cmd = ['/sbin/iptables', '-t', 'filter', '-P', 'INPUT', 'DROP']
    module.run_command.assert_called_once_with(expected_cmd, check_rc=True)
