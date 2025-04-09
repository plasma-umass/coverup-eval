# file: lib/ansible/module_utils/facts/virtual/netbsd.py:71-73
# asked: {"lines": [71, 72, 73], "branches": []}
# gained: {"lines": [71, 72, 73], "branches": []}

import pytest
from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtualCollector, NetBSDVirtual

def test_netbsd_virtual_collector_class_attributes():
    assert NetBSDVirtualCollector._fact_class is NetBSDVirtual
    assert NetBSDVirtualCollector._platform == 'NetBSD'
