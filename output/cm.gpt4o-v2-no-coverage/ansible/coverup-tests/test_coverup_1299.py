# file: lib/ansible/modules/iptables.py:693-695
# asked: {"lines": [694, 695], "branches": []}
# gained: {"lines": [694, 695], "branches": []}

import pytest
from unittest.mock import Mock

# Assuming push_arguments and flush_table are imported from the module
from ansible.modules.iptables import push_arguments, flush_table

def test_flush_table(mocker):
    iptables_path = "/sbin/iptables"
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'rule_num': None
    }
    
    module = Mock()
    mocker.patch('ansible.modules.iptables.push_arguments', return_value=[iptables_path, '-t', 'filter', '-F', 'INPUT'])
    mocker.patch.object(module, 'run_command', return_value=(0, '', ''))

    flush_table(iptables_path, module, params)

    module.run_command.assert_called_once_with([iptables_path, '-t', 'filter', '-F', 'INPUT'], check_rc=True)
