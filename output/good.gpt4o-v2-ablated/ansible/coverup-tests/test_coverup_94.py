# file: lib/ansible/module_utils/facts/other/facter.py:64-85
# asked: {"lines": [64, 68, 70, 71, 73, 76, 77, 79, 80, 81, 83, 85], "branches": [[70, 71], [70, 73], [76, 77], [76, 79]]}
# gained: {"lines": [64, 68, 70, 71, 73, 76, 77, 79, 80, 81, 83, 85], "branches": [[70, 71], [70, 73], [76, 77], [76, 79]]}

import pytest
import json
from ansible.module_utils.facts.other.facter import FacterFactCollector
from unittest.mock import Mock, patch

@pytest.fixture
def facter_collector():
    return FacterFactCollector()

def test_collect_no_module(facter_collector):
    result = facter_collector.collect(module=None)
    assert result == {}

def test_collect_facter_output_none(facter_collector):
    module = Mock()
    with patch.object(FacterFactCollector, 'get_facter_output', return_value=None):
        result = facter_collector.collect(module=module)
        assert result == {}

def test_collect_facter_output_invalid_json(facter_collector):
    module = Mock()
    with patch.object(FacterFactCollector, 'get_facter_output', return_value='invalid json'):
        result = facter_collector.collect(module=module)
        assert result == {}

def test_collect_facter_output_valid_json(facter_collector):
    module = Mock()
    facter_output = '{"key": "value"}'
    with patch.object(FacterFactCollector, 'get_facter_output', return_value=facter_output):
        result = facter_collector.collect(module=module)
        assert result == {"key": "value"}
