# file: lib/ansible/modules/iptables.py:678-680
# asked: {"lines": [679, 680], "branches": []}
# gained: {"lines": [679, 680], "branches": []}

import pytest
from unittest import mock

# Assuming push_arguments and append_rule are in a module named iptables
from ansible.modules.iptables import append_rule, push_arguments

@pytest.fixture
def mock_module():
    return mock.Mock()

def test_append_rule(mock_module):
    iptables_path = "/sbin/iptables"
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'rule_num': None,
        'protocol': 'tcp',
        'source': '1.2.3.4',
        'destination': '5.6.7.8',
        'jump': 'ACCEPT'
    }

    expected_cmd = [
        iptables_path,
        '-t', 'filter',
        '-A', 'INPUT',
        '-p', 'tcp',
        '-s', '1.2.3.4',
        '-d', '5.6.7.8',
        '-j', 'ACCEPT'
    ]

    with mock.patch('ansible.modules.iptables.push_arguments', return_value=expected_cmd) as mock_push_arguments:
        append_rule(iptables_path, mock_module, params)
        mock_push_arguments.assert_called_once_with(iptables_path, '-A', params)
        mock_module.run_command.assert_called_once_with(expected_cmd, check_rc=True)
