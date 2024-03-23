# file lib/ansible/module_utils/facts/hardware/darwin.py:134-154
# lines [148]
# branches ['147->148']

import pytest
import struct
import time
from unittest.mock import MagicMock

# Assuming DarwinHardware and Hardware are defined elsewhere in the module
from ansible.module_utils.facts.hardware.darwin import DarwinHardware

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    mock_module.get_bin_path.return_value = '/usr/sbin/sysctl'
    return mock_module

def test_get_uptime_facts_failure(mock_module, mocker):
    # Mock the run_command method to simulate a failure
    mocker.patch.object(mock_module, 'run_command', return_value=(1, b'', b'Error'))

    hardware = DarwinHardware(module=mock_module)
    facts = hardware.get_uptime_facts()

    # Assert that the method returns an empty dictionary on failure
    assert facts == {}

def test_get_uptime_facts_success(mock_module, mocker):
    # Prepare the expected output from the sysctl command
    kern_boottime = int(time.time()) - 3600  # Assume the system booted up 1 hour ago
    packed_data = struct.pack('@L', kern_boottime)

    # Mock the run_command method to return successful output
    mocker.patch.object(mock_module, 'run_command', return_value=(0, packed_data, b''))

    hardware = DarwinHardware(module=mock_module)
    facts = hardware.get_uptime_facts()

    # Assert that the method returns the correct uptime_seconds
    assert 'uptime_seconds' in facts
    assert facts['uptime_seconds'] == 3600
