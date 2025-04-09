# file lib/ansible/module_utils/facts/collector.py:254-263
# lines [254, 255, 257, 258, 259, 260, 261, 262, 263]
# branches ['261->262', '261->263']

import pytest
from ansible.module_utils.facts.collector import CollectorNotFoundError

# Assuming the existence of a Collector class with a required_facts attribute
class MockCollector:
    required_facts = {'fact1', 'fact2'}

@pytest.fixture
def all_fact_subsets():
    return {'test_collector': [MockCollector]}

def test_get_requires_by_collector_name_success(all_fact_subsets):
    from ansible.module_utils.facts.collector import _get_requires_by_collector_name
    required_facts = _get_requires_by_collector_name('test_collector', all_fact_subsets)
    
    assert required_facts == {'fact1', 'fact2'}

def test_get_requires_by_collector_name_not_found(all_fact_subsets):
    from ansible.module_utils.facts.collector import _get_requires_by_collector_name
    with pytest.raises(CollectorNotFoundError):
        _get_requires_by_collector_name('nonexistent_collector', all_fact_subsets)
