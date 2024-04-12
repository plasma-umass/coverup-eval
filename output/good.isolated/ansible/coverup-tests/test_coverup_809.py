# file lib/ansible/module_utils/facts/system/local.py:30-33
# lines [30, 31, 32]
# branches []

import pytest
from ansible.module_utils.facts.system.local import LocalFactCollector
from ansible.module_utils.facts.collector import BaseFactCollector

# Since the LocalFactCollector class does not have much functionality,
# we will test the class attributes and instantiation.

def test_local_fact_collector():
    local_fact_collector = LocalFactCollector()

    # Check if the instance is created correctly
    assert isinstance(local_fact_collector, LocalFactCollector)
    assert isinstance(local_fact_collector, BaseFactCollector)

    # Check if the name attribute is set correctly
    assert local_fact_collector.name == 'local'

    # Check if the _fact_ids attribute is a set and is empty initially
    assert isinstance(local_fact_collector._fact_ids, set)
    assert len(local_fact_collector._fact_ids) == 0

# No cleanup is necessary as no external resources are being modified.
