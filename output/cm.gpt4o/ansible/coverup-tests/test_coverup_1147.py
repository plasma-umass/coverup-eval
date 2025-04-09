# file lib/ansible/module_utils/facts/collector.py:254-263
# lines [255, 257, 258, 259, 260, 261, 262, 263]
# branches ['261->262', '261->263']

import pytest
from ansible.module_utils.facts.collector import CollectorNotFoundError

class MockCollector:
    required_facts = {'fact1', 'fact2'}

def test_get_requires_by_collector_name(mocker):
    from ansible.module_utils.facts.collector import _get_requires_by_collector_name

    # Mock data
    collector_name = 'test_collector'
    all_fact_subsets = {
        collector_name: [MockCollector]
    }

    # Test when collector_name is found
    required_facts = _get_requires_by_collector_name(collector_name, all_fact_subsets)
    assert required_facts == {'fact1', 'fact2'}

    # Test when collector_name is not found
    with pytest.raises(CollectorNotFoundError) as excinfo:
        _get_requires_by_collector_name('non_existent_collector', all_fact_subsets)
    assert 'Fact collector "non_existent_collector" not found' in str(excinfo.value)
