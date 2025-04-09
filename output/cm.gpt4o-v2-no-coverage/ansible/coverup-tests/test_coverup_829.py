# file: lib/ansible/module_utils/facts/virtual/sunos.py:137-139
# asked: {"lines": [137, 138, 139], "branches": []}
# gained: {"lines": [137, 138, 139], "branches": []}

import pytest
from ansible.module_utils.facts.virtual.sunos import SunOSVirtualCollector
from ansible.module_utils.facts.virtual.base import VirtualCollector

class MockSunOSVirtual:
    pass

def test_sunos_virtual_collector_initialization(monkeypatch):
    monkeypatch.setattr(SunOSVirtualCollector, '_fact_class', MockSunOSVirtual)
    collector = SunOSVirtualCollector()
    assert collector._fact_class == MockSunOSVirtual
    assert collector._platform == 'SunOS'
    assert issubclass(SunOSVirtualCollector, VirtualCollector)
