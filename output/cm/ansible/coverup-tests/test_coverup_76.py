# file lib/ansible/module_utils/facts/hardware/aix.py:57-84
# lines [57, 58, 59, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 74, 76, 77, 79, 80, 81, 82, 84]
# branches ['62->63', '62->84', '64->66', '64->72', '66->64', '66->67', '67->68', '67->71', '80->81', '80->84']

import pytest
from unittest.mock import MagicMock

# Assuming the AIXHardware class is part of a module named aix
from ansible.module_utils.facts.hardware import aix

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    mock_module.run_command = MagicMock()
    return mock_module

def test_get_cpu_facts(mock_module, mocker):
    # Mock the responses for run_command
    mock_module.run_command.side_effect = [
        (0, "proc0 Available\nproc1 Available", ""),  # First call to run_command
        (0, "type PowerPC_POWER8", ""),               # Second call to run_command
        (0, "smt_threads 8", "")                      # Third call to run_command
    ]

    hardware = aix.AIXHardware(module=mock_module)
    cpu_facts = hardware.get_cpu_facts()

    # Assertions to check if the cpu_facts dictionary contains the right information
    assert cpu_facts['processor_count'] == 2
    assert cpu_facts['processor'] == 'PowerPC_POWER8'
    assert cpu_facts['processor_cores'] == 8

    # Cleanup is handled by the fixture and mock, no persistent changes are made
