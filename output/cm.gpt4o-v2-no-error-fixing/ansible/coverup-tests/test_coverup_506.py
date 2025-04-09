# file: lib/ansible/modules/iptables.py:693-695
# asked: {"lines": [693, 694, 695], "branches": []}
# gained: {"lines": [693, 694, 695], "branches": []}

import pytest
from unittest import mock

# Assuming the flush_table function is part of a module named iptables_module
from ansible.modules.iptables import flush_table

@pytest.fixture
def mock_module():
    return mock.Mock()

def test_flush_table(mock_module):
    iptables_path = '/sbin/iptables'
    params = {'table': 'filter', 'chain': 'INPUT'}

    with mock.patch('ansible.modules.iptables.push_arguments', return_value=['/sbin/iptables', '-t', 'filter', '-F', 'INPUT']):
        flush_table(iptables_path, mock_module, params)

    mock_module.run_command.assert_called_once_with(['/sbin/iptables', '-t', 'filter', '-F', 'INPUT'], check_rc=True)
