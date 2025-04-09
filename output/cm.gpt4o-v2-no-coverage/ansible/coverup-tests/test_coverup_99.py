# file: lib/ansible/module_utils/facts/ansible_collector.py:56-74
# asked: {"lines": [56, 58, 59, 61, 62, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74], "branches": [[58, 59], [58, 61], [61, 62], [61, 64], [65, 66], [65, 74], [66, 65], [66, 67], [67, 68], [67, 69], [69, 66], [69, 71], [72, 66], [72, 73]]}
# gained: {"lines": [56, 58, 59, 61, 62, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74], "branches": [[58, 59], [58, 61], [61, 62], [61, 64], [65, 66], [65, 74], [66, 65], [66, 67], [67, 68], [67, 69], [69, 66], [69, 71], [72, 66], [72, 73]]}

import pytest
from ansible.module_utils.facts.ansible_collector import AnsibleFactCollector
from ansible.module_utils.common.collections import is_string

@pytest.fixture
def fact_collector():
    return AnsibleFactCollector()

def test_filter_with_empty_filter_spec(fact_collector):
    facts_dict = {'ansible_os': 'Linux', 'ansible_memory': '8GB'}
    filter_spec = ''
    result = fact_collector._filter(facts_dict, filter_spec)
    assert result == facts_dict

def test_filter_with_wildcard_filter_spec(fact_collector):
    facts_dict = {'ansible_os': 'Linux', 'ansible_memory': '8GB'}
    filter_spec = '*'
    result = fact_collector._filter(facts_dict, filter_spec)
    assert result == facts_dict

def test_filter_with_specific_filter_spec(fact_collector):
    facts_dict = {'ansible_os': 'Linux', 'ansible_memory': '8GB'}
    filter_spec = 'ansible_os'
    result = fact_collector._filter(facts_dict, filter_spec)
    assert result == [('ansible_os', 'Linux')]

def test_filter_with_non_matching_filter_spec(fact_collector):
    facts_dict = {'ansible_os': 'Linux', 'ansible_memory': '8GB'}
    filter_spec = 'non_matching'
    result = fact_collector._filter(facts_dict, filter_spec)
    assert result == []

def test_filter_with_prefix_matching_filter_spec(fact_collector):
    facts_dict = {'ansible_os': 'Linux', 'ansible_memory': '8GB'}
    filter_spec = 'os'
    result = fact_collector._filter(facts_dict, filter_spec)
    assert result == [('ansible_os', 'Linux')]

def test_filter_with_multiple_filter_specs(fact_collector):
    facts_dict = {'ansible_os': 'Linux', 'ansible_memory': '8GB', 'facter_os': 'Linux'}
    filter_spec = ['ansible_os', 'facter_os']
    result = fact_collector._filter(facts_dict, filter_spec)
    assert result == [('ansible_os', 'Linux'), ('facter_os', 'Linux')]

def test_is_string():
    assert is_string('test') is True
    assert is_string(b'test') is True
    assert is_string(123) is False
    assert is_string(['test']) is False
