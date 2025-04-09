# file: lib/ansible/module_utils/facts/collector.py:308-327
# asked: {"lines": [308, 309, 311, 313, 314, 315, 316, 317, 318, 320, 321, 322, 324, 325, 327], "branches": [[313, 314], [313, 327], [315, 316], [315, 324], [316, 317], [316, 320], [317, 316], [317, 318], [324, 313], [324, 325]]}
# gained: {"lines": [308, 309, 311, 313, 314, 315, 316, 317, 318, 320, 321, 322, 324, 325, 327], "branches": [[313, 314], [313, 327], [315, 316], [315, 324], [316, 317], [316, 320], [317, 316], [317, 318], [324, 313], [324, 325]]}

import pytest
from ansible.module_utils.facts.collector import tsort, CycleFoundInFactDeps

def test_tsort_no_cycle():
    dep_map = {
        'A': ['B', 'C'],
        'B': ['C'],
        'C': []
    }
    result = tsort(dep_map)
    assert result == [('C', []), ('B', ['C']), ('A', ['B', 'C'])]

def test_tsort_with_cycle():
    dep_map = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }
    with pytest.raises(CycleFoundInFactDeps) as excinfo:
        tsort(dep_map)
    assert 'Unable to tsort deps, there was a cycle in the graph' in str(excinfo.value)

def test_tsort_empty():
    dep_map = {}
    result = tsort(dep_map)
    assert result == []

def test_tsort_single_node():
    dep_map = {
        'A': []
    }
    result = tsort(dep_map)
    assert result == [('A', [])]
