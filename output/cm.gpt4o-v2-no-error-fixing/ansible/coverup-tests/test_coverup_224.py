# file: lib/ansible/module_utils/facts/other/facter.py:52-62
# asked: {"lines": [52, 53, 54, 55, 57, 59, 60, 62], "branches": [[54, 55], [54, 57], [59, 60], [59, 62]]}
# gained: {"lines": [52, 53, 54, 55, 57, 59, 60, 62], "branches": [[54, 55], [54, 57], [59, 60], [59, 62]]}

import pytest
from unittest.mock import Mock
from ansible.module_utils.facts.other.facter import FacterFactCollector

@pytest.fixture
def mock_module():
    return Mock()

def test_get_facter_output_no_facter_path(mock_module):
    collector = FacterFactCollector()
    mock_module.get_bin_path.return_value = None
    result = collector.get_facter_output(mock_module)
    assert result is None

def test_get_facter_output_run_facter_failure(mock_module):
    collector = FacterFactCollector()
    mock_module.get_bin_path.return_value = '/usr/bin/facter'
    mock_module.run_command.return_value = (1, '', 'error')
    result = collector.get_facter_output(mock_module)
    assert result is None

def test_get_facter_output_success(mock_module):
    collector = FacterFactCollector()
    mock_module.get_bin_path.return_value = '/usr/bin/facter'
    mock_module.run_command.return_value = (0, 'output', '')
    result = collector.get_facter_output(mock_module)
    assert result == 'output'
