# file: lib/ansible/module_utils/facts/other/facter.py:46-50
# asked: {"lines": [46, 49, 50], "branches": []}
# gained: {"lines": [46, 49, 50], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.module_utils.facts.other.facter import FacterFactCollector

@pytest.fixture
def mock_module():
    return Mock()

def test_run_facter_success(mock_module):
    facter_collector = FacterFactCollector()
    mock_module.run_command.return_value = (0, '{"facter": "data"}', '')

    rc, out, err = facter_collector.run_facter(mock_module, '/usr/bin/facter')

    assert rc == 0
    assert out == '{"facter": "data"}'
    assert err == ''
    mock_module.run_command.assert_called_once_with('/usr/bin/facter --puppet --json')

def test_run_facter_failure(mock_module):
    facter_collector = FacterFactCollector()
    mock_module.run_command.return_value = (1, '', 'error')

    rc, out, err = facter_collector.run_facter(mock_module, '/usr/bin/facter')

    assert rc == 1
    assert out == ''
    assert err == 'error'
    mock_module.run_command.assert_called_once_with('/usr/bin/facter --puppet --json')
