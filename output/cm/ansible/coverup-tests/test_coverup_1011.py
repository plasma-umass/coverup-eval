# file lib/ansible/module_utils/facts/collector.py:50-51
# lines [50, 51]
# branches []

import pytest
from ansible.module_utils.facts.collector import UnresolvedFactDep

def test_unresolved_fact_dep_exception():
    with pytest.raises(UnresolvedFactDep) as exc_info:
        raise UnresolvedFactDep("test exception")

    assert str(exc_info.value) == "test exception", "UnresolvedFactDep did not contain the correct message"
