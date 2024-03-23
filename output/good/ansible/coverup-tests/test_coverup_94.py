# file lib/ansible/module_utils/facts/ansible_collector.py:56-74
# lines [56, 58, 59, 61, 62, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74]
# branches ['58->59', '58->61', '61->62', '61->64', '65->66', '65->74', '66->65', '66->67', '67->68', '67->69', '69->66', '69->71', '72->66', '72->73']

import fnmatch
import pytest
from ansible.module_utils.facts.ansible_collector import AnsibleFactCollector

@pytest.fixture
def ansible_fact_collector():
    return AnsibleFactCollector()

def test_ansible_fact_collector_filter(ansible_fact_collector):
    facts_dict = {
        'ansible_os_family': 'Debian',
        'ansible_distribution': 'Ubuntu',
        'facter_os': 'Linux',
        'ohai_os': 'Linux',
        'custom_fact': 'value1',
        'ansible_custom_fact': 'value2'
    }

    # Test with no filter (should return all facts)
    no_filter_result = ansible_fact_collector._filter(facts_dict, '')
    assert len(no_filter_result) == len(facts_dict)
    assert dict(no_filter_result) == facts_dict

    # Test with wildcard filter (should return all facts)
    wildcard_filter_result = ansible_fact_collector._filter(facts_dict, '*')
    assert len(wildcard_filter_result) == len(facts_dict)
    assert dict(wildcard_filter_result) == facts_dict

    # Test with specific filter (should return matching facts)
    specific_filter_result = ansible_fact_collector._filter(facts_dict, 'ansible_os_family')
    assert len(specific_filter_result) == 1
    assert dict(specific_filter_result) == {'ansible_os_family': 'Debian'}

    # Test with non-ansible prefixed filter (should return matching facts with 'ansible_' prefix added)
    non_prefixed_filter_result = ansible_fact_collector._filter(facts_dict, 'custom_fact')
    assert len(non_prefixed_filter_result) == 2
    assert dict(non_prefixed_filter_result) == {'custom_fact': 'value1', 'ansible_custom_fact': 'value2'}

    # Test with non-ansible prefixed filter that does not match any fact (should return empty list)
    non_matching_filter_result = ansible_fact_collector._filter(facts_dict, 'non_existent_fact')
    assert len(non_matching_filter_result) == 0
    assert dict(non_matching_filter_result) == {}

    # Test with list of filters (should return matching facts for all filters in the list)
    list_filter_result = ansible_fact_collector._filter(facts_dict, ['ansible_os_family', 'facter_os'])
    assert len(list_filter_result) == 2
    assert dict(list_filter_result) == {'ansible_os_family': 'Debian', 'facter_os': 'Linux'}
