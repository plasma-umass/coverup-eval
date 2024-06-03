# file lib/ansible/module_utils/facts/collector.py:50-51
# lines [50, 51]
# branches []

import pytest
from ansible.module_utils.facts.collector import UnresolvedFactDep

def test_unresolved_fact_dep():
    with pytest.raises(UnresolvedFactDep):
        raise UnresolvedFactDep("This is a test for UnresolvedFactDep exception")
