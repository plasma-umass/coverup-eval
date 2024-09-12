# file: lib/ansible/module_utils/facts/collector.py:266-280
# asked: {"lines": [], "branches": [[277, 276]]}
# gained: {"lines": [], "branches": [[277, 276]]}

import pytest
from ansible.module_utils.facts.collector import find_unresolved_requires, CollectorNotFoundError

class MockCollectorClass:
    def __init__(self, required_facts):
        self.required_facts = required_facts

def test_find_unresolved_requires():
    all_fact_subsets = {
        'collector1': [MockCollectorClass(['fact1', 'fact2'])],
        'collector2': [MockCollectorClass(['fact3'])],
        'collector3': [MockCollectorClass(['fact4', 'fact5'])],
    }

    collector_names = ['collector1', 'collector2']
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    
    assert unresolved == {'fact1', 'fact2', 'fact3'}

    collector_names = ['collector1', 'collector2', 'collector3']
    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    
    assert unresolved == {'fact1', 'fact2', 'fact3', 'fact4', 'fact5'}

    collector_names = ['collector1', 'collector2', 'fact1', 'fact2', 'fact3']
    with pytest.raises(CollectorNotFoundError):
        find_unresolved_requires(collector_names, all_fact_subsets)
