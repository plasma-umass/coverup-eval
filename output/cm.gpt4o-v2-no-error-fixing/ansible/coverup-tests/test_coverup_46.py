# file: lib/ansible/module_utils/facts/ansible_collector.py:56-74
# asked: {"lines": [56, 58, 59, 61, 62, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74], "branches": [[58, 59], [58, 61], [61, 62], [61, 64], [65, 66], [65, 74], [66, 65], [66, 67], [67, 68], [67, 69], [69, 66], [69, 71], [72, 66], [72, 73]]}
# gained: {"lines": [56, 58, 59, 61, 62, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74], "branches": [[58, 59], [58, 61], [61, 62], [61, 64], [65, 66], [65, 74], [66, 65], [66, 67], [67, 68], [67, 69], [69, 71], [72, 66], [72, 73]]}

import pytest
from ansible.module_utils.facts.ansible_collector import AnsibleFactCollector

@pytest.fixture
def fact_collector():
    return AnsibleFactCollector()

def test_filter_no_filter_spec(fact_collector):
    facts_dict = {'key1': 'value1', 'key2': 'value2'}
    result = fact_collector._filter(facts_dict, '')
    assert result == facts_dict

def test_filter_wildcard_filter_spec(fact_collector):
    facts_dict = {'key1': 'value1', 'key2': 'value2'}
    result = fact_collector._filter(facts_dict, '*')
    assert result == facts_dict

def test_filter_string_filter_spec(fact_collector):
    facts_dict = {'key1': 'value1', 'key2': 'value2'}
    result = fact_collector._filter(facts_dict, 'key1')
    assert result == [('key1', 'value1')]

def test_filter_list_filter_spec(fact_collector):
    facts_dict = {'key1': 'value1', 'key2': 'value2'}
    result = fact_collector._filter(facts_dict, ['key1', 'key2'])
    assert result == [('key1', 'value1'), ('key2', 'value2')]

def test_filter_with_prefix(fact_collector):
    facts_dict = {'ansible_key1': 'value1', 'key2': 'value2'}
    result = fact_collector._filter(facts_dict, 'key1')
    assert result == [('ansible_key1', 'value1')]

def test_filter_with_non_matching_prefix(fact_collector):
    facts_dict = {'facter_key1': 'value1', 'key2': 'value2'}
    result = fact_collector._filter(facts_dict, 'key1')
    assert result == []

def test_filter_with_empty_filter(fact_collector):
    facts_dict = {'key1': 'value1', 'key2': 'value2'}
    result = fact_collector._filter(facts_dict, [''])
    assert result == [('key1', 'value1'), ('key2', 'value2')]
