# file lib/ansible/module_utils/facts/other/facter.py:46-50
# lines [46, 49, 50]
# branches []

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.other.facter import FacterFactCollector

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def facter_path():
    return "/usr/bin/facter"

def test_run_facter_success(mock_module, facter_path):
    collector = FacterFactCollector()
    mock_module.run_command.return_value = (0, '{"fact": "value"}', '')

    rc, out, err = collector.run_facter(mock_module, facter_path)

    mock_module.run_command.assert_called_once_with(facter_path + " --puppet --json")
    assert rc == 0
    assert out == '{"fact": "value"}'
    assert err == ''

def test_run_facter_failure(mock_module, facter_path):
    collector = FacterFactCollector()
    mock_module.run_command.return_value = (1, '', 'error message')

    rc, out, err = collector.run_facter(mock_module, facter_path)

    mock_module.run_command.assert_called_once_with(facter_path + " --puppet --json")
    assert rc == 1
    assert out == ''
    assert err == 'error message'
