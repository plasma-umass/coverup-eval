# file: lib/ansible/module_utils/facts/other/facter.py:64-85
# asked: {"lines": [64, 68, 70, 71, 73, 76, 77, 79, 80, 81, 83, 85], "branches": [[70, 71], [70, 73], [76, 77], [76, 79]]}
# gained: {"lines": [64, 68, 70, 71, 73, 76, 77, 79, 80, 81, 83, 85], "branches": [[70, 71], [70, 73], [76, 77], [76, 79]]}

import pytest
import json
from ansible.module_utils.facts.other.facter import FacterFactCollector

class MockModule:
    def run_command(self, command):
        if command == 'facter --json':
            return 0, '{"key": "value"}', ''
        elif command == 'facter --json fail':
            return 1, '', 'error'
        return 0, '', ''

@pytest.fixture
def mock_module():
    return MockModule()

def test_collect_no_module():
    collector = FacterFactCollector()
    result = collector.collect()
    assert result == {}

def test_collect_facter_output_none(monkeypatch, mock_module):
    def mock_get_facter_output(self, module):
        return None

    monkeypatch.setattr(FacterFactCollector, 'get_facter_output', mock_get_facter_output)
    collector = FacterFactCollector()
    result = collector.collect(module=mock_module)
    assert result == {}

def test_collect_facter_output_valid(monkeypatch, mock_module):
    def mock_get_facter_output(self, module):
        return '{"key": "value"}'

    monkeypatch.setattr(FacterFactCollector, 'get_facter_output', mock_get_facter_output)
    collector = FacterFactCollector()
    result = collector.collect(module=mock_module)
    assert result == {"key": "value"}

def test_collect_facter_output_invalid_json(monkeypatch, mock_module):
    def mock_get_facter_output(self, module):
        return 'invalid json'

    monkeypatch.setattr(FacterFactCollector, 'get_facter_output', mock_get_facter_output)
    collector = FacterFactCollector()
    result = collector.collect(module=mock_module)
    assert result == {}
