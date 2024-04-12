# file lib/ansible/module_utils/facts/collector.py:120-196
# lines [163, 164, 168, 169, 171, 172, 192]
# branches ['162->163', '167->168', '170->171', '191->192']

import pytest
from collections import defaultdict
from ansible.module_utils.facts.collector import get_collector_names

def test_get_collector_names_full_coverage(mocker):
    # Mocking the defaultdict to return a specific set when a key is accessed
    aliases_map = defaultdict(set, {'network': {'eth0', 'wlan0'}, 'hardware': {'cpu', 'memory'}})

    # Define the valid subsets and minimal gather subset
    valid_subsets = frozenset(['network', 'hardware', 'virtual', 'all'])
    minimal_gather_subset = frozenset(['network'])

    # Test case to cover line 163-164
    gather_subset = ['all']
    result = get_collector_names(valid_subsets=valid_subsets,
                                 minimal_gather_subset=minimal_gather_subset,
                                 gather_subset=gather_subset,
                                 aliases_map=aliases_map)
    assert valid_subsets.issubset(result)

    # Test case to cover line 168-169
    gather_subset = ['!min']
    result = get_collector_names(valid_subsets=valid_subsets,
                                 minimal_gather_subset=minimal_gather_subset,
                                 gather_subset=gather_subset,
                                 aliases_map=aliases_map)
    assert minimal_gather_subset.isdisjoint(result)

    # Test case to cover line 171-172
    gather_subset = ['!all']
    result = get_collector_names(valid_subsets=valid_subsets,
                                 minimal_gather_subset=minimal_gather_subset,
                                 gather_subset=gather_subset,
                                 aliases_map=aliases_map)
    assert (valid_subsets - minimal_gather_subset).isdisjoint(result)

    # Test case to cover line 192
    gather_subset = []
    result = get_collector_names(valid_subsets=valid_subsets,
                                 minimal_gather_subset=minimal_gather_subset,
                                 gather_subset=gather_subset,
                                 aliases_map=aliases_map)
    assert valid_subsets.issubset(result)

    # Test case to cover TypeError exception
    with pytest.raises(TypeError):
        gather_subset = ['unknown']
        get_collector_names(valid_subsets=valid_subsets,
                            minimal_gather_subset=minimal_gather_subset,
                            gather_subset=gather_subset,
                            aliases_map=aliases_map)
