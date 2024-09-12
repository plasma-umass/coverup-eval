# file: lib/ansible/module_utils/facts/hardware/netbsd.py:160-162
# asked: {"lines": [160, 161, 162], "branches": []}
# gained: {"lines": [160, 161, 162], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardwareCollector, NetBSDHardware
from ansible.module_utils.facts.hardware.base import HardwareCollector

def test_netbsd_hardware_collector_inheritance():
    collector = NetBSDHardwareCollector()
    assert isinstance(collector, HardwareCollector)

def test_netbsd_hardware_collector_fact_class():
    collector = NetBSDHardwareCollector()
    assert collector._fact_class == NetBSDHardware

def test_netbsd_hardware_collector_platform():
    collector = NetBSDHardwareCollector()
    assert collector._platform == 'NetBSD'
