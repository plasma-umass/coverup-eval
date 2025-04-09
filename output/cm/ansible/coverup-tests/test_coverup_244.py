# file lib/ansible/module_utils/facts/collector.py:283-294
# lines [283, 284, 285, 286, 287, 288, 290, 292, 293, 294]
# branches ['286->287', '286->292', '287->288', '287->290', '292->293', '292->294']

import pytest
from ansible.module_utils.facts.collector import UnresolvedFactDep

# Assuming the existence of the UnresolvedFactDep exception in the module
# If it doesn't exist, it should be created or the correct exception should be used

def test_resolve_requires_success(mocker):
    # Mocking all_fact_subsets to contain the required subsets
    all_fact_subsets = {'subset1', 'subset2', 'subset3'}
    unresolved_requires = ['subset1', 'subset2']

    # Call the function with the mocked data
    new_names = resolve_requires(unresolved_requires, all_fact_subsets)

    # Assertions to check if the function behaves as expected
    assert new_names == set(unresolved_requires), "The new_names set should contain the resolved subsets"

def test_resolve_requires_failure(mocker):
    # Mocking all_fact_subsets to not contain the required subsets
    all_fact_subsets = {'subset1', 'subset2'}
    unresolved_requires = ['subset1', 'subset2', 'subset4']

    # Using pytest.raises to check for the expected exception
    with pytest.raises(UnresolvedFactDep) as excinfo:
        resolve_requires(unresolved_requires, all_fact_subsets)

    # Assertions to check if the exception message is correct
    assert 'unresolved fact dep subset4' in str(excinfo.value), "The exception message should contain the unresolved subset"

# The actual function to be tested
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
