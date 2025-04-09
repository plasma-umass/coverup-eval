# file: lib/ansible/modules/iptables.py:688-690
# asked: {"lines": [688, 689, 690], "branches": []}
# gained: {"lines": [688, 689, 690], "branches": []}

import pytest
from unittest import mock

# Mocking the push_arguments function
def mock_push_arguments(iptables_path, action, params, make_rule=True):
    return [iptables_path, '-t', params['table'], action, params['chain']]

# Mocking the module with run_command method
class MockModule:
    def run_command(self, cmd, check_rc):
        assert cmd == ['/sbin/iptables', '-t', 'filter', '-D', 'INPUT']
        assert check_rc is True
        return 0, '', ''

@pytest.fixture
def mock_module():
    return MockModule()

def test_remove_rule(mock_module, monkeypatch):
    monkeypatch.setattr('ansible.modules.iptables.push_arguments', mock_push_arguments)
    
    params = {
        'table': 'filter',
        'chain': 'INPUT',
        'rule_num': None
    }
    
    from ansible.modules.iptables import remove_rule
    remove_rule('/sbin/iptables', mock_module, params)
