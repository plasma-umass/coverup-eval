# file lib/ansible/module_utils/facts/collector.py:283-294
# lines [283, 284, 285, 286, 287, 288, 290, 292, 293, 294]
# branches ['286->287', '286->292', '287->288', '287->290', '292->293', '292->294']

import pytest
from ansible.module_utils.facts.collector import UnresolvedFactDep

def test_resolve_requires():
    def resolve_requires(unresolved_requires, all_fact_subsets):
        new_names = set()
        failed = []
        for unresolved in unresolved_requires:
            if unresolved in all_fact_subsets:
                new_names.add(unresolved)
            else:
                failed.append(unresolved)
    
        if failed:
            raise UnresolvedFactDep('unresolved fact dep %s' % ','.join(failed))
        return new_names

    # Test case where all unresolved requires are resolved
    unresolved_requires = ['fact1', 'fact2']
    all_fact_subsets = {'fact1', 'fact2', 'fact3'}
    result = resolve_requires(unresolved_requires, all_fact_subsets)
    assert result == {'fact1', 'fact2'}

    # Test case where some unresolved requires are not resolved
    unresolved_requires = ['fact1', 'fact4']
    all_fact_subsets = {'fact1', 'fact2', 'fact3'}
    with pytest.raises(UnresolvedFactDep) as excinfo:
        resolve_requires(unresolved_requires, all_fact_subsets)
    assert 'unresolved fact dep fact4' in str(excinfo.value)

    # Test case where no unresolved requires are resolved
    unresolved_requires = ['fact4', 'fact5']
    all_fact_subsets = {'fact1', 'fact2', 'fact3'}
    with pytest.raises(UnresolvedFactDep) as excinfo:
        resolve_requires(unresolved_requires, all_fact_subsets)
    assert 'unresolved fact dep fact4,fact5' in str(excinfo.value)
