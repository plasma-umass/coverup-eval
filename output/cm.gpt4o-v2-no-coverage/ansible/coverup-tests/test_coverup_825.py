# file: lib/ansible/module_utils/facts/virtual/freebsd.py:77-79
# asked: {"lines": [77, 78, 79], "branches": []}
# gained: {"lines": [77, 78, 79], "branches": []}

import pytest
from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtualCollector
from ansible.module_utils.facts.virtual.base import VirtualCollector

def test_freebsd_virtual_collector_inheritance():
    collector = FreeBSDVirtualCollector()
    assert isinstance(collector, VirtualCollector)
    assert collector._platform == 'FreeBSD'
    assert collector._fact_class.__name__ == 'FreeBSDVirtual'
