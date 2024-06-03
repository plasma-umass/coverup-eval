# file lib/ansible/module_utils/facts/collector.py:106-117
# lines [106, 116, 117]
# branches []

import pytest
from ansible.module_utils.facts.collector import BaseFactCollector

def test_base_fact_collector_collect():
    collector = BaseFactCollector()
    collected_facts = {'existing_fact': 'value'}
    
    # Call the collect method
    result = collector.collect(module=None, collected_facts=collected_facts)
    
    # Assert that the result is an empty dictionary
    assert result == {}
    
    # Assert that collected_facts is not modified
    assert collected_facts == {'existing_fact': 'value'}
