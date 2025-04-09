# file lib/ansible/module_utils/facts/hardware/aix.py:113-131
# lines [113, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]
# branches ['120->121', '120->131', '122->123', '122->131', '123->124', '123->131', '125->126', '125->127', '127->128', '127->129', '129->123', '129->130']

import pytest
from unittest.mock import MagicMock

# Assuming the AIXHardware class is part of a module named aix
from ansible.module_utils.facts.hardware import aix

@pytest.fixture
def mock_module(mocker):
    mock_module = MagicMock()
    mock_module.run_command = MagicMock()
    return mock_module

def test_get_dmi_facts(mock_module, mocker):
    # Mock the run_command method for '/usr/sbin/lsattr -El sys0 -a fwversion'
    mock_module.run_command.side_effect = [
        (0, "fwversion IBM,TestVersion", ""),
        (0, "Machine Serial Number: TestSerial\nLPAR Info: TestLPARInfo\nSystem Model: TestModel", "")
    ]
    
    # Mock the get_bin_path method to return a valid path
    mock_module.get_bin_path = MagicMock(return_value="/usr/sbin/lsconf")

    hardware = aix.AIXHardware(module=mock_module)
    dmi_facts = hardware.get_dmi_facts()

    # Assertions to ensure that the dmi_facts dictionary contains the expected keys and values
    assert dmi_facts['firmware_version'] == 'TestVersion'
    assert dmi_facts['product_serial'] == 'TestSerial'
    assert dmi_facts['lpar_info'] == 'TestLPARInfo'
    assert dmi_facts['product_name'] == 'TestModel'

    # Ensure that run_command was called with the expected commands
    mock_module.run_command.assert_any_call("/usr/sbin/lsattr -El sys0 -a fwversion")
    mock_module.run_command.assert_any_call("/usr/sbin/lsconf")

    # Ensure that get_bin_path was called with the expected argument
    mock_module.get_bin_path.assert_called_once_with("lsconf")
