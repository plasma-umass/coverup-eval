# file lib/ansible/module_utils/facts/collector.py:106-117
# lines [106, 116, 117]
# branches []

import pytest
from ansible.module_utils.facts.collector import BaseFactCollector

# Test function to cover BaseFactCollector.collect
def test_base_fact_collector_collect():
    collector = BaseFactCollector()
    collected_facts = {}
    result = collector.collect(collected_facts=collected_facts)
    assert isinstance(result, dict), "The result should be a dictionary"
    assert result == {}, "The result should be an empty dictionary since BaseFactCollector does not collect any facts"

# Use pytest-mock to ensure isolation and cleanup
def test_base_fact_collector_collect_with_mocker(mocker):
    mocker.patch.object(BaseFactCollector, 'collect', return_value={'mocked_fact': True})
    collector = BaseFactCollector()
    collected_facts = {}
    result = collector.collect(collected_facts=collected_facts)
    assert result == {'mocked_fact': True}, "The result should contain the mocked fact"
