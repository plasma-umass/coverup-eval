# file: lib/ansible/module_utils/facts/hardware/netbsd.py:137-157
# asked: {"lines": [137, 138, 145, 146, 147, 148, 149, 150, 153, 154, 155, 157], "branches": [[153, 154], [153, 157], [154, 153], [154, 155]]}
# gained: {"lines": [137, 138, 145, 146, 147, 148, 149, 150, 153, 154, 155, 157], "branches": [[153, 154], [153, 157], [154, 153], [154, 155]]}

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardware

@pytest.fixture
def netbsd_hardware():
    module = MagicMock()
    hardware = NetBSDHardware(module)
    return hardware

def test_get_dmi_facts_empty_sysctl(netbsd_hardware):
    netbsd_hardware.sysctl = {}
    dmi_facts = netbsd_hardware.get_dmi_facts()
    assert dmi_facts == {}

def test_get_dmi_facts_with_sysctl(netbsd_hardware):
    netbsd_hardware.sysctl = {
        'machdep.dmi.system-product': 'TestProduct',
        'machdep.dmi.system-version': 'TestVersion',
        'machdep.dmi.system-uuid': 'TestUUID',
        'machdep.dmi.system-serial': 'TestSerial',
        'machdep.dmi.system-vendor': 'TestVendor',
    }
    dmi_facts = netbsd_hardware.get_dmi_facts()
    assert dmi_facts == {
        'product_name': 'TestProduct',
        'product_version': 'TestVersion',
        'product_uuid': 'TestUUID',
        'product_serial': 'TestSerial',
        'system_vendor': 'TestVendor',
    }
