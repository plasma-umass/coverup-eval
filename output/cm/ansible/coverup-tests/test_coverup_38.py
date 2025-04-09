# file lib/ansible/module_utils/facts/other/ohai.py:26-72
# lines [26, 27, 28, 29, 31, 32, 33, 34, 35, 37, 38, 39, 41, 42, 43, 45, 46, 47, 48, 50, 51, 52, 54, 56, 57, 58, 59, 61, 63, 64, 66, 67, 68, 70, 72]
# branches ['47->48', '47->50', '51->52', '51->54', '58->59', '58->61', '63->64', '63->66']

import json
import pytest
from ansible.module_utils.facts.other.ohai import OhaiFactCollector

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    mock_module.get_bin_path.return_value = '/usr/bin/ohai'
    mock_module.run_command.return_value = (0, '{"key": "value"}', '')
    return mock_module

def test_ohai_fact_collector_collect_with_module(mock_module):
    collector = OhaiFactCollector()
    facts = collector.collect(module=mock_module)
    assert facts == {"key": "value"}

def test_ohai_fact_collector_collect_without_module():
    collector = OhaiFactCollector()
    facts = collector.collect()
    assert facts == {}

def test_ohai_fact_collector_collect_with_failed_ohai(mock_module):
    mock_module.run_command.return_value = (1, '', 'error')
    collector = OhaiFactCollector()
    facts = collector.collect(module=mock_module)
    assert facts == {}

def test_ohai_fact_collector_collect_with_invalid_json(mock_module):
    mock_module.run_command.return_value = (0, 'not json', '')
    collector = OhaiFactCollector()
    facts = collector.collect(module=mock_module)
    assert facts == {}

def test_ohai_fact_collector_collect_with_missing_ohai(mock_module):
    mock_module.get_bin_path.return_value = None
    collector = OhaiFactCollector()
    facts = collector.collect(module=mock_module)
    assert facts == {}
