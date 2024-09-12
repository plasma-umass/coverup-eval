# file: lib/ansible/modules/iptables.py:678-680
# asked: {"lines": [678, 679, 680], "branches": []}
# gained: {"lines": [678, 679, 680], "branches": []}

import pytest
from unittest import mock

# Assuming the append_rule function is part of a class or module named 'iptables'
from ansible.modules.iptables import append_rule

def test_append_rule(monkeypatch):
    iptables_path = '/sbin/iptables'
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'protocol': 'tcp',
        'source': '192.168.1.1',
        'destination': '192.168.1.2',
        'jump': 'ACCEPT'
    }

    # Mocking the module and its run_command method
    module = mock.Mock()
    module.run_command = mock.Mock(return_value=(0, '', ''))

    def mock_push_arguments(iptables_path, action, params):
        return [iptables_path, '-t', params['table'], action, params['chain']]

    monkeypatch.setattr('ansible.modules.iptables.push_arguments', mock_push_arguments)

    append_rule(iptables_path, module, params)

    # Verifying that run_command was called with the expected command
    expected_cmd = [iptables_path, '-t', 'filter', '-A', 'INPUT']
    module.run_command.assert_called_once_with(expected_cmd, check_rc=True)
