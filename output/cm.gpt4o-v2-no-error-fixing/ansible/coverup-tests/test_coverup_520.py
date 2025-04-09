# file: lib/ansible/module_utils/facts/hardware/netbsd.py:160-162
# asked: {"lines": [160, 161, 162], "branches": []}
# gained: {"lines": [160, 161, 162], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardwareCollector
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardware

def test_netbsd_hardware_collector():
    collector = NetBSDHardwareCollector()
    assert collector._fact_class == NetBSDHardware
    assert collector._platform == 'NetBSD'
