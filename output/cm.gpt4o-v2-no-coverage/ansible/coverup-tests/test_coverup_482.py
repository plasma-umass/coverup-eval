# file: lib/ansible/module_utils/facts/collector.py:254-263
# asked: {"lines": [254, 255, 257, 258, 259, 260, 261, 262, 263], "branches": [[261, 262], [261, 263]]}
# gained: {"lines": [254, 255, 257, 258, 259, 260, 261, 262, 263], "branches": [[261, 262], [261, 263]]}

import pytest
from ansible.module_utils.facts.collector import _get_requires_by_collector_name, CollectorNotFoundError

class MockCollectorClass:
    required_facts = {'fact1', 'fact2'}

def test_get_requires_by_collector_name_success():
    all_fact_subsets = {
        'collector1': [MockCollectorClass]
    }
    result = _get_requires_by_collector_name('collector1', all_fact_subsets)
    assert result == {'fact1', 'fact2'}

def test_get_requires_by_collector_name_collector_not_found():
    all_fact_subsets = {}
    with pytest.raises(CollectorNotFoundError) as excinfo:
        _get_requires_by_collector_name('collector1', all_fact_subsets)
    assert str(excinfo.value) == '\'Fact collector "collector1" not found\''
