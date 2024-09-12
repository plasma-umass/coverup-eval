# file: lib/ansible/module_utils/facts/hardware/netbsd.py:137-157
# asked: {"lines": [137, 138, 145, 146, 147, 148, 149, 150, 153, 154, 155, 157], "branches": [[153, 154], [153, 157], [154, 153], [154, 155]]}
# gained: {"lines": [137, 138, 145, 146, 147, 148, 149, 150, 153, 154, 155, 157], "branches": [[153, 154], [153, 157], [154, 153], [154, 155]]}

import pytest
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardware

@pytest.fixture
def netbsd_hardware(mocker):
    module_mock = mocker.Mock()
    return NetBSDHardware(module=module_mock)

def test_get_dmi_facts_empty_sysctl(netbsd_hardware):
    netbsd_hardware.sysctl = {}
    dmi_facts = netbsd_hardware.get_dmi_facts()
    assert dmi_facts == {}

def test_get_dmi_facts_partial_sysctl(netbsd_hardware):
    netbsd_hardware.sysctl = {
        'machdep.dmi.system-product': 'TestProduct',
        'machdep.dmi.system-version': '1.0',
    }
    dmi_facts = netbsd_hardware.get_dmi_facts()
    assert dmi_facts == {
        'product_name': 'TestProduct',
        'product_version': '1.0',
    }

def test_get_dmi_facts_full_sysctl(netbsd_hardware):
    netbsd_hardware.sysctl = {
        'machdep.dmi.system-product': 'TestProduct',
        'machdep.dmi.system-version': '1.0',
        'machdep.dmi.system-uuid': '1234-5678-9012',
        'machdep.dmi.system-serial': 'SN123456',
        'machdep.dmi.system-vendor': 'TestVendor',
    }
    dmi_facts = netbsd_hardware.get_dmi_facts()
    assert dmi_facts == {
        'product_name': 'TestProduct',
        'product_version': '1.0',
        'product_uuid': '1234-5678-9012',
        'product_serial': 'SN123456',
        'system_vendor': 'TestVendor',
    }
