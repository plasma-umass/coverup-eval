# file: lib/ansible/module_utils/facts/collector.py:308-327
# asked: {"lines": [308, 309, 311, 313, 314, 315, 316, 317, 318, 320, 321, 322, 324, 325, 327], "branches": [[313, 314], [313, 327], [315, 316], [315, 324], [316, 317], [316, 320], [317, 316], [317, 318], [324, 313], [324, 325]]}
# gained: {"lines": [308, 309, 311, 313, 314, 315, 316, 317, 318, 320, 321, 322, 324, 325, 327], "branches": [[313, 314], [313, 327], [315, 316], [315, 324], [316, 317], [316, 320], [317, 316], [317, 318], [324, 313], [324, 325]]}

import pytest
from ansible.module_utils.facts.collector import tsort, CycleFoundInFactDeps

def test_tsort_no_dependencies():
    dep_map = {
        'a': [],
        'b': [],
        'c': []
    }
    result = tsort(dep_map)
    assert result == [('a', []), ('b', []), ('c', [])]

def test_tsort_linear_dependencies():
    dep_map = {
        'a': ['b'],
        'b': ['c'],
        'c': []
    }
    result = tsort(dep_map)
    assert result == [('c', []), ('b', ['c']), ('a', ['b'])]

def test_tsort_branching_dependencies():
    dep_map = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['d'],
        'd': []
    }
    result = tsort(dep_map)
    assert result == [('d', []), ('b', ['d']), ('c', ['d']), ('a', ['b', 'c'])]

def test_tsort_cycle_detection():
    dep_map = {
        'a': ['b'],
        'b': ['c'],
        'c': ['a']
    }
    with pytest.raises(CycleFoundInFactDeps) as excinfo:
        tsort(dep_map)
    assert 'Unable to tsort deps, there was a cycle in the graph' in str(excinfo.value)

def test_tsort_complex_graph():
    dep_map = {
        'a': ['b', 'c'],
        'b': ['d', 'e'],
        'c': ['f'],
        'd': [],
        'e': ['f'],
        'f': []
    }
    result = tsort(dep_map)
    expected_result = [
        ('d', []),
        ('f', []),
        ('e', ['f']),
        ('b', ['d', 'e']),
        ('c', ['f']),
        ('a', ['b', 'c'])
    ]
    assert sorted(result) == sorted(expected_result)
