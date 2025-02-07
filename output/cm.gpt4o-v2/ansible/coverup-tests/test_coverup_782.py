# file: lib/ansible/module_utils/facts/collector.py:106-117
# asked: {"lines": [106, 116, 117], "branches": []}
# gained: {"lines": [106, 116, 117], "branches": []}

import pytest
from ansible.module_utils.facts.collector import BaseFactCollector

def test_collect_method():
    collector = BaseFactCollector()
    result = collector.collect()
    assert isinstance(result, dict)
    assert result == {}

def test_collect_method_with_collected_facts():
    collector = BaseFactCollector()
    collected_facts = {'existing_fact': 'value'}
    result = collector.collect(collected_facts=collected_facts)
    assert isinstance(result, dict)
    assert result == {}
