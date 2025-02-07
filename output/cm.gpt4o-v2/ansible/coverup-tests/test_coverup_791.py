# file: lib/ansible/module_utils/facts/virtual/hpux.py:70-72
# asked: {"lines": [70, 71, 72], "branches": []}
# gained: {"lines": [70, 71, 72], "branches": []}

import pytest
from ansible.module_utils.facts.virtual.hpux import HPUXVirtualCollector
from ansible.module_utils.facts.virtual.base import VirtualCollector

def test_hpux_virtual_collector_inheritance():
    # Ensure HPUXVirtualCollector inherits from VirtualCollector
    assert issubclass(HPUXVirtualCollector, VirtualCollector)

def test_hpux_virtual_collector_fact_class():
    # Ensure the _fact_class attribute is set correctly
    assert HPUXVirtualCollector._fact_class.__name__ == 'HPUXVirtual'

def test_hpux_virtual_collector_platform():
    # Ensure the _platform attribute is set correctly
    assert HPUXVirtualCollector._platform == 'HP-UX'
