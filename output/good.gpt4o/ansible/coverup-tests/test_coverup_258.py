# file lib/ansible/module_utils/facts/other/facter.py:64-85
# lines [64, 68, 70, 71, 73, 76, 77, 79, 80, 81, 83, 85]
# branches ['70->71', '70->73', '76->77', '76->79']

import pytest
import json
from ansible.module_utils.facts.other.facter import FacterFactCollector
from unittest.mock import Mock, patch

@pytest.fixture
def mock_module():
    return Mock()

def test_collect_no_module():
    collector = FacterFactCollector()
    result = collector.collect(module=None)
    assert result == {}

def test_collect_facter_output_none(mock_module):
    collector = FacterFactCollector()
    with patch.object(collector, 'get_facter_output', return_value=None):
        result = collector.collect(module=mock_module)
        assert result == {}

def test_collect_facter_output_invalid_json(mock_module):
    collector = FacterFactCollector()
    with patch.object(collector, 'get_facter_output', return_value='invalid json'):
        result = collector.collect(module=mock_module)
        assert result == {}

def test_collect_facter_output_valid_json(mock_module):
    collector = FacterFactCollector()
    valid_json = '{"key": "value"}'
    with patch.object(collector, 'get_facter_output', return_value=valid_json):
        result = collector.collect(module=mock_module)
        assert result == json.loads(valid_json)
