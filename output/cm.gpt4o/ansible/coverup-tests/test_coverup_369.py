# file lib/ansible/module_utils/facts/hardware/freebsd.py:129-149
# lines [129, 132, 133, 136, 140, 141, 142, 143, 145, 147, 148]
# branches ['142->143', '142->145']

import pytest
import struct
import time
from unittest.mock import patch, MagicMock

# Assuming the FreeBSDHardware class is imported from ansible.module_utils.facts.hardware.freebsd
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    return module

def test_get_uptime_facts_success(mock_module):
    hardware = FreeBSDHardware(mock_module)

    # Mock the return value of run_command
    current_time = int(time.time())
    kern_boottime = current_time - 1000  # Assume the system booted 1000 seconds ago
    packed_boottime = struct.pack('@L', kern_boottime)
    mock_module.run_command.return_value = (0, packed_boottime, '')

    result = hardware.get_uptime_facts()

    assert 'uptime_seconds' in result
    assert result['uptime_seconds'] == 1000

def test_get_uptime_facts_failure(mock_module):
    hardware = FreeBSDHardware(mock_module)

    # Mock the return value of run_command to simulate a failure
    mock_module.run_command.return_value = (1, b'', 'error')

    result = hardware.get_uptime_facts()

    assert result == {}

def test_get_uptime_facts_insufficient_output(mock_module):
    hardware = FreeBSDHardware(mock_module)

    # Mock the return value of run_command to simulate insufficient output
    mock_module.run_command.return_value = (0, b'\x00\x00\x00', '')

    result = hardware.get_uptime_facts()

    assert result == {}
