# file: lib/ansible/module_utils/facts/ansible_collector.py:76-100
# asked: {"lines": [76, 77, 79, 81, 82, 84, 87, 88, 89, 90, 91, 95, 98, 100], "branches": [[81, 82], [81, 100]]}
# gained: {"lines": [76, 77, 79, 81, 82, 84, 87, 88, 89, 90, 91, 95, 98, 100], "branches": [[81, 82], [81, 100]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.ansible_collector import AnsibleFactCollector
from ansible.module_utils.facts.collector import BaseFactCollector

class MockCollector(BaseFactCollector):
    def collect_with_namespace(self, module=None, collected_facts=None):
        return {"mock_fact": "value"}

@pytest.fixture
def mock_collectors():
    return [MockCollector()]

@pytest.fixture
def ansible_fact_collector(mock_collectors):
    return AnsibleFactCollector(collectors=mock_collectors)

def test_collect_success(ansible_fact_collector):
    result = ansible_fact_collector.collect()
    assert result == {"mock_fact": "value"}

def test_collect_with_exception(ansible_fact_collector, monkeypatch):
    def mock_collect_with_namespace(module=None, collected_facts=None):
        raise Exception("Test exception")

    ansible_fact_collector.collectors[0].collect_with_namespace = mock_collect_with_namespace

    with patch('sys.stderr.write') as mock_stderr:
        result = ansible_fact_collector.collect()
        assert result == {}
        mock_stderr.assert_any_call("Exception('Test exception')")
        mock_stderr.assert_any_call('\n')
