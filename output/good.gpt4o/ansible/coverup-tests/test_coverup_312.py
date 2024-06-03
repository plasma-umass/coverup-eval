# file lib/ansible/module_utils/facts/collector.py:223-236
# lines [223, 224, 225, 227, 228, 230, 232, 233, 234, 236]
# branches ['227->228', '227->236', '232->227', '232->233']

import pytest
from collections import defaultdict

# Mock collector class for testing
class MockCollector:
    def __init__(self, name, fact_ids):
        self.name = name
        self._fact_ids = fact_ids

def test_build_fact_id_to_collector_map():
    from ansible.module_utils.facts.collector import build_fact_id_to_collector_map

    # Create mock collectors
    collector1 = MockCollector('collector1', ['fact1', 'fact2'])
    collector2 = MockCollector('collector2', ['fact3'])
    collectors_for_platform = [collector1, collector2]

    # Call the function with the mock collectors
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)

    # Assertions to verify the postconditions
    assert fact_id_to_collector_map['collector1'] == [collector1]
    assert fact_id_to_collector_map['collector2'] == [collector2]
    assert fact_id_to_collector_map['fact1'] == [collector1]
    assert fact_id_to_collector_map['fact2'] == [collector1]
    assert fact_id_to_collector_map['fact3'] == [collector2]

    assert aliases_map['collector1'] == {'fact1', 'fact2'}
    assert aliases_map['collector2'] == {'fact3'}

@pytest.fixture(autouse=True)
def cleanup(mocker):
    # Cleanup code to ensure no side effects on other tests
    yield
    mocker.stopall()
