# file: lib/ansible/module_utils/facts/hardware/sunos.py:282-286
# asked: {"lines": [282, 283, 284, 286], "branches": []}
# gained: {"lines": [282, 283, 284, 286], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.sunos import SunOSHardwareCollector, SunOSHardware
from ansible.module_utils.facts.hardware.base import HardwareCollector

def test_sunos_hardware_collector_initialization():
    collector = SunOSHardwareCollector()
    assert collector._fact_class == SunOSHardware
    assert collector._platform == 'SunOS'
    assert collector.required_facts == set(['platform'])

def test_sunos_hardware_collector_collect(monkeypatch):
    class MockModule:
        def __init__(self):
            self.params = {}

    def mock_collect(self, module=None, collected_facts=None):
        return {'platform': 'SunOS'}

    monkeypatch.setattr(HardwareCollector, 'collect', mock_collect)
    collector = SunOSHardwareCollector()
    facts = collector.collect(MockModule())
    assert facts == {'platform': 'SunOS'}
