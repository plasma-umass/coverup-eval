# file: lib/ansible/module_utils/facts/ansible_collector.py:76-100
# asked: {"lines": [76, 77, 79, 81, 82, 84, 87, 88, 89, 90, 91, 95, 98, 100], "branches": [[81, 82], [81, 100]]}
# gained: {"lines": [76, 77, 79, 81, 82, 84, 87, 88, 89, 90, 91, 95, 98, 100], "branches": [[81, 82], [81, 100]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.ansible_collector import AnsibleFactCollector

class MockCollector:
    def collect_with_namespace(self, module=None, collected_facts=None):
        return {"mock_fact": "value"}

def test_collect_with_collectors():
    mock_collector = MockCollector()
    collector = AnsibleFactCollector(collectors=[mock_collector])
    
    with patch('ansible.module_utils.facts.ansible_collector.sys.stderr.write') as mock_stderr:
        result = collector.collect()
    
    assert result == {"mock_fact": "value"}
    assert mock_stderr.call_count == 0

def test_collect_with_exception():
    mock_collector = MockCollector()
    mock_collector.collect_with_namespace = Mock(side_effect=Exception("Test exception"))
    collector = AnsibleFactCollector(collectors=[mock_collector])
    
    with patch('ansible.module_utils.facts.ansible_collector.sys.stderr.write') as mock_stderr:
        result = collector.collect()
    
    assert result == {}
    mock_stderr.assert_any_call("Exception('Test exception')")
    mock_stderr.assert_any_call('\n')
