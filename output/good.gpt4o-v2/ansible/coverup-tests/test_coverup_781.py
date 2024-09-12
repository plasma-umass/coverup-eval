# file: lib/ansible/module_utils/facts/hardware/netbsd.py:160-162
# asked: {"lines": [160, 161, 162], "branches": []}
# gained: {"lines": [160, 161, 162], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardwareCollector, NetBSDHardware
from ansible.module_utils.facts.hardware.base import HardwareCollector

def test_netbsd_hardware_collector_inheritance():
    # Ensure NetBSDHardwareCollector inherits from HardwareCollector
    assert issubclass(NetBSDHardwareCollector, HardwareCollector)

def test_netbsd_hardware_collector_fact_class():
    # Ensure the _fact_class attribute is set correctly
    assert NetBSDHardwareCollector._fact_class is NetBSDHardware

def test_netbsd_hardware_collector_platform():
    # Ensure the _platform attribute is set correctly
    assert NetBSDHardwareCollector._platform == 'NetBSD'
