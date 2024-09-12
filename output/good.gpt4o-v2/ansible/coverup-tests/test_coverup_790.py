# file: lib/ansible/module_utils/facts/virtual/netbsd.py:71-73
# asked: {"lines": [71, 72, 73], "branches": []}
# gained: {"lines": [71, 72, 73], "branches": []}

import pytest
from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtualCollector, NetBSDVirtual

def test_netbsd_virtual_collector():
    collector = NetBSDVirtualCollector()
    assert collector._fact_class == NetBSDVirtual
    assert collector._platform == 'NetBSD'
