# file: lib/ansible/modules/iptables.py:688-690
# asked: {"lines": [688, 689, 690], "branches": []}
# gained: {"lines": [688, 689, 690], "branches": []}

import pytest
from unittest.mock import Mock

from ansible.modules.iptables import remove_rule, push_arguments

def test_remove_rule(monkeypatch):
    def mock_push_arguments(iptables_path, action, params, make_rule=True):
        return [iptables_path, action, params['table'], params['chain']]

    def mock_run_command(cmd, check_rc):
        assert cmd == ['/sbin/iptables', '-D', 'filter', 'INPUT']
        assert check_rc is True
        return 0, '', ''

    monkeypatch.setattr('ansible.modules.iptables.push_arguments', mock_push_arguments)
    module = Mock()
    module.run_command = Mock(side_effect=mock_run_command)

    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'rule_num': None
    }

    remove_rule('/sbin/iptables', module, params)
    module.run_command.assert_called_once()
