# file: lib/ansible/module_utils/facts/hardware/netbsd.py:137-157
# asked: {"lines": [137, 138, 145, 146, 147, 148, 149, 150, 153, 154, 155, 157], "branches": [[153, 154], [153, 157], [154, 153], [154, 155]]}
# gained: {"lines": [137, 138, 145, 146, 147, 148, 149, 150, 153, 154, 155, 157], "branches": [[153, 154], [153, 157], [154, 153], [154, 155]]}

import pytest
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardware

class MockHardware(NetBSDHardware):
    def __init__(self, sysctl):
        self.sysctl = sysctl

@pytest.fixture
def mock_hardware():
    sysctl_data = {
        'machdep.dmi.system-product': 'TestProduct',
        'machdep.dmi.system-version': 'TestVersion',
        'machdep.dmi.system-uuid': 'TestUUID',
        'machdep.dmi.system-serial': 'TestSerial',
        'machdep.dmi.system-vendor': 'TestVendor',
    }
    return MockHardware(sysctl_data)

def test_get_dmi_facts_all_keys_present(mock_hardware):
    dmi_facts = mock_hardware.get_dmi_facts()
    
    assert dmi_facts['product_name'] == 'TestProduct'
    assert dmi_facts['product_version'] == 'TestVersion'
    assert dmi_facts['product_uuid'] == 'TestUUID'
    assert dmi_facts['product_serial'] == 'TestSerial'
    assert dmi_facts['system_vendor'] == 'TestVendor'

def test_get_dmi_facts_some_keys_missing(mock_hardware):
    sysctl_data = {
        'machdep.dmi.system-product': 'TestProduct',
        'machdep.dmi.system-version': 'TestVersion',
    }
    mock_hardware.sysctl = sysctl_data
    dmi_facts = mock_hardware.get_dmi_facts()
    
    assert dmi_facts['product_name'] == 'TestProduct'
    assert dmi_facts['product_version'] == 'TestVersion'
    assert 'product_uuid' not in dmi_facts
    assert 'product_serial' not in dmi_facts
    assert 'system_vendor' not in dmi_facts

def test_get_dmi_facts_no_keys_present(mock_hardware):
    mock_hardware.sysctl = {}
    dmi_facts = mock_hardware.get_dmi_facts()
    
    assert dmi_facts == {}
