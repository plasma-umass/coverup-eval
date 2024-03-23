# file lib/ansible/module_utils/facts/collector.py:297-305
# lines [298, 299, 300, 301, 302, 303, 304, 305]
# branches ['299->300', '299->305', '301->302', '301->304', '302->301', '302->303']

import pytest
from collections import defaultdict
from unittest.mock import MagicMock

# Assuming the Collector class and required_facts attribute exist in the module
# If they don't, they will need to be created or mocked accordingly

class FakeCollector:
    def __init__(self, required_facts):
        self.required_facts = required_facts

@pytest.fixture
def cleanup():
    # Setup code if necessary
    yield
    # Cleanup code if necessary

def test_build_dep_data(cleanup):
    from ansible.module_utils.facts.collector import build_dep_data

    # Mocking the all_fact_subsets with required dependencies
    all_fact_subsets = {
        'network': [FakeCollector(['interfaces', 'dns'])],
        'hardware': [FakeCollector(['memory', 'cpu'])]
    }
    collector_names = ['network', 'hardware']

    expected_dep_map = defaultdict(set, {
        'network': {'interfaces', 'dns'},
        'hardware': {'memory', 'cpu'}
    })

    dep_map = build_dep_data(collector_names, all_fact_subsets)

    assert dep_map == expected_dep_map
    # No cleanup needed if no external state is changed
