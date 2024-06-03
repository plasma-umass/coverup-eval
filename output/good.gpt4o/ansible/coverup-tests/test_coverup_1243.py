# file lib/ansible/module_utils/facts/collector.py:120-196
# lines [168, 169]
# branches ['167->168']

import pytest
from collections import defaultdict
from ansible.module_utils.facts.collector import get_collector_names

def test_get_collector_names_minimal_gather_subset_exclusion():
    valid_subsets = frozenset(['all', 'network', 'hardware'])
    minimal_gather_subset = frozenset(['min'])
    gather_subset = ['!min']
    aliases_map = defaultdict(set)
    platform_info = None

    result = get_collector_names(valid_subsets=valid_subsets,
                                 minimal_gather_subset=minimal_gather_subset,
                                 gather_subset=gather_subset,
                                 aliases_map=aliases_map,
                                 platform_info=platform_info)

    assert 'min' not in result
    assert 'network' not in result
    assert 'hardware' not in result
    assert result == set()

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
