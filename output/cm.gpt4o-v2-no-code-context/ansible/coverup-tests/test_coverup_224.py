# file: lib/ansible/module_utils/facts/hardware/openbsd.py:159-179
# asked: {"lines": [159, 160, 167, 168, 169, 170, 171, 172, 175, 176, 177, 179], "branches": [[175, 176], [175, 179], [176, 175], [176, 177]]}
# gained: {"lines": [159, 160, 167, 168, 169, 170, 171, 172, 175, 176, 177, 179], "branches": [[175, 176], [175, 179], [176, 175], [176, 177]]}

import pytest
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware

class MockHardware(OpenBSDHardware):
    def __init__(self, sysctl):
        self.sysctl = sysctl

@pytest.fixture
def mock_hardware():
    sysctl_data = {
        'hw.product': 'TestProduct',
        'hw.version': '1.0',
        'hw.uuid': '1234-5678-90AB-CDEF',
        'hw.serialno': 'SN1234567890',
        'hw.vendor': 'TestVendor'
    }
    return MockHardware(sysctl=sysctl_data)

def test_get_dmi_facts_all_keys_present(mock_hardware):
    hardware = mock_hardware
    dmi_facts = hardware.get_dmi_facts()
    
    assert dmi_facts['product_name'] == 'TestProduct'
    assert dmi_facts['product_version'] == '1.0'
    assert dmi_facts['product_uuid'] == '1234-5678-90AB-CDEF'
    assert dmi_facts['product_serial'] == 'SN1234567890'
    assert dmi_facts['system_vendor'] == 'TestVendor'

def test_get_dmi_facts_some_keys_missing(mock_hardware):
    sysctl_data = {
        'hw.product': 'TestProduct',
        'hw.uuid': '1234-5678-90AB-CDEF',
        'hw.vendor': 'TestVendor'
    }
    mock_hardware.sysctl = sysctl_data
    hardware = mock_hardware
    dmi_facts = hardware.get_dmi_facts()
    
    assert dmi_facts['product_name'] == 'TestProduct'
    assert 'product_version' not in dmi_facts
    assert dmi_facts['product_uuid'] == '1234-5678-90AB-CDEF'
    assert 'product_serial' not in dmi_facts
    assert dmi_facts['system_vendor'] == 'TestVendor'

def test_get_dmi_facts_no_keys_present(mock_hardware):
    mock_hardware.sysctl = {}
    hardware = mock_hardware
    dmi_facts = hardware.get_dmi_facts()
    
    assert dmi_facts == {}
