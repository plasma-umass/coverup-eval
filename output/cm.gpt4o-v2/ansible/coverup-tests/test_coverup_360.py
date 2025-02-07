# file: lib/ansible/module_utils/facts/other/facter.py:52-62
# asked: {"lines": [52, 53, 54, 55, 57, 59, 60, 62], "branches": [[54, 55], [54, 57], [59, 60], [59, 62]]}
# gained: {"lines": [52, 53, 54, 55, 57, 59, 60, 62], "branches": [[54, 55], [54, 57], [59, 60], [59, 62]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.other.facter import FacterFactCollector

@pytest.fixture
def mock_module():
    return MagicMock()

@pytest.fixture
def facter_collector():
    return FacterFactCollector()

def test_get_facter_output_no_facter_path(facter_collector, mock_module):
    with patch.object(facter_collector, 'find_facter', return_value=None):
        result = facter_collector.get_facter_output(mock_module)
        assert result is None

def test_get_facter_output_run_facter_failure(facter_collector, mock_module):
    with patch.object(facter_collector, 'find_facter', return_value='/usr/bin/facter'):
        with patch.object(facter_collector, 'run_facter', return_value=(1, '', 'error')):
            result = facter_collector.get_facter_output(mock_module)
            assert result is None

def test_get_facter_output_success(facter_collector, mock_module):
    with patch.object(facter_collector, 'find_facter', return_value='/usr/bin/facter'):
        with patch.object(facter_collector, 'run_facter', return_value=(0, 'output', '')):
            result = facter_collector.get_facter_output(mock_module)
            assert result == 'output'
