# file lib/ansible/module_utils/facts/hardware/aix.py:113-131
# lines []
# branches ['120->131', '122->131']

import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_module(mocker):
    module = Mock()
    module.run_command = Mock()
    module.get_bin_path = Mock()
    return module

def test_get_dmi_facts_with_lsconf_path(mock_module):
    from ansible.module_utils.facts.hardware.aix import AIXHardware

    # Mocking the module's methods
    mock_module.run_command.side_effect = [
        (0, "fwversion IBM,FW123", ""),  # First call to run_command
        (0, "Machine Serial Number: 123456\nLPAR Info: LPAR123\nSystem Model: Model123", "")  # Second call to run_command
    ]
    mock_module.get_bin_path.return_value = "/usr/sbin/lsconf"

    # Create an instance of AIXHardware with the mocked module
    aix_hardware = AIXHardware(mock_module)

    # Call the method
    dmi_facts = aix_hardware.get_dmi_facts()

    # Assertions to verify the postconditions
    assert dmi_facts['firmware_version'] == "FW123"
    assert dmi_facts['product_serial'] == "123456"
    assert dmi_facts['lpar_info'] == "LPAR123"
    assert dmi_facts['product_name'] == "Model123"

    # Verify that the methods were called with expected arguments
    mock_module.run_command.assert_any_call("/usr/sbin/lsattr -El sys0 -a fwversion")
    mock_module.run_command.assert_any_call("/usr/sbin/lsconf")
    mock_module.get_bin_path.assert_called_once_with("lsconf")

def test_get_dmi_facts_without_lsconf_path(mock_module):
    from ansible.module_utils.facts.hardware.aix import AIXHardware

    # Mocking the module's methods
    mock_module.run_command.return_value = (0, "fwversion IBM,FW123", "")
    mock_module.get_bin_path.return_value = None

    # Create an instance of AIXHardware with the mocked module
    aix_hardware = AIXHardware(mock_module)

    # Call the method
    dmi_facts = aix_hardware.get_dmi_facts()

    # Assertions to verify the postconditions
    assert dmi_facts['firmware_version'] == "FW123"
    assert 'product_serial' not in dmi_facts
    assert 'lpar_info' not in dmi_facts
    assert 'product_name' not in dmi_facts

    # Verify that the methods were called with expected arguments
    mock_module.run_command.assert_called_once_with("/usr/sbin/lsattr -El sys0 -a fwversion")
    mock_module.get_bin_path.assert_called_once_with("lsconf")
