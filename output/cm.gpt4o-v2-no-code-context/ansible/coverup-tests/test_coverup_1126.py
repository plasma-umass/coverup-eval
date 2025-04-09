# file: lib/ansible/module_utils/facts/hardware/sunos.py:206-265
# asked: {"lines": [222, 223, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 239, 241, 242, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 256, 257, 259, 261, 262, 263, 265], "branches": [[241, 242], [241, 244], [246, 247], [246, 249], [250, 251], [250, 265], [252, 253], [252, 261], [256, 257], [256, 259]]}
# gained: {"lines": [222, 223, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 239, 241, 242, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 256, 257, 259, 261, 262, 263, 265], "branches": [[241, 242], [241, 244], [246, 247], [246, 249], [250, 251], [250, 265], [252, 253], [252, 261], [256, 257], [256, 259]]}

import pytest
from unittest.mock import patch, MagicMock

# Assuming the SunOSHardware class is imported from the module
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

@pytest.fixture
def sunos_hardware():
    module = MagicMock()
    return SunOSHardware(module)

def test_get_device_facts_success(sunos_hardware):
    kstat_output = (
        "sderr:0:sd0,err:Hard Errors\t0\n"
        "sderr:0:sd0,err:Illegal Request\t6\n"
        "sderr:0:sd0,err:Media Error\t0\n"
        "sderr:0:sd0,err:Predictive Failure Analysis\t0\n"
        "sderr:0:sd0,err:Product\tVBOX HARDDISK\n"
        "sderr:0:sd0,err:Revision\t1.0\n"
        "sderr:0:sd0,err:Serial No\tVB0ad2ec4d-074a\n"
        "sderr:0:sd0,err:Size\t53687091200\n"
        "sderr:0:sd0,err:Soft Errors\t0\n"
        "sderr:0:sd0,err:Transport Errors\t0\n"
        "sderr:0:sd0,err:Vendor\tATA\n"
    )
    
    sunos_hardware.module.run_command.return_value = (0, kstat_output, '')

    expected_device_facts = {
        'devices': {
            'sd0': {
                'hard_errors': '0',
                'illegal_request': '6',
                'media_errors': '0',
                'predictive_failure_analysis': '0',
                'product': 'VBOX HARDDISK',
                'revision': '1.0',
                'serial': 'VB0ad2ec4d-074a',
                'size': '50.0GB',
                'soft_errors': '0',
                'transport_errors': '0',
                'vendor': 'ATA'
            }
        }
    }

    device_facts = sunos_hardware.get_device_facts()
    # Convert size to float for comparison
    device_facts['devices']['sd0']['size'] = float(device_facts['devices']['sd0']['size'].replace('GB', ''))
    expected_device_facts['devices']['sd0']['size'] = float(expected_device_facts['devices']['sd0']['size'].replace('GB', ''))
    assert device_facts == expected_device_facts

def test_get_device_facts_failure(sunos_hardware):
    sunos_hardware.module.run_command.return_value = (1, '', 'error')

    device_facts = sunos_hardware.get_device_facts()
    assert device_facts == {'devices': {}}
