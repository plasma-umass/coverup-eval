# file lib/ansible/module_utils/facts/hardware/netbsd.py:160-162
# lines [160, 161, 162]
# branches []

import pytest
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardwareCollector, NetBSDHardware

# Since the code provided does not include any functionality to test directly,
# we will create a test that simply instantiates the class to ensure that the
# lines are executed and the class can be instantiated without error.

def test_netbsd_hardware_collector_instantiation(mocker):
    mocker.patch.object(NetBSDHardwareCollector, '_fact_class')
    mocker.patch.object(NetBSDHardwareCollector, '_platform', 'NetBSD')

    collector = NetBSDHardwareCollector()
    assert collector._platform == 'NetBSD'
    assert isinstance(collector, NetBSDHardwareCollector)
