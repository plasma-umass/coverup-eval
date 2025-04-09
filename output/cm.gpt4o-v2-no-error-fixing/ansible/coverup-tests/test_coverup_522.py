# file: lib/ansible/module_utils/facts/virtual/hpux.py:70-72
# asked: {"lines": [70, 71, 72], "branches": []}
# gained: {"lines": [70, 71, 72], "branches": []}

import pytest
from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector, HPUXVirtual

def test_hpux_virtual_collector_initialization():
    collector = HPUXVirtualCollector()
    assert collector._fact_class == HPUXVirtual
    assert collector._platform == 'HP-UX'
