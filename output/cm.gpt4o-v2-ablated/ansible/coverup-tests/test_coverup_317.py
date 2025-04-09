# file: lib/ansible/module_utils/facts/virtual/hpux.py:70-72
# asked: {"lines": [70, 71, 72], "branches": []}
# gained: {"lines": [70, 71, 72], "branches": []}

import pytest
from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector
from ansible.module_utils.facts.virtual.base import VirtualCollector

def test_hpux_virtual_collector_inheritance():
    collector = HPUXVirtualCollector()
    assert isinstance(collector, VirtualCollector)

def test_hpux_virtual_collector_fact_class():
    collector = HPUXVirtualCollector()
    assert collector._fact_class.__name__ == 'HPUXVirtual'

def test_hpux_virtual_collector_platform():
    collector = HPUXVirtualCollector()
    assert collector._platform == 'HP-UX'
