# file: lib/ansible/module_utils/facts/collector.py:106-117
# asked: {"lines": [106, 116, 117], "branches": []}
# gained: {"lines": [106, 116, 117], "branches": []}

import pytest
from ansible.module_utils.facts.collector import BaseFactCollector

class TestBaseFactCollector:
    
    def test_collect_with_defaults(self):
        collector = BaseFactCollector()
        result = collector.collect()
        assert result == {}, "Expected an empty dictionary when no arguments are provided"

    def test_collect_with_module(self, mocker):
        collector = BaseFactCollector()
        mock_module = mocker.Mock()
        result = collector.collect(module=mock_module)
        assert result == {}, "Expected an empty dictionary when module is provided"

    def test_collect_with_collected_facts(self):
        collector = BaseFactCollector()
        collected_facts = {'existing_fact': 'value'}
        result = collector.collect(collected_facts=collected_facts)
        assert result == {}, "Expected an empty dictionary when collected_facts is provided"
