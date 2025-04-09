# file: lib/ansible/module_utils/facts/virtual/openbsd.py:72-74
# asked: {"lines": [72, 73, 74], "branches": []}
# gained: {"lines": [72, 73, 74], "branches": []}

import pytest
from ansible.module_utils.facts.virtual.openbsd import OpenBSDVirtualCollector, OpenBSDVirtual
from ansible.module_utils.facts.virtual.base import VirtualCollector

def test_openbsd_virtual_collector_inheritance():
    collector = OpenBSDVirtualCollector()
    assert isinstance(collector, VirtualCollector)

def test_openbsd_virtual_collector_fact_class():
    collector = OpenBSDVirtualCollector()
    assert collector._fact_class == OpenBSDVirtual

def test_openbsd_virtual_collector_platform():
    collector = OpenBSDVirtualCollector()
    assert collector._platform == 'OpenBSD'
