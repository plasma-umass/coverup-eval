# file: lib/ansible/module_utils/facts/collector.py:106-117
# asked: {"lines": [106, 116, 117], "branches": []}
# gained: {"lines": [106, 116, 117], "branches": []}

import pytest
from ansible.module_utils.facts.collector import BaseFactCollector

def test_collect_returns_empty_dict():
    collector = BaseFactCollector()
    result = collector.collect()
    assert result == {}

def test_collect_with_module_and_collected_facts():
    collector = BaseFactCollector()
    module = object()  # Mock or create a dummy module object
    collected_facts = {'existing_fact': 'value'}
    result = collector.collect(module=module, collected_facts=collected_facts)
    assert result == {}
