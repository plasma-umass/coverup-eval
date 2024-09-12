# file: lib/ansible/module_utils/facts/collector.py:106-117
# asked: {"lines": [106, 116, 117], "branches": []}
# gained: {"lines": [106, 116, 117], "branches": []}

import pytest
from ansible.module_utils.facts.collector import BaseFactCollector

@pytest.fixture
def base_fact_collector():
    return BaseFactCollector()

def test_collect_returns_empty_dict(base_fact_collector):
    result = base_fact_collector.collect()
    assert result == {}

def test_collect_with_module(base_fact_collector):
    module = object()  # Mock module object
    result = base_fact_collector.collect(module=module)
    assert result == {}

def test_collect_with_collected_facts(base_fact_collector):
    collected_facts = {'existing_fact': 'value'}
    result = base_fact_collector.collect(collected_facts=collected_facts)
    assert result == {}

def test_collect_with_module_and_collected_facts(base_fact_collector):
    module = object()  # Mock module object
    collected_facts = {'existing_fact': 'value'}
    result = base_fact_collector.collect(module=module, collected_facts=collected_facts)
    assert result == {}
