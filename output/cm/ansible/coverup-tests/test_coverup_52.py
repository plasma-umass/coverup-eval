# file lib/ansible/module_utils/facts/hardware/freebsd.py:191-236
# lines [191, 196, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 220, 221, 222, 223, 226, 227, 228, 229, 230, 232, 234, 236]
# branches ['220->221', '220->236', '221->222', '221->234', '223->226', '223->232']

import json
import pytest
from unittest.mock import MagicMock

# Assuming the FreeBSDHardware class is part of a module named freebsd
from ansible.module_utils.facts.hardware import freebsd

@pytest.fixture
def mock_module(mocker):
    mock_module = MagicMock()
    mock_module.get_bin_path = MagicMock(return_value='/usr/sbin/dmidecode')
    mock_module.run_command = MagicMock()
    return mock_module

@pytest.fixture
def freebsd_hardware(mock_module):
    return freebsd.FreeBSDHardware(module=mock_module)

def test_get_dmi_facts_with_dmidecode_success(freebsd_hardware, mock_module):
    # Mock the run_command to simulate successful dmidecode output
    def run_command_effect(cmd):
        dmi_key = cmd.split()[-1]
        return (0, f"Test {dmi_key} output", "")
    mock_module.run_command.side_effect = run_command_effect

    DMI_DICT = {
        'bios_date': 'bios-release-date',
        'bios_vendor': 'bios-vendor',
        'bios_version': 'bios-version',
        'board_asset_tag': 'baseboard-asset-tag',
        'board_name': 'baseboard-product-name',
        'board_serial': 'baseboard-serial-number',
        'board_vendor': 'baseboard-manufacturer',
        'board_version': 'baseboard-version',
        'chassis_asset_tag': 'chassis-asset-tag',
        'chassis_serial': 'chassis-serial-number',
        'chassis_vendor': 'chassis-manufacturer',
        'chassis_version': 'chassis-version',
        'form_factor': 'chassis-type',
        'product_name': 'system-product-name',
        'product_serial': 'system-serial-number',
        'product_uuid': 'system-uuid',
        'product_version': 'system-version',
        'system_vendor': 'system-manufacturer',
    }

    expected_dmi_facts = {
        'bios_date': 'Test bios-release-date output',
        'bios_vendor': 'Test bios-vendor output',
        'bios_version': 'Test bios-version output',
        'board_asset_tag': 'Test baseboard-asset-tag output',
        'board_name': 'Test baseboard-product-name output',
        'board_serial': 'Test baseboard-serial-number output',
        'board_vendor': 'Test baseboard-manufacturer output',
        'board_version': 'Test baseboard-version output',
        'chassis_asset_tag': 'Test chassis-asset-tag output',
        'chassis_serial': 'Test chassis-serial-number output',
        'chassis_vendor': 'Test chassis-manufacturer output',
        'chassis_version': 'Test chassis-version output',
        'form_factor': 'Test chassis-type output',
        'product_name': 'Test system-product-name output',
        'product_serial': 'Test system-serial-number output',
        'product_uuid': 'Test system-uuid output',
        'product_version': 'Test system-version output',
        'system_vendor': 'Test system-manufacturer output',
    }

    dmi_facts = freebsd_hardware.get_dmi_facts()

    # Verify that the returned dmi_facts match the expected values
    assert dmi_facts == expected_dmi_facts
    # Verify that run_command was called with the correct arguments
    for dmi_key, dmi_value in DMI_DICT.items():
        mock_module.run_command.assert_any_call(f'/usr/sbin/dmidecode -s {dmi_value}')

def test_get_dmi_facts_with_dmidecode_failure(freebsd_hardware, mock_module):
    # Mock the run_command to simulate dmidecode failure
    mock_module.run_command.return_value = (1, "", "Error")

    dmi_facts = freebsd_hardware.get_dmi_facts()

    # Verify that all dmi_facts are 'NA' due to dmidecode failure
    for value in dmi_facts.values():
        assert value == 'NA'

def test_get_dmi_facts_without_dmidecode(freebsd_hardware, mock_module):
    # Mock get_bin_path to simulate absence of dmidecode
    mock_module.get_bin_path.return_value = None

    dmi_facts = freebsd_hardware.get_dmi_facts()

    # Verify that all dmi_facts are 'NA' due to absence of dmidecode
    for value in dmi_facts.values():
        assert value == 'NA'
