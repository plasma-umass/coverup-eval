# file: lib/ansible/module_utils/facts/ansible_collector.py:56-74
# asked: {"lines": [61, 62, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74], "branches": [[58, 61], [61, 62], [61, 64], [65, 66], [65, 74], [66, 65], [66, 67], [67, 68], [67, 69], [69, 66], [69, 71], [72, 66], [72, 73]]}
# gained: {"lines": [61, 62, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74], "branches": [[58, 61], [61, 62], [61, 64], [65, 66], [65, 74], [66, 65], [66, 67], [67, 68], [67, 69], [69, 71], [72, 66], [72, 73]]}

import pytest
from ansible.module_utils.facts.ansible_collector import AnsibleFactCollector
from ansible.module_utils.common.collections import is_string
import fnmatch

@pytest.fixture
def fact_collector():
    return AnsibleFactCollector()

def test_filter_with_empty_filter_spec(fact_collector):
    facts_dict = {'key1': 'value1', 'key2': 'value2'}
    filter_spec = ''
    result = fact_collector._filter(facts_dict, filter_spec)
    assert result == facts_dict

def test_filter_with_string_filter_spec(fact_collector):
    facts_dict = {'key1': 'value1', 'key2': 'value2'}
    filter_spec = 'key1'
    result = fact_collector._filter(facts_dict, filter_spec)
    assert result == [('key1', 'value1')]

def test_filter_with_list_filter_spec(fact_collector):
    facts_dict = {'key1': 'value1', 'key2': 'value2'}
    filter_spec = ['key1', 'key2']
    result = fact_collector._filter(facts_dict, filter_spec)
    assert result == [('key1', 'value1'), ('key2', 'value2')]

def test_filter_with_fnmatch(fact_collector):
    facts_dict = {'key1': 'value1', 'key2': 'value2'}
    filter_spec = 'key*'
    result = fact_collector._filter(facts_dict, filter_spec)
    assert result == [('key1', 'value1'), ('key2', 'value2')]

def test_filter_with_ansible_prefix(fact_collector):
    facts_dict = {'ansible_key1': 'value1', 'key2': 'value2'}
    filter_spec = 'key1'
    result = fact_collector._filter(facts_dict, filter_spec)
    assert result == [('ansible_key1', 'value1')]

def test_filter_with_non_matching_prefix(fact_collector):
    facts_dict = {'ansible_key1': 'value1', 'key2': 'value2'}
    filter_spec = 'non_matching_key'
    result = fact_collector._filter(facts_dict, filter_spec)
    assert result == []

