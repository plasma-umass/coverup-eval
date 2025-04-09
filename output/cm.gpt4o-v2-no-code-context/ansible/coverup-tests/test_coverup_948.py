# file: lib/ansible/module_utils/facts/ansible_collector.py:56-74
# asked: {"lines": [61, 62, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74], "branches": [[58, 61], [61, 62], [61, 64], [65, 66], [65, 74], [66, 65], [66, 67], [67, 68], [67, 69], [69, 66], [69, 71], [72, 66], [72, 73]]}
# gained: {"lines": [61, 62, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74], "branches": [[58, 61], [61, 62], [61, 64], [65, 66], [65, 74], [66, 65], [66, 67], [67, 68], [67, 69], [69, 71], [72, 66], [72, 73]]}

import pytest
from ansible.module_utils.facts.ansible_collector import AnsibleFactCollector
from ansible.module_utils.facts.collector import BaseFactCollector
import fnmatch

class TestAnsibleFactCollector:
    @pytest.fixture
    def collector(self):
        return AnsibleFactCollector()

    def test_filter_with_empty_filter_spec(self, collector):
        facts_dict = {'key1': 'value1', 'key2': 'value2'}
        filter_spec = ''
        result = collector._filter(facts_dict, filter_spec)
        assert result == facts_dict

    def test_filter_with_wildcard_filter_spec(self, collector):
        facts_dict = {'key1': 'value1', 'key2': 'value2'}
        filter_spec = '*'
        result = collector._filter(facts_dict, filter_spec)
        assert result == facts_dict

    def test_filter_with_string_filter_spec(self, collector):
        facts_dict = {'key1': 'value1', 'key2': 'value2'}
        filter_spec = 'key1'
        result = collector._filter(facts_dict, filter_spec)
        assert result == [('key1', 'value1')]

    def test_filter_with_list_filter_spec(self, collector):
        facts_dict = {'key1': 'value1', 'key2': 'value2'}
        filter_spec = ['key1']
        result = collector._filter(facts_dict, filter_spec)
        assert result == [('key1', 'value1')]

    def test_filter_with_non_matching_filter_spec(self, collector):
        facts_dict = {'key1': 'value1', 'key2': 'value2'}
        filter_spec = 'non_matching_key'
        result = collector._filter(facts_dict, filter_spec)
        assert result == []

    def test_filter_with_prefix_matching_filter_spec(self, collector):
        facts_dict = {'ansible_key1': 'value1', 'key2': 'value2'}
        filter_spec = 'key1'
        result = collector._filter(facts_dict, filter_spec)
        assert result == [('ansible_key1', 'value1')]

    def test_filter_with_non_ansible_prefix(self, collector):
        facts_dict = {'facter_key1': 'value1', 'ohai_key2': 'value2'}
        filter_spec = 'key1'
        result = collector._filter(facts_dict, filter_spec)
        assert result == []

    def test_filter_with_mixed_prefixes(self, collector):
        facts_dict = {'ansible_key1': 'value1', 'facter_key2': 'value2', 'key3': 'value3'}
        filter_spec = 'key1'
        result = collector._filter(facts_dict, filter_spec)
        assert result == [('ansible_key1', 'value1')]

    def test_filter_with_multiple_filters(self, collector):
        facts_dict = {'ansible_key1': 'value1', 'facter_key2': 'value2', 'key3': 'value3'}
        filter_spec = ['key1', 'key3']
        result = collector._filter(facts_dict, filter_spec)
        assert result == [('ansible_key1', 'value1'), ('key3', 'value3')]
