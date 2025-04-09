# file: lib/ansible/module_utils/facts/virtual/hpux.py:70-72
# asked: {"lines": [70, 71, 72], "branches": []}
# gained: {"lines": [70, 71, 72], "branches": []}

import pytest
from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector

def test_hpux_virtual_collector_class_attributes():
    assert HPUXVirtualCollector._fact_class.__name__ == 'HPUXVirtual'
    assert HPUXVirtualCollector._platform == 'HP-UX'
