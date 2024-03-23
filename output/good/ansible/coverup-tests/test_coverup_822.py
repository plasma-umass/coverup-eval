# file lib/ansible/module_utils/facts/other/facter.py:46-50
# lines [46, 49, 50]
# branches []

import json
import pytest
from ansible.module_utils.facts.other.facter import FacterFactCollector

# Mocking the AnsibleModule class
class MockModule:
    def run_command(self, command):
        if command.endswith("--puppet --json"):
            return 0, '{"key": "value"}', ''  # Simulating successful command execution with JSON output
        else:
            return 1, '', 'Error'  # Simulating failed command execution

@pytest.fixture
def mock_module(mocker):
    mocker.patch('ansible.module_utils.basic.AnsibleModule.run_command', side_effect=MockModule().run_command)
    return MockModule()

def test_run_facter_with_json(mock_module):
    facter = FacterFactCollector()
    rc, out, err = facter.run_facter(mock_module, '/usr/bin/facter')
    assert rc == 0
    assert json.loads(out) == {"key": "value"}
    assert err == ''
