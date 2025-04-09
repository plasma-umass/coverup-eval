# file: lib/ansible/module_utils/facts/collector.py:330-342
# asked: {"lines": [330, 331, 332, 334, 335, 336, 337, 339, 340, 342], "branches": [[334, 335], [336, 337], [336, 339]]}
# gained: {"lines": [330, 331, 332, 334, 335, 336, 337, 339, 340, 342], "branches": [[334, 335], [336, 337], [336, 339]]}

import pytest
from ansible.module_utils.facts.collector import _solve_deps, find_unresolved_requires, resolve_requires, _get_requires_by_collector_name, UnresolvedFactDep

def test_solve_deps(monkeypatch):
    def mock_find_unresolved_requires(solutions, all_fact_subsets):
        if solutions == {'fact1'}:
            return {'fact2'}
        elif solutions == {'fact1', 'fact2'}:
            return set()
        return set()

    def mock_resolve_requires(unresolved, all_fact_subsets):
        if unresolved == {'fact2'}:
            return {'fact2'}
        return set()

    monkeypatch.setattr('ansible.module_utils.facts.collector.find_unresolved_requires', mock_find_unresolved_requires)
    monkeypatch.setattr('ansible.module_utils.facts.collector.resolve_requires', mock_resolve_requires)

    collector_names = {'fact1'}
    all_fact_subsets = {'fact1', 'fact2'}
    result = _solve_deps(collector_names, all_fact_subsets)
    assert result == {'fact1', 'fact2'}

def test_find_unresolved_requires(monkeypatch):
    def mock_get_requires_by_collector_name(collector_name, all_fact_subsets):
        if collector_name == 'fact1':
            return {'fact2'}
        return set()

    monkeypatch.setattr('ansible.module_utils.facts.collector._get_requires_by_collector_name', mock_get_requires_by_collector_name)

    collector_names = {'fact1'}
    all_fact_subsets = {'fact1', 'fact2'}
    result = find_unresolved_requires(collector_names, all_fact_subsets)
    assert result == {'fact2'}

def test_resolve_requires():
    unresolved_requires = {'fact2'}
    all_fact_subsets = {'fact1', 'fact2'}
    result = resolve_requires(unresolved_requires, all_fact_subsets)
    assert result == {'fact2'}

    unresolved_requires = {'fact3'}
    with pytest.raises(UnresolvedFactDep):
        resolve_requires(unresolved_requires, all_fact_subsets)
