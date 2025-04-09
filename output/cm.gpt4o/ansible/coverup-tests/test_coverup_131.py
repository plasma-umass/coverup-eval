# file lib/ansible/module_utils/facts/collector.py:308-327
# lines [308, 309, 311, 313, 314, 315, 316, 317, 318, 320, 321, 322, 324, 325, 327]
# branches ['313->314', '313->327', '315->316', '315->324', '316->317', '316->320', '317->316', '317->318', '324->313', '324->325']

import pytest
from ansible.module_utils.facts.collector import tsort, CycleFoundInFactDeps

def test_tsort_no_cycle():
    dep_map = {
        'a': ['b', 'c'],
        'b': ['c'],
        'c': []
    }
    sorted_list = tsort(dep_map)
    assert sorted_list == [('c', []), ('b', ['c']), ('a', ['b', 'c'])]

def test_tsort_with_cycle():
    dep_map = {
        'a': ['b'],
        'b': ['c'],
        'c': ['a']
    }
    with pytest.raises(CycleFoundInFactDeps) as excinfo:
        tsort(dep_map)
    assert 'Unable to tsort deps, there was a cycle in the graph.' in str(excinfo.value)

def test_tsort_empty():
    dep_map = {}
    sorted_list = tsort(dep_map)
    assert sorted_list == []

def test_tsort_single_node():
    dep_map = {
        'a': []
    }
    sorted_list = tsort(dep_map)
    assert sorted_list == [('a', [])]
