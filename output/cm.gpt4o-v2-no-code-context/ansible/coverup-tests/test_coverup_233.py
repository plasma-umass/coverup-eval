# file: lib/ansible/module_utils/facts/collector.py:297-305
# asked: {"lines": [297, 298, 299, 300, 301, 302, 303, 304, 305], "branches": [[299, 300], [299, 305], [301, 302], [301, 304], [302, 301], [302, 303]]}
# gained: {"lines": [297, 298, 299, 300, 301, 302, 303, 304, 305], "branches": [[299, 300], [299, 305], [301, 302], [301, 304], [302, 301], [302, 303]]}

import pytest
from collections import defaultdict

# Assuming the build_dep_data function is imported from the module
from ansible.module_utils.facts.collector import build_dep_data

class MockCollector:
    def __init__(self, required_facts):
        self.required_facts = required_facts

@pytest.fixture
def mock_all_fact_subsets():
    return {
        'collector1': [MockCollector(['fact1', 'fact2']), MockCollector(['fact3'])],
        'collector2': [MockCollector(['fact4'])],
        'collector3': [MockCollector([])]
    }

def test_build_dep_data(mock_all_fact_subsets):
    collector_names = ['collector1', 'collector2', 'collector3']
    dep_map = build_dep_data(collector_names, mock_all_fact_subsets)
    
    assert dep_map == {
        'collector1': {'fact1', 'fact2', 'fact3'},
        'collector2': {'fact4'},
        'collector3': set()
    }
