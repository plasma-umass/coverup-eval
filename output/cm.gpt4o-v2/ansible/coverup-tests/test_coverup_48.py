# file: lib/ansible/module_utils/facts/hardware/freebsd.py:191-236
# asked: {"lines": [191, 196, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 220, 221, 222, 223, 226, 227, 228, 229, 230, 232, 234, 236], "branches": [[220, 221], [220, 236], [221, 222], [221, 234], [223, 226], [223, 232]]}
# gained: {"lines": [191, 196, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 220, 221, 222, 223, 226, 227, 228, 229, 230, 232, 234, 236], "branches": [[220, 221], [220, 236], [221, 222], [221, 234], [223, 226], [223, 232]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

@pytest.fixture
def module_mock():
    return Mock()

@pytest.fixture
def freebsd_hardware(module_mock):
    hw = FreeBSDHardware(module=module_mock)
    return hw

def test_get_dmi_facts_no_dmidecode(freebsd_hardware, module_mock):
    module_mock.get_bin_path.return_value = None
    dmi_facts = freebsd_hardware.get_dmi_facts()
    expected_keys = [
        'bios_date', 'bios_vendor', 'bios_version', 'board_asset_tag', 'board_name',
        'board_serial', 'board_vendor', 'board_version', 'chassis_asset_tag', 'chassis_serial',
        'chassis_vendor', 'chassis_version', 'form_factor', 'product_name', 'product_serial',
        'product_uuid', 'product_version', 'system_vendor'
    ]
    assert all(dmi_facts[key] == 'NA' for key in expected_keys)

def test_get_dmi_facts_with_dmidecode(freebsd_hardware, module_mock):
    module_mock.get_bin_path.return_value = '/usr/sbin/dmidecode'
    module_mock.run_command.return_value = (0, 'test_output', '')

    dmi_facts = freebsd_hardware.get_dmi_facts()
    expected_keys = [
        'bios_date', 'bios_vendor', 'bios_version', 'board_asset_tag', 'board_name',
        'board_serial', 'board_vendor', 'board_version', 'chassis_asset_tag', 'chassis_serial',
        'chassis_vendor', 'chassis_version', 'form_factor', 'product_name', 'product_serial',
        'product_uuid', 'product_version', 'system_vendor'
    ]
    assert all(dmi_facts[key] == 'test_output' for key in expected_keys)

def test_get_dmi_facts_with_unicode_error(freebsd_hardware, module_mock):
    module_mock.get_bin_path.return_value = '/usr/sbin/dmidecode'
    module_mock.run_command.return_value = (0, 'test_output', '')

    with patch('json.dumps', side_effect=UnicodeDecodeError('utf-8', b"", 0, 1, '')):
        dmi_facts = freebsd_hardware.get_dmi_facts()
        expected_keys = [
            'bios_date', 'bios_vendor', 'bios_version', 'board_asset_tag', 'board_name',
            'board_serial', 'board_vendor', 'board_version', 'chassis_asset_tag', 'chassis_serial',
            'chassis_vendor', 'chassis_version', 'form_factor', 'product_name', 'product_serial',
            'product_uuid', 'product_version', 'system_vendor'
        ]
        assert all(dmi_facts[key] == 'NA' for key in expected_keys)

def test_get_dmi_facts_command_failure(freebsd_hardware, module_mock):
    module_mock.get_bin_path.return_value = '/usr/sbin/dmidecode'
    module_mock.run_command.return_value = (1, '', 'error')

    dmi_facts = freebsd_hardware.get_dmi_facts()
    expected_keys = [
        'bios_date', 'bios_vendor', 'bios_version', 'board_asset_tag', 'board_name',
        'board_serial', 'board_vendor', 'board_version', 'chassis_asset_tag', 'chassis_serial',
        'chassis_vendor', 'chassis_version', 'form_factor', 'product_name', 'product_serial',
        'product_uuid', 'product_version', 'system_vendor'
    ]
    assert all(dmi_facts[key] == 'NA' for key in expected_keys)
