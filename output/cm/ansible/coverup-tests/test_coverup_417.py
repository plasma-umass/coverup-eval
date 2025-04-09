# file lib/ansible/module_utils/facts/other/facter.py:52-62
# lines [52, 53, 54, 55, 57, 59, 60, 62]
# branches ['54->55', '54->57', '59->60', '59->62']

import pytest
from ansible.module_utils.facts.other.facter import FacterFactCollector

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    mock_module.run_command.return_value = (0, 'facter_output', '')
    return mock_module

@pytest.fixture
def mock_module_with_facter_not_found(mocker):
    mock_module = mocker.MagicMock()
    mock_module.run_command.return_value = (1, '', 'facter not found')
    return mock_module

@pytest.fixture
def mock_facter_fact_collector(mocker):
    mocker.patch.object(FacterFactCollector, 'find_facter', return_value='/usr/bin/facter')
    mocker.patch.object(FacterFactCollector, 'run_facter', return_value=(0, 'facter_output', ''))
    return FacterFactCollector()

@pytest.fixture
def mock_facter_fact_collector_with_facter_not_found(mocker):
    mocker.patch.object(FacterFactCollector, 'find_facter', return_value=None)
    return FacterFactCollector()

def test_get_facter_output_success(mock_facter_fact_collector, mock_module):
    output = mock_facter_fact_collector.get_facter_output(mock_module)
    assert output == 'facter_output'
    mock_facter_fact_collector.run_facter.assert_called_once_with(mock_module, '/usr/bin/facter')

def test_get_facter_output_facter_not_found(mock_facter_fact_collector_with_facter_not_found, mock_module):
    output = mock_facter_fact_collector_with_facter_not_found.get_facter_output(mock_module)
    assert output is None

def test_get_facter_output_facter_command_fails(mock_facter_fact_collector, mock_module_with_facter_not_found):
    mock_facter_fact_collector.run_facter.return_value = (1, '', 'facter not found')
    output = mock_facter_fact_collector.get_facter_output(mock_module_with_facter_not_found)
    assert output is None
    mock_facter_fact_collector.run_facter.assert_called_once_with(mock_module_with_facter_not_found, '/usr/bin/facter')
