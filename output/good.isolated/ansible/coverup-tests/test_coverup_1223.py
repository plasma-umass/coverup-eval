# file lib/ansible/module_utils/facts/collector.py:223-236
# lines [224, 225, 227, 228, 230, 232, 233, 234, 236]
# branches ['227->228', '227->236', '232->227', '232->233']

import pytest
from collections import defaultdict
from ansible.module_utils.facts.collector import build_fact_id_to_collector_map

class MockCollector:
    name = 'mock_collector'
    _fact_ids = ['fact_id_1', 'fact_id_2']

@pytest.fixture
def collectors_for_platform():
    return [MockCollector]

def test_build_fact_id_to_collector_map(collectors_for_platform):
    fact_id_to_collector_map, aliases_map = build_fact_id_to_collector_map(collectors_for_platform)

    assert 'mock_collector' in fact_id_to_collector_map
    assert MockCollector in fact_id_to_collector_map['mock_collector']
    assert 'fact_id_1' in fact_id_to_collector_map
    assert MockCollector in fact_id_to_collector_map['fact_id_1']
    assert 'fact_id_2' in fact_id_to_collector_map
    assert MockCollector in fact_id_to_collector_map['fact_id_2']
    assert 'fact_id_1' in aliases_map['mock_collector']
    assert 'fact_id_2' in aliases_map['mock_collector']
