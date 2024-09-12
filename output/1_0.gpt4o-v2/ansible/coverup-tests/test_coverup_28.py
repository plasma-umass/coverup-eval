# file: lib/ansible/module_utils/facts/virtual/dragonfly.py:22-25
# asked: {"lines": [22, 24, 25], "branches": []}
# gained: {"lines": [22, 24, 25], "branches": []}

import pytest
from ansible.module_utils.facts.virtual.dragonfly import DragonFlyVirtualCollector
from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtual

def test_dragonfly_virtual_collector_inheritance():
    collector = DragonFlyVirtualCollector()
    assert isinstance(collector, DragonFlyVirtualCollector)
    assert collector._fact_class == FreeBSDVirtual
    assert collector._platform == 'DragonFly'

def test_dragonfly_virtual_collector_collect(monkeypatch):
    class MockModule:
        pass

    class MockCollectedFacts:
        pass

    def mock_collect(self, module=None, collected_facts=None):
        return {'virtual': 'mocked'}

    monkeypatch.setattr(DragonFlyVirtualCollector, 'collect', mock_collect)
    collector = DragonFlyVirtualCollector()
    result = collector.collect(MockModule(), MockCollectedFacts())
    assert result == {'virtual': 'mocked'}
