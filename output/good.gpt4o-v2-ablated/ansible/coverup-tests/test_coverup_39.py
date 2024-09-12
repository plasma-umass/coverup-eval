# file: lib/ansible/module_utils/facts/ansible_collector.py:56-74
# asked: {"lines": [56, 58, 59, 61, 62, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74], "branches": [[58, 59], [58, 61], [61, 62], [61, 64], [65, 66], [65, 74], [66, 65], [66, 67], [67, 68], [67, 69], [69, 66], [69, 71], [72, 66], [72, 73]]}
# gained: {"lines": [56, 58, 59, 61, 62, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74], "branches": [[58, 59], [58, 61], [61, 62], [61, 64], [65, 66], [65, 74], [66, 65], [66, 67], [67, 68], [67, 69], [69, 66], [69, 71], [72, 66], [72, 73]]}

import pytest
import fnmatch
from ansible.module_utils.facts.ansible_collector import AnsibleFactCollector
from ansible.module_utils.common.text.converters import to_text

def is_string(value):
    return isinstance(value, str)

class MockBaseFactCollector:
    pass

@pytest.fixture
def collector(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.facts.ansible_collector.collector.BaseFactCollector', MockBaseFactCollector)
    return AnsibleFactCollector()

def test_filter_no_filter_spec(collector):
    facts_dict = {'ansible_os': 'Linux', 'ansible_version': '2.9'}
    filter_spec = ''
    result = collector._filter(facts_dict, filter_spec)
    assert result == facts_dict

def test_filter_wildcard_filter_spec(collector):
    facts_dict = {'ansible_os': 'Linux', 'ansible_version': '2.9'}
    filter_spec = '*'
    result = collector._filter(facts_dict, filter_spec)
    assert result == facts_dict

def test_filter_string_filter_spec(collector):
    facts_dict = {'ansible_os': 'Linux', 'ansible_version': '2.9'}
    filter_spec = 'ansible_os'
    result = collector._filter(facts_dict, filter_spec)
    assert result == [('ansible_os', 'Linux')]

def test_filter_list_filter_spec(collector):
    facts_dict = {'ansible_os': 'Linux', 'ansible_version': '2.9'}
    filter_spec = ['ansible_os']
    result = collector._filter(facts_dict, filter_spec)
    assert result == [('ansible_os', 'Linux')]

def test_filter_non_matching_filter_spec(collector):
    facts_dict = {'ansible_os': 'Linux', 'ansible_version': '2.9'}
    filter_spec = 'non_matching'
    result = collector._filter(facts_dict, filter_spec)
    assert result == []

def test_filter_with_prefix(collector):
    facts_dict = {'ansible_os': 'Linux', 'ansible_version': '2.9'}
    filter_spec = 'os'
    result = collector._filter(facts_dict, filter_spec)
    assert result == [('ansible_os', 'Linux')]

def test_filter_with_non_ansible_prefix(collector):
    facts_dict = {'facter_os': 'Linux', 'ohai_version': '2.9'}
    filter_spec = 'os'
    result = collector._filter(facts_dict, filter_spec)
    assert result == []

def test_filter_with_empty_filter_spec(collector):
    facts_dict = {'ansible_os': 'Linux', 'ansible_version': '2.9'}
    filter_spec = None
    result = collector._filter(facts_dict, filter_spec)
    assert result == facts_dict
