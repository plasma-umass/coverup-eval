# file: lib/ansible/modules/iptables.py:683-685
# asked: {"lines": [684, 685], "branches": []}
# gained: {"lines": [684, 685], "branches": []}

import pytest
from unittest import mock

# Mocking the push_arguments function
def mock_push_arguments(iptables_path, action, params, make_rule=True):
    return [iptables_path, action, params]

# Mocking the run_command method
class MockModule:
    def run_command(self, cmd, check_rc):
        assert cmd == ['/sbin/iptables', '-I', {'table': 'filter', 'chain': 'INPUT', 'rule_num': '1'}]
        assert check_rc == True
        return 0, '', ''

def test_insert_rule(monkeypatch):
    from ansible.modules.iptables import insert_rule

    # Mocking the push_arguments function and module.run_command method
    monkeypatch.setattr('ansible.modules.iptables.push_arguments', mock_push_arguments)
    module = MockModule()

    params = {'table': 'filter', 'chain': 'INPUT', 'rule_num': '1'}
    iptables_path = '/sbin/iptables'

    insert_rule(iptables_path, module, params)
