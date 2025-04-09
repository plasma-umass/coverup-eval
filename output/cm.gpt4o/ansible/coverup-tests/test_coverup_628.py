# file lib/ansible/module_utils/facts/collector.py:58-64
# lines [58, 59, 61, 62, 63]
# branches []

import pytest
from ansible.module_utils.facts.collector import BaseFactCollector

def test_base_fact_collector_initialization():
    collector = BaseFactCollector()
    
    assert collector._fact_ids == set()
    assert collector._platform == 'Generic'
    assert collector.name is None
    assert collector.required_facts == set()
