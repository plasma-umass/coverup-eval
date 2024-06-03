# file lib/ansible/module_utils/facts/ansible_collector.py:56-74
# lines [56, 58, 59, 61, 62, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74]
# branches ['58->59', '58->61', '61->62', '61->64', '65->66', '65->74', '66->65', '66->67', '67->68', '67->69', '69->66', '69->71', '72->66', '72->73']

import pytest
from unittest.mock import patch
from fnmatch import fnmatch
from ansible.module_utils.facts.ansible_collector import AnsibleFactCollector
from ansible.module_utils.common.collections import is_string

@pytest.fixture
def facts_dict():
    return {
        'ansible_os_family': 'Debian',
        'ansible_distribution': 'Ubuntu',
        'facter_os': 'Linux',
        'ohai_platform': 'ubuntu',
        'custom_fact': 'value'
    }

def test_filter_with_empty_filter_spec(facts_dict):
    collector = AnsibleFactCollector()
    result = collector._filter(facts_dict, '')
    assert result == facts_dict

def test_filter_with_wildcard_filter_spec(facts_dict):
    collector = AnsibleFactCollector()
    result = collector._filter(facts_dict, '*')
    assert result == facts_dict

def test_filter_with_specific_filter_spec(facts_dict):
    collector = AnsibleFactCollector()
    result = collector._filter(facts_dict, 'ansible_os_family')
    assert result == [('ansible_os_family', 'Debian')]

def test_filter_with_list_filter_spec(facts_dict):
    collector = AnsibleFactCollector()
    result = collector._filter(facts_dict, ['ansible_os_family', 'facter_os'])
    assert result == [('ansible_os_family', 'Debian'), ('facter_os', 'Linux')]

def test_filter_with_non_matching_filter_spec(facts_dict):
    collector = AnsibleFactCollector()
    result = collector._filter(facts_dict, 'non_existent_fact')
    assert result == []

def test_filter_with_prefix_matching(facts_dict):
    collector = AnsibleFactCollector()
    result = collector._filter(facts_dict, 'distribution')
    assert result == [('ansible_distribution', 'Ubuntu')]

def test_filter_with_non_ansible_prefix(facts_dict):
    collector = AnsibleFactCollector()
    result = collector._filter(facts_dict, 'custom_fact')
    assert result == [('custom_fact', 'value')]
