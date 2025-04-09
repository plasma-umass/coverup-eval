# file: lib/ansible/module_utils/facts/hardware/netbsd.py:160-162
# asked: {"lines": [160, 161, 162], "branches": []}
# gained: {"lines": [160, 161, 162], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardwareCollector, NetBSDHardware

def test_netbsd_hardware_collector_class_attributes():
    assert NetBSDHardwareCollector._fact_class == NetBSDHardware
    assert NetBSDHardwareCollector._platform == 'NetBSD'
