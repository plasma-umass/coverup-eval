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

def test_get_dmi_facts(mock_hardware):
    dmi_facts = mock_hardware.get_dmi_facts()
    assert dmi_facts == {
        'product_name': 'TestProduct',
        'product_version': '1.0',
        'product_uuid': '1234-5678-90AB-CDEF',
        'product_serial': 'SN1234567890',
        'system_vendor': 'TestVendor'
    }

def test_get_dmi_facts_partial_data():
    sysctl_data = {
        'hw.product': 'TestProduct',
        'hw.uuid': '1234-5678-90AB-CDEF'
    }
    hardware = MockHardware(sysctl=sysctl_data)
    dmi_facts = hardware.get_dmi_facts()
    assert dmi_facts == {
        'product_name': 'TestProduct',
        'product_uuid': '1234-5678-90AB-CDEF'
    }

def test_get_dmi_facts_no_data():
    hardware = MockHardware(sysctl={})
    dmi_facts = hardware.get_dmi_facts()
    assert dmi_facts == {}
