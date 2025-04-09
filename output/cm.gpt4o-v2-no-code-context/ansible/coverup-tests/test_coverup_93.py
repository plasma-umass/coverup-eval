# file: lib/ansible/module_utils/facts/hardware/sunos.py:168-204
# asked: {"lines": [168, 169, 173, 174, 176, 177, 178, 181, 182, 186, 193, 194, 195, 196, 197, 199, 200, 201, 202, 204], "branches": [[181, 182], [181, 204], [200, 201], [200, 204]]}
# gained: {"lines": [168, 169, 173, 174, 176, 177, 178, 181, 182, 186, 193, 194, 195, 196, 197, 199, 200, 201, 202, 204], "branches": [[181, 182], [181, 204], [200, 201], [200, 204]]}

import pytest
import re
from unittest.mock import MagicMock

# Assuming the SunOSHardware class is imported from the module
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

@pytest.fixture
def sunos_hardware(mocker):
    module = mocker.MagicMock()
    return SunOSHardware(module)

def test_get_dmi_facts_no_prtdiag(sunos_hardware, mocker):
    # Mock the run_command to return a platform
    sunos_hardware.module.run_command = mocker.MagicMock(side_effect=[
        (0, 'i86pc', ''),  # uname -i
        (1, '', '')        # prtdiag not found
    ])
    # Mock get_bin_path to return a path
    sunos_hardware.module.get_bin_path = mocker.MagicMock(return_value='/usr/platform/i86pc/sbin/prtdiag')

    dmi_facts = sunos_hardware.get_dmi_facts()
    assert dmi_facts == {}

def test_get_dmi_facts_with_prtdiag_output(sunos_hardware, mocker):
    # Mock the run_command to return a platform and prtdiag output
    sunos_hardware.module.run_command = mocker.MagicMock(side_effect=[
        (0, 'i86pc', ''),  # uname -i
        (0, 'System Configuration: Oracle Corporation  Sun Fire X4170 M2', '')  # prtdiag output
    ])
    # Mock get_bin_path to return a path
    sunos_hardware.module.get_bin_path = mocker.MagicMock(return_value='/usr/platform/i86pc/sbin/prtdiag')

    dmi_facts = sunos_hardware.get_dmi_facts()
    assert dmi_facts == {
        'system_vendor': 'Oracle Corporation',
        'product_name': 'Sun Fire X4170 M2'
    }

def test_get_dmi_facts_with_prtdiag_no_match(sunos_hardware, mocker):
    # Mock the run_command to return a platform and prtdiag output with no match
    sunos_hardware.module.run_command = mocker.MagicMock(side_effect=[
        (0, 'i86pc', ''),  # uname -i
        (0, 'System Configuration: Unknown Vendor Unknown Product', '')  # prtdiag output
    ])
    # Mock get_bin_path to return a path
    sunos_hardware.module.get_bin_path = mocker.MagicMock(return_value='/usr/platform/i86pc/sbin/prtdiag')

    dmi_facts = sunos_hardware.get_dmi_facts()
    assert dmi_facts == {}

def test_get_dmi_facts_with_prtdiag_partial_match(sunos_hardware, mocker):
    # Mock the run_command to return a platform and prtdiag output with partial match
    sunos_hardware.module.run_command = mocker.MagicMock(side_effect=[
        (0, 'i86pc', ''),  # uname -i
        (0, 'System Configuration: VMware, Inc. Some Product', '')  # prtdiag output
    ])
    # Mock get_bin_path to return a path
    sunos_hardware.module.get_bin_path = mocker.MagicMock(return_value='/usr/platform/i86pc/sbin/prtdiag')

    dmi_facts = sunos_hardware.get_dmi_facts()
    assert dmi_facts == {
        'system_vendor': 'VMware, Inc.',
        'product_name': 'Some Product'
    }
