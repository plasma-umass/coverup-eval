# file lib/ansible/module_utils/facts/hardware/freebsd.py:191-236
# lines [196, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 220, 221, 222, 223, 226, 227, 228, 229, 230, 232, 234, 236]
# branches ['220->221', '220->236', '221->222', '221->234', '223->226', '223->232']

import pytest
from unittest.mock import Mock, patch

# Assuming the FreeBSDHardware class is imported from ansible.module_utils.facts.hardware.freebsd
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

@pytest.fixture
def mock_module():
    module = Mock()
    module.get_bin_path.return_value = '/usr/sbin/dmidecode'
    return module

def test_get_dmi_facts(mock_module):
    hardware = FreeBSDHardware(mock_module)

    dmi_output = {
        'bios-release-date': '01/01/2020\n',
        'bios-vendor': 'VendorName\n',
        'bios-version': '1.0.0\n',
        'baseboard-asset-tag': 'AssetTag\n',
        'baseboard-product-name': 'ProductName\n',
        'baseboard-serial-number': 'SerialNumber\n',
        'baseboard-manufacturer': 'Manufacturer\n',
        'baseboard-version': '1.0\n',
        'chassis-asset-tag': 'ChassisAssetTag\n',
        'chassis-serial-number': 'ChassisSerialNumber\n',
        'chassis-manufacturer': 'ChassisManufacturer\n',
        'chassis-version': 'ChassisVersion\n',
        'chassis-type': 'Desktop\n',
        'system-product-name': 'SystemProductName\n',
        'system-serial-number': 'SystemSerialNumber\n',
        'system-uuid': 'UUID\n',
        'system-version': 'SystemVersion\n',
        'system-manufacturer': 'SystemManufacturer\n',
    }

    def mock_run_command(cmd):
        for key, value in dmi_output.items():
            if key in cmd:
                return (0, value, '')
        return (1, '', 'Error')

    hardware.module.run_command.side_effect = mock_run_command

    dmi_facts = hardware.get_dmi_facts()

    expected_facts = {
        'bios_date': '01/01/2020',
        'bios_vendor': 'VendorName',
        'bios_version': '1.0.0',
        'board_asset_tag': 'AssetTag',
        'board_name': 'ProductName',
        'board_serial': 'SerialNumber',
        'board_vendor': 'Manufacturer',
        'board_version': '1.0',
        'chassis_asset_tag': 'ChassisAssetTag',
        'chassis_serial': 'ChassisSerialNumber',
        'chassis_vendor': 'ChassisManufacturer',
        'chassis_version': 'ChassisVersion',
        'form_factor': 'Desktop',
        'product_name': 'SystemProductName',
        'product_serial': 'SystemSerialNumber',
        'product_uuid': 'UUID',
        'product_version': 'SystemVersion',
        'system_vendor': 'SystemManufacturer',
    }

    assert dmi_facts == expected_facts

    # Clean up
    mock_module.reset_mock()
