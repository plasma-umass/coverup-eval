# file lib/ansible/module_utils/facts/collector.py:308-327
# lines [308, 309, 311, 313, 314, 315, 316, 317, 318, 320, 321, 322, 324, 325, 327]
# branches ['313->314', '313->327', '315->316', '315->324', '316->317', '316->320', '317->316', '317->318', '324->313', '324->325']

import pytest
from ansible.module_utils.facts.collector import CycleFoundInFactDeps, tsort

def test_tsort_with_no_cycles(mocker):
    dep_map = {
        'node1': ['node2'],
        'node2': [],
        'node3': ['node1'],
    }
    expected_sorted_list = [('node2', []), ('node1', ['node2']), ('node3', ['node1'])]
    sorted_list = tsort(dep_map)
    assert sorted_list == expected_sorted_list

def test_tsort_with_cycle(mocker):
    dep_map = {
        'node1': ['node2'],
        'node2': ['node3'],
        'node3': ['node1'],
    }
    with pytest.raises(CycleFoundInFactDeps):
        tsort(dep_map)

# No cleanup is necessary for these tests as they do not modify any external state.
