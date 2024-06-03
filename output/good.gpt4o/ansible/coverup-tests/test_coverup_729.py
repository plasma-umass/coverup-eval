# file lib/ansible/module_utils/facts/hardware/netbsd.py:160-162
# lines [160, 161, 162]
# branches []

import pytest
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardwareCollector, HardwareCollector, NetBSDHardware

def test_netbsd_hardware_collector_initialization():
    collector = NetBSDHardwareCollector()
    assert isinstance(collector, HardwareCollector)
    assert collector._fact_class == NetBSDHardware
    assert collector._platform == 'NetBSD'
