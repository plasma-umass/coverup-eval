# file lib/ansible/module_utils/facts/other/facter.py:64-85
# lines [64, 68, 70, 71, 73, 76, 77, 79, 80, 81, 83, 85]
# branches ['70->71', '70->73', '76->77', '76->79']

import json
import pytest
from ansible.module_utils.facts.other.facter import FacterFactCollector

# Mocking the module that would be passed to the FacterFactCollector
class MockModule:
    def __init__(self, mocker):
        self.mocker = mocker

    def run_command(self, command):
        return (0, '{"facter_key": "facter_value"}', '')

    def get_bin_path(self, bin_name, opt_dirs=[]):
        return self.mocker.MagicMock()

@pytest.fixture
def mock_module(mocker):
    mock = MockModule(mocker)
    mocker.patch.object(mock, 'run_command', return_value=(0, '{"facter_key": "facter_value"}', ''))
    return mock

def test_facter_fact_collector_collect_with_valid_json(mock_module):
    facter = FacterFactCollector()
    result = facter.collect(module=mock_module)
    assert result == {"facter_key": "facter_value"}

@pytest.fixture
def mock_module_with_invalid_json(mocker):
    mock = MockModule(mocker)
    mocker.patch.object(mock, 'run_command', return_value=(0, 'not a valid json', ''))
    return mock

def test_facter_fact_collector_collect_with_invalid_json(mock_module_with_invalid_json):
    facter = FacterFactCollector()
    result = facter.collect(module=mock_module_with_invalid_json)
    assert result == {}

@pytest.fixture
def mock_module_with_none_output(mocker):
    mock = MockModule(mocker)
    mocker.patch.object(mock, 'run_command', return_value=(0, None, ''))
    return mock

def test_facter_fact_collector_collect_with_none_output(mock_module_with_none_output):
    facter = FacterFactCollector()
    result = facter.collect(module=mock_module_with_none_output)
    assert result == {}

def test_facter_fact_collector_collect_without_module():
    facter = FacterFactCollector()
    result = facter.collect()
    assert result == {}
