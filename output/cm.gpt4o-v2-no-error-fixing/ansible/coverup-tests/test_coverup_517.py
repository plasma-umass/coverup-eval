# file: lib/ansible/module_utils/facts/virtual/netbsd.py:71-73
# asked: {"lines": [71, 72, 73], "branches": []}
# gained: {"lines": [71, 72, 73], "branches": []}

import pytest
from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtualCollector
from ansible.module_utils.facts.virtual.base import VirtualCollector

def test_netbsd_virtual_collector_inheritance():
    collector = NetBSDVirtualCollector()
    assert isinstance(collector, VirtualCollector)
    assert collector._fact_class.__name__ == 'NetBSDVirtual'
    assert collector._platform == 'NetBSD'
