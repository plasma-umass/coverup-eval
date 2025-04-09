# file lib/ansible/module_utils/facts/hardware/sunos.py:206-265
# lines [206, 222, 223, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 239, 241, 242, 244, 245, 246, 247, 249, 250, 251, 252, 253, 254, 256, 257, 259, 261, 262, 263, 265]
# branches ['241->242', '241->244', '246->247', '246->249', '250->251', '250->265', '252->253', '252->261', '256->257', '256->259']

import pytest
from unittest.mock import patch, MagicMock

# Assuming the SunOSHardware class is imported from the module
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.run_command = MagicMock()
    return module

@pytest.fixture
def sunos_hardware(mock_module):
    return SunOSHardware(module=mock_module)

def bytes_to_human(size):
    # Mock implementation of bytes_to_human function
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.1f}{unit}"
        size /= 1024.0
    return f"{size:.1f}PB"

@patch('ansible.module_utils.facts.hardware.sunos.bytes_to_human', side_effect=bytes_to_human)
def test_get_device_facts_success(mock_bytes_to_human, sunos_hardware, mock_module):
    mock_output = (
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
    mock_module.run_command.return_value = (0, mock_output, '')

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
                'vendor': 'ATA',
            }
        }
    }

    device_facts = sunos_hardware.get_device_facts()
    assert device_facts == expected_device_facts

def test_get_device_facts_failure(sunos_hardware, mock_module):
    mock_module.run_command.return_value = (1, '', 'error')

    device_facts = sunos_hardware.get_device_facts()
    assert device_facts == {'devices': {}}
