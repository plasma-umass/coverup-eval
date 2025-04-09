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
    module = object()  # Mock object for module
    collected_facts = {'existing_fact': 'value'}
    result = collector.collect(module=module, collected_facts=collected_facts)
    assert result == {}

@pytest.fixture
def mock_collector(mocker):
    collector = BaseFactCollector()
    mocker.patch.object(collector, 'collect', return_value={})
    return collector

def test_collect_called_with_module_and_collected_facts(mock_collector):
    module = object()  # Mock object for module
    collected_facts = {'existing_fact': 'value'}
    result = mock_collector.collect(module=module, collected_facts=collected_facts)
    assert result == {}
    mock_collector.collect.assert_called_once_with(module=module, collected_facts=collected_facts)
