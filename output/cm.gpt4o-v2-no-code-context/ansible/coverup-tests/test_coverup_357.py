# file: lib/ansible/module_utils/facts/collector.py:254-263
# asked: {"lines": [254, 255, 257, 258, 259, 260, 261, 262, 263], "branches": [[261, 262], [261, 263]]}
# gained: {"lines": [254, 255, 257, 258, 259, 260, 261, 262, 263], "branches": [[261, 262], [261, 263]]}

import pytest
from ansible.module_utils.facts.collector import _get_requires_by_collector_name, CollectorNotFoundError

class MockCollector:
    required_facts = {'fact1', 'fact2'}

def test_get_requires_by_collector_name_success():
    all_fact_subsets = {
        'mock_collector': [MockCollector]
    }
    result = _get_requires_by_collector_name('mock_collector', all_fact_subsets)
    assert result == {'fact1', 'fact2'}

def test_get_requires_by_collector_name_collector_not_found():
    all_fact_subsets = {
        'mock_collector': [MockCollector]
    }
    with pytest.raises(CollectorNotFoundError) as excinfo:
        _get_requires_by_collector_name('non_existent_collector', all_fact_subsets)
    assert 'Fact collector "non_existent_collector" not found' in str(excinfo.value)
