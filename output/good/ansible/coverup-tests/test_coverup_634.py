# file lib/ansible/module_utils/facts/hardware/openbsd.py:151-157
# lines [151, 152, 153, 154, 155, 157]
# branches []

import pytest
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware

# Mocking the OpenBSDHardware class to simulate the sysctl attribute
@pytest.fixture
def openbsd_hardware(mocker):
    mocker.patch('ansible.module_utils.facts.hardware.openbsd.Hardware', autospec=True)
    openbsd_hardware = OpenBSDHardware(module=mocker.MagicMock())
    openbsd_hardware.sysctl = {'hw.disknames': 'sd0,sd1'}
    return openbsd_hardware

# Test function to cover get_device_facts method
def test_get_device_facts(openbsd_hardware):
    expected_device_facts = {
        'devices': ['sd0', 'sd1']
    }
    device_facts = openbsd_hardware.get_device_facts()
    assert device_facts == expected_device_facts
