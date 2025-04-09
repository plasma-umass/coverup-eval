# file lib/ansible/module_utils/facts/hardware/aix.py:113-131
# lines []
# branches ['122->131']

import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_module(mocker):
    module = Mock()
    module.run_command = Mock()
    module.get_bin_path = Mock()
    return module

@pytest.fixture
def aix_hardware(mock_module):
    from ansible.module_utils.facts.hardware.aix import AIXHardware
    return AIXHardware(module=mock_module)

def test_get_dmi_facts_full_coverage(aix_hardware, mock_module):
    # Mock the run_command to return expected values
    mock_module.run_command.side_effect = [
        (0, "fwversion IBM,FW860.50", ""),  # First call for firmware version
        (0, "Machine Serial Number: 1234567\nLPAR Info: LPAR123\nSystem Model: IBM,9117-MMB", ""),  # Second call for lsconf
        (1, "", "error")  # Third call to simulate non-zero return code
    ]
    mock_module.get_bin_path.return_value = "/usr/sbin/lsconf"

    dmi_facts = aix_hardware.get_dmi_facts()

    assert dmi_facts['firmware_version'] == "FW860.50"
    assert dmi_facts['product_serial'] == "1234567"
    assert dmi_facts['lpar_info'] == "LPAR123"
    assert dmi_facts['product_name'] == "IBM,9117-MMB"

    # Ensure the run_command was called twice
    assert mock_module.run_command.call_count == 2

    # Ensure get_bin_path was called once
    mock_module.get_bin_path.assert_called_once_with("lsconf")

    # Test the branch where rc != 0 or out is empty
    mock_module.run_command.side_effect = [
        (0, "fwversion IBM,FW860.50", ""),  # First call for firmware version
        (1, "", "error")  # Second call to simulate non-zero return code
    ]
    dmi_facts = aix_hardware.get_dmi_facts()

    assert dmi_facts['firmware_version'] == "FW860.50"
    assert 'product_serial' not in dmi_facts
    assert 'lpar_info' not in dmi_facts
    assert 'product_name' not in dmi_facts

    # Ensure the run_command was called twice again
    assert mock_module.run_command.call_count == 4  # 2 previous + 2 new calls

    # Ensure get_bin_path was called twice in total
    assert mock_module.get_bin_path.call_count == 2
