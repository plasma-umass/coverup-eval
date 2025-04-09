# file: lib/ansible/module_utils/facts/hardware/aix.py:113-131
# asked: {"lines": [113, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131], "branches": [[120, 121], [120, 131], [122, 123], [122, 131], [123, 124], [123, 131], [125, 126], [125, 127], [127, 128], [127, 129], [129, 123], [129, 130]]}
# gained: {"lines": [113, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131], "branches": [[120, 121], [120, 131], [122, 123], [122, 131], [123, 124], [123, 131], [125, 126], [125, 127], [127, 128], [127, 129], [129, 123], [129, 130]]}

import pytest
from unittest.mock import Mock

from ansible.module_utils.facts.hardware.aix import AIXHardware

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def aix_hardware(mock_module):
    return AIXHardware(module=mock_module)

def test_get_dmi_facts_no_lsconf(aix_hardware, mock_module):
    mock_module.run_command.return_value = (0, "fwversion IBM,1234", "")
    mock_module.get_bin_path.return_value = None

    dmi_facts = aix_hardware.get_dmi_facts()

    assert dmi_facts == {'firmware_version': '1234'}
    mock_module.run_command.assert_called_once_with("/usr/sbin/lsattr -El sys0 -a fwversion")
    mock_module.get_bin_path.assert_called_once_with("lsconf")

def test_get_dmi_facts_with_lsconf(aix_hardware, mock_module):
    mock_module.run_command.side_effect = [
        (0, "fwversion IBM,1234", ""),
        (0, "Machine Serial Number: 5678\nLPAR Info: lpar123\nSystem Model: modelXYZ", "")
    ]
    mock_module.get_bin_path.return_value = "/usr/sbin/lsconf"

    dmi_facts = aix_hardware.get_dmi_facts()

    assert dmi_facts == {
        'firmware_version': '1234',
        'product_serial': '5678',
        'lpar_info': 'lpar123',
        'product_name': 'modelXYZ'
    }
    mock_module.run_command.assert_any_call("/usr/sbin/lsattr -El sys0 -a fwversion")
    mock_module.run_command.assert_any_call("/usr/sbin/lsconf")
    mock_module.get_bin_path.assert_called_once_with("lsconf")

def test_get_dmi_facts_lsconf_no_output(aix_hardware, mock_module):
    mock_module.run_command.side_effect = [
        (0, "fwversion IBM,1234", ""),
        (0, "", "")
    ]
    mock_module.get_bin_path.return_value = "/usr/sbin/lsconf"

    dmi_facts = aix_hardware.get_dmi_facts()

    assert dmi_facts == {'firmware_version': '1234'}
    mock_module.run_command.assert_any_call("/usr/sbin/lsattr -El sys0 -a fwversion")
    mock_module.run_command.assert_any_call("/usr/sbin/lsconf")
    mock_module.get_bin_path.assert_called_once_with("lsconf")
