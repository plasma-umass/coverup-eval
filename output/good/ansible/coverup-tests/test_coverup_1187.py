# file lib/ansible/module_utils/facts/hardware/hpux.py:142-158
# lines [143, 144, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 158]
# branches ['148->149', '148->158', '150->151', '150->152', '155->156', '155->158']

import pytest
from unittest.mock import MagicMock

# Assuming the HPUXHardware class is part of a module named hpux
from ansible.module_utils.facts.hardware import hpux

# Test function to cover lines 143-158
@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    mock_module.run_command = MagicMock()
    return mock_module

def test_get_hw_facts_ia64_architecture(mock_module):
    hw = hpux.HPUXHardware(module=mock_module)

    # Mocking the responses for run_command
    mock_module.run_command.side_effect = [
        (0, "Test Model", ""),
        (0, "Firmware revision=1234", ""),
        (0, "Machine serial number=ABCD", "")
    ]

    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': "B.11.23"
    }

    hw_facts = hw.get_hw_facts(collected_facts)

    # Assertions to verify postconditions
    assert hw_facts['model'] == "Test Model"
    assert hw_facts['firmware_version'] == "1234"
    assert hw_facts['product_serial'] == "ABCD"

    # Verify that run_command was called with the expected commands
    mock_module.run_command.assert_any_call("model")
    mock_module.run_command.assert_any_call("/usr/contrib/bin/machinfo |grep -i 'Firmware revision' | grep -v BMC", use_unsafe_shell=True)
    mock_module.run_command.assert_any_call("/usr/contrib/bin/machinfo |grep -i 'Machine serial number' ", use_unsafe_shell=True)

    # Verify that run_command was called exactly 3 times
    assert mock_module.run_command.call_count == 3
