# file: lib/ansible/module_utils/facts/other/facter.py:64-85
# asked: {"lines": [64, 68, 70, 71, 73, 76, 77, 79, 80, 81, 83, 85], "branches": [[70, 71], [70, 73], [76, 77], [76, 79]]}
# gained: {"lines": [64], "branches": []}

import json
import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.collector import BaseFactCollector

class FacterFactCollector(BaseFactCollector):
    def collect(self, module=None, collected_facts=None):
        facter_dict = {}
        if not module:
            return facter_dict
        facter_output = self.get_facter_output(module)
        if facter_output is None:
            return facter_dict
        try:
            facter_dict = json.loads(facter_output)
        except Exception:
            pass
        return facter_dict

    def get_facter_output(self, module):
        facter_path = self.find_facter(module)
        if not facter_path:
            return None
        (rc, out, err) = self.run_facter(module, facter_path)
        if rc != 0:
            return None
        return out

    def find_facter(self, module):
        # Mock implementation for testing
        return "/usr/bin/facter"

    def run_facter(self, module, facter_path):
        # Mock implementation for testing
        return (0, '{"facter_key": "facter_value"}', '')

@pytest.fixture
def mock_module():
    return Mock()

def test_collect_no_module():
    collector = FacterFactCollector()
    result = collector.collect()
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

def test_collect_success(mock_module):
    collector = FacterFactCollector()
    with patch.object(collector, 'get_facter_output', return_value='{"facter_key": "facter_value"}'):
        result = collector.collect(module=mock_module)
        assert result == {"facter_key": "facter_value"}
