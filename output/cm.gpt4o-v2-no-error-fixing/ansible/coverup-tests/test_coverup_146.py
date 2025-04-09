# file: lib/ansible/module_utils/facts/other/facter.py:64-85
# asked: {"lines": [64, 68, 70, 71, 73, 76, 77, 79, 80, 81, 83, 85], "branches": [[70, 71], [70, 73], [76, 77], [76, 79]]}
# gained: {"lines": [64, 68, 70, 71, 73, 76, 77, 79, 80, 81, 83, 85], "branches": [[70, 71], [70, 73], [76, 77], [76, 79]]}

import json
import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.other.facter import FacterFactCollector

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def facter_collector():
    return FacterFactCollector()

def test_collect_no_module(facter_collector):
    result = facter_collector.collect(module=None)
    assert result == {}

@patch.object(FacterFactCollector, 'get_facter_output', return_value=None)
def test_collect_no_facter_output(mock_get_facter_output, facter_collector, mock_module):
    result = facter_collector.collect(module=mock_module)
    assert result == {}

@patch.object(FacterFactCollector, 'get_facter_output', return_value='{"key": "value"}')
def test_collect_valid_facter_output(mock_get_facter_output, facter_collector, mock_module):
    result = facter_collector.collect(module=mock_module)
    assert result == {"key": "value"}

@patch.object(FacterFactCollector, 'get_facter_output', return_value='invalid json')
def test_collect_invalid_facter_output(mock_get_facter_output, facter_collector, mock_module):
    result = facter_collector.collect(module=mock_module)
    assert result == {}

@patch.object(FacterFactCollector, 'find_facter', return_value=None)
def test_get_facter_output_no_facter_path(mock_find_facter, facter_collector, mock_module):
    result = facter_collector.get_facter_output(module=mock_module)
    assert result is None

@patch.object(FacterFactCollector, 'find_facter', return_value='/path/to/facter')
@patch.object(FacterFactCollector, 'run_facter', return_value=(1, '', 'error'))
def test_get_facter_output_run_facter_error(mock_run_facter, mock_find_facter, facter_collector, mock_module):
    result = facter_collector.get_facter_output(module=mock_module)
    assert result is None

@patch.object(FacterFactCollector, 'find_facter', return_value='/path/to/facter')
@patch.object(FacterFactCollector, 'run_facter', return_value=(0, 'output', ''))
def test_get_facter_output_success(mock_run_facter, mock_find_facter, facter_collector, mock_module):
    result = facter_collector.get_facter_output(module=mock_module)
    assert result == 'output'
