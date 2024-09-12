# file: lib/ansible/module_utils/facts/collector.py:330-342
# asked: {"lines": [331, 332, 334, 335, 336, 337, 339, 340, 342], "branches": [[334, 335], [336, 337], [336, 339]]}
# gained: {"lines": [331, 332, 334, 335, 336, 337, 339, 340, 342], "branches": [[334, 335], [336, 337], [336, 339]]}

import pytest
from ansible.module_utils.facts.collector import _solve_deps, UnresolvedFactDep

def test_solve_deps(monkeypatch):
    def mock_find_unresolved_requires(solutions, all_fact_subsets):
        if 'fact1' in solutions:
            return set()
        return {'fact1'}

    def mock_resolve_requires(unresolved, all_fact_subsets):
        if 'fact1' in unresolved:
            return {'fact1'}
        raise UnresolvedFactDep('unresolved fact dep')

    monkeypatch.setattr('ansible.module_utils.facts.collector.find_unresolved_requires', mock_find_unresolved_requires)
    monkeypatch.setattr('ansible.module_utils.facts.collector.resolve_requires', mock_resolve_requires)

    collector_names = {'fact2'}
    all_fact_subsets = {'fact1': [], 'fact2': []}

    solutions = _solve_deps(collector_names, all_fact_subsets)
    assert solutions == {'fact1', 'fact2'}
