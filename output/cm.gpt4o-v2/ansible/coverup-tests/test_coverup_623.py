# file: lib/ansible/module_utils/facts/hardware/openbsd.py:151-157
# asked: {"lines": [151, 152, 153, 154, 155, 157], "branches": []}
# gained: {"lines": [151, 152, 153, 154, 155, 157], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware
from unittest.mock import MagicMock

@pytest.fixture
def openbsd_hardware():
    module = MagicMock()
    hardware = OpenBSDHardware(module)
    hardware.sysctl = {'hw.disknames': 'sd0,sd1,sd2'}
    return hardware

def test_get_device_facts(openbsd_hardware):
    device_facts = openbsd_hardware.get_device_facts()
    assert 'devices' in device_facts
    assert device_facts['devices'] == ['sd0', 'sd1', 'sd2']
