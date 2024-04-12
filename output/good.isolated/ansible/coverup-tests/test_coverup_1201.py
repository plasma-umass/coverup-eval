# file lib/ansible/module_utils/facts/collector.py:283-294
# lines [284, 285, 286, 287, 288, 290, 292, 293, 294]
# branches ['286->287', '286->292', '287->288', '287->290', '292->293', '292->294']

import pytest
from ansible.module_utils.facts.collector import resolve_requires, UnresolvedFactDep

def test_resolve_requires_success(mocker):
    all_fact_subsets = {'network', 'virtual', 'hardware'}
    unresolved_requires = {'network', 'virtual'}
    
    result = resolve_requires(unresolved_requires, all_fact_subsets)
    
    assert result == {'network', 'virtual'}, "The resolved fact subsets should match the expected ones."

def test_resolve_requires_failure(mocker):
    all_fact_subsets = {'network', 'virtual', 'hardware'}
    unresolved_requires = {'network', 'nonexistent'}
    
    with pytest.raises(UnresolvedFactDep) as excinfo:
        resolve_requires(unresolved_requires, all_fact_subsets)
    
    assert 'unresolved fact dep nonexistent' in str(excinfo.value), "The exception message should contain the unresolved fact dep."

# Run the tests
def run_tests():
    test_resolve_requires_success(mocker)
    test_resolve_requires_failure(mocker)

if __name__ == "__main__":
    run_tests()
