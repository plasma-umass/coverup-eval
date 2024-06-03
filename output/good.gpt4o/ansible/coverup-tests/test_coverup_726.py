# file lib/ansible/module_utils/facts/collector.py:39-47
# lines [39, 40, 47]
# branches []

import pytest
from ansible.module_utils.facts.collector import CycleFoundInFactDeps

def test_cycle_found_in_fact_deps():
    with pytest.raises(CycleFoundInFactDeps):
        raise CycleFoundInFactDeps("Cycle detected in fact collector dependencies")
