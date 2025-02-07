# file: lib/ansible/module_utils/facts/hardware/aix.py:113-131
# asked: {"lines": [114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131], "branches": [[120, 121], [120, 131], [122, 123], [122, 131], [123, 124], [123, 131], [125, 126], [125, 127], [127, 128], [127, 129], [129, 123], [129, 130]]}
# gained: {"lines": [114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131], "branches": [[120, 121], [120, 131], [122, 123], [122, 131], [123, 124], [123, 131], [125, 126], [125, 127], [127, 128], [127, 129], [129, 123], [129, 130]]}

import pytest
from unittest.mock import MagicMock

from ansible.module_utils.facts.hardware.aix import AIXHardware

@pytest.fixture
def module_mock():
    return MagicMock()

@pytest.fixture
def aix_hardware(module_mock):
    return AIXHardware(module=module_mock)

def test_get_dmi_facts_no_lsconf(aix_hardware, module_mock):
    module_mock.run_command.return_value = (0, "fwversion IBM,FW123", "")
    module_mock.get_bin_path.return_value = None

    dmi_facts = aix_hardware.get_dmi_facts()

    assert dmi_facts == {'firmware_version': 'FW123'}
    module_mock.run_command.assert_called_once_with("/usr/sbin/lsattr -El sys0 -a fwversion")
    module_mock.get_bin_path.assert_called_once_with("lsconf")

def test_get_dmi_facts_with_lsconf(aix_hardware, module_mock):
    module_mock.run_command.side_effect = [
        (0, "fwversion IBM,FW123", ""),
        (0, "Machine Serial Number: 123456\nLPAR Info: LPAR1\nSystem Model: ModelX", "")
    ]
    module_mock.get_bin_path.return_value = "/usr/sbin/lsconf"

    dmi_facts = aix_hardware.get_dmi_facts()

    assert dmi_facts == {
        'firmware_version': 'FW123',
        'product_serial': '123456',
        'lpar_info': 'LPAR1',
        'product_name': 'ModelX'
    }
    module_mock.run_command.assert_any_call("/usr/sbin/lsattr -El sys0 -a fwversion")
    module_mock.run_command.assert_any_call("/usr/sbin/lsconf")
    module_mock.get_bin_path.assert_called_once_with("lsconf")

def test_get_dmi_facts_with_lsconf_no_output(aix_hardware, module_mock):
    module_mock.run_command.side_effect = [
        (0, "fwversion IBM,FW123", ""),
        (0, "", "")
    ]
    module_mock.get_bin_path.return_value = "/usr/sbin/lsconf"

    dmi_facts = aix_hardware.get_dmi_facts()

    assert dmi_facts == {'firmware_version': 'FW123'}
    module_mock.run_command.assert_any_call("/usr/sbin/lsattr -El sys0 -a fwversion")
    module_mock.run_command.assert_any_call("/usr/sbin/lsconf")
    module_mock.get_bin_path.assert_called_once_with("lsconf")
