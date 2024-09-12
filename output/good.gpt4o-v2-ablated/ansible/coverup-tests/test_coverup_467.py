# file: lib/ansible/module_utils/facts/other/facter.py:46-50
# asked: {"lines": [49, 50], "branches": []}
# gained: {"lines": [49, 50], "branches": []}

import pytest
from ansible.module_utils.facts.other.facter import FacterFactCollector
from ansible.module_utils.basic import AnsibleModule

class MockModule:
    def run_command(self, command):
        if "facter" in command:
            return 0, '{"fact1": "value1"}', ''
        return 1, '', 'error'

@pytest.fixture
def mock_module():
    return MockModule()

def test_run_facter_success(mock_module):
    facter_collector = FacterFactCollector()
    rc, out, err = facter_collector.run_facter(mock_module, "facter")
    assert rc == 0
    assert out == '{"fact1": "value1"}'
    assert err == ''

def test_run_facter_failure(mock_module, monkeypatch):
    def mock_run_command_failure(command):
        return 1, '', 'error'
    
    monkeypatch.setattr(mock_module, "run_command", mock_run_command_failure)
    
    facter_collector = FacterFactCollector()
    rc, out, err = facter_collector.run_facter(mock_module, "facter")
    assert rc == 1
    assert out == ''
    assert err == 'error'
