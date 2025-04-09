# file: lib/ansible/module_utils/facts/collector.py:297-305
# asked: {"lines": [297, 298, 299, 300, 301, 302, 303, 304, 305], "branches": [[299, 300], [299, 305], [301, 302], [301, 304], [302, 301], [302, 303]]}
# gained: {"lines": [297, 298, 299, 300, 301, 302, 303, 304, 305], "branches": [[299, 300], [299, 305], [301, 302], [301, 304], [302, 301], [302, 303]]}

import pytest
from collections import defaultdict

# Assuming the build_dep_data function is imported from ansible/module_utils/facts/collector.py
from ansible.module_utils.facts.collector import build_dep_data

class MockCollector:
    def __init__(self, required_facts):
        self.required_facts = required_facts

def test_build_dep_data():
    collector_names = ['collector1', 'collector2']
    all_fact_subsets = {
        'collector1': [MockCollector(['fact1', 'fact2']), MockCollector(['fact3'])],
        'collector2': [MockCollector(['fact4']), MockCollector(['fact5', 'fact6'])]
    }

    expected_dep_map = {
        'collector1': {'fact1', 'fact2', 'fact3'},
        'collector2': {'fact4', 'fact5', 'fact6'}
    }

    dep_map = build_dep_data(collector_names, all_fact_subsets)
    
    assert dep_map == expected_dep_map

@pytest.fixture(autouse=True)
def run_around_tests():
    # Setup code: runs before each test
    yield
    # Teardown code: runs after each test
    # Clean up any state here if necessary

