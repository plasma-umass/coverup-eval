# file: lib/ansible/module_utils/facts/hardware/netbsd.py:160-162
# asked: {"lines": [160, 161, 162], "branches": []}
# gained: {"lines": [160, 161, 162], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardwareCollector
from ansible.module_utils.facts.hardware.base import HardwareCollector

def test_netbsd_hardware_collector_inheritance():
    collector = NetBSDHardwareCollector()
    assert isinstance(collector, HardwareCollector)
    assert collector._platform == 'NetBSD'
    assert collector._fact_class.__name__ == 'NetBSDHardware'
