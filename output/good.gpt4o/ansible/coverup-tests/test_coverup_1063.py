# file lib/ansible/module_utils/facts/hardware/aix.py:57-84
# lines [58, 59, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 74, 76, 77, 79, 80, 81, 82, 84]
# branches ['62->63', '62->84', '64->66', '64->72', '66->64', '66->67', '67->68', '67->71', '80->81', '80->84']

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.hardware.aix import AIXHardware

@pytest.fixture
def mock_module(mocker):
    module = Mock()
    mocker.patch.object(AIXHardware, '__init__', lambda self: None)
    AIXHardware.module = module
    return module

def test_get_cpu_facts(mock_module):
    # Mock the run_command method to return expected values
    mock_module.run_command.side_effect = [
        (0, "proc0 Available\nproc1 Available\n", ""),  # First command output
        (0, "type PowerPC_POWER8", ""),  # Second command output
        (0, "smt_threads 8", "")  # Third command output
    ]

    aix_hardware = AIXHardware()
    cpu_facts = aix_hardware.get_cpu_facts()

    # Assertions to verify the postconditions
    assert cpu_facts['processor_count'] == 2
    assert cpu_facts['processor'] == 'PowerPC_POWER8'
    assert cpu_facts['processor_cores'] == 8

    # Ensure the run_command was called with the expected commands
    mock_module.run_command.assert_any_call("/usr/sbin/lsdev -Cc processor")
    mock_module.run_command.assert_any_call("/usr/sbin/lsattr -El proc0 -a type")
    mock_module.run_command.assert_any_call("/usr/sbin/lsattr -El proc0 -a smt_threads")
