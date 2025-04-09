# file: lib/ansible/module_utils/facts/hardware/sunos.py:282-286
# asked: {"lines": [282, 283, 284, 286], "branches": []}
# gained: {"lines": [282, 283, 284, 286], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.sunos import SunOSHardwareCollector

def test_sunos_hardware_collector_initialization():
    collector = SunOSHardwareCollector()
    assert collector._fact_class.__name__ == 'SunOSHardware'
    assert collector._platform == 'SunOS'
    assert collector.required_facts == {'platform'}
