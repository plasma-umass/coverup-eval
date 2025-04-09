# file: lib/ansible/module_utils/facts/collector.py:283-294
# asked: {"lines": [283, 284, 285, 286, 287, 288, 290, 292, 293, 294], "branches": [[286, 287], [286, 292], [287, 288], [287, 290], [292, 293], [292, 294]]}
# gained: {"lines": [283, 284, 285, 286, 287, 288, 290, 292, 293, 294], "branches": [[286, 287], [286, 292], [287, 288], [287, 290], [292, 293], [292, 294]]}

import pytest
from ansible.module_utils.facts.collector import resolve_requires, UnresolvedFactDep

def test_resolve_requires_all_resolved():
    unresolved_requires = ['fact1', 'fact2']
    all_fact_subsets = {'fact1', 'fact2', 'fact3'}
    result = resolve_requires(unresolved_requires, all_fact_subsets)
    assert result == {'fact1', 'fact2'}

def test_resolve_requires_some_unresolved():
    unresolved_requires = ['fact1', 'fact4']
    all_fact_subsets = {'fact1', 'fact2', 'fact3'}
    with pytest.raises(UnresolvedFactDep) as excinfo:
        resolve_requires(unresolved_requires, all_fact_subsets)
    assert 'unresolved fact dep fact4' in str(excinfo.value)

def test_resolve_requires_none_resolved():
    unresolved_requires = ['fact4', 'fact5']
    all_fact_subsets = {'fact1', 'fact2', 'fact3'}
    with pytest.raises(UnresolvedFactDep) as excinfo:
        resolve_requires(unresolved_requires, all_fact_subsets)
    assert 'unresolved fact dep fact4,fact5' in str(excinfo.value)
