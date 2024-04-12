# file lib/ansible/module_utils/facts/hardware/freebsd.py:129-149
# lines [129, 132, 133, 136, 140, 141, 142, 143, 145, 147, 148]
# branches ['142->143', '142->145']

import pytest
import struct
import time
from unittest.mock import MagicMock

# Assuming the FreeBSDHardware class is part of a module named freebsd_hardware
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

@pytest.fixture
def freebsd_hardware(mocker):
    module_mock = MagicMock()
    module_mock.get_bin_path.return_value = '/sbin/sysctl'
    hardware = FreeBSDHardware(module=module_mock)
    return hardware

def test_get_uptime_facts_success(freebsd_hardware, mocker):
    # Mock the run_command method to return successful output
    kern_boottime = int(time.time()) - 3600  # Assume the system booted up 1 hour ago
    packed_time = struct.pack('@L', kern_boottime)
    mocker.patch.object(freebsd_hardware.module, 'run_command', return_value=(0, packed_time, ''))

    # Call the method under test
    uptime_facts = freebsd_hardware.get_uptime_facts()

    # Assert that the returned dictionary contains the correct uptime_seconds
    assert uptime_facts['uptime_seconds'] == 3600

def test_get_uptime_facts_failure(freebsd_hardware, mocker):
    # Mock the run_command method to simulate a failure
    mocker.patch.object(freebsd_hardware.module, 'run_command', return_value=(1, b'', ''))

    # Call the method under test
    uptime_facts = freebsd_hardware.get_uptime_facts()

    # Assert that the returned dictionary is empty due to the failure
    assert uptime_facts == {}

def test_get_uptime_facts_incomplete_data(freebsd_hardware, mocker):
    # Mock the run_command method to return incomplete data
    incomplete_data = b'\x00'  # Less than the required struct_size
    mocker.patch.object(freebsd_hardware.module, 'run_command', return_value=(0, incomplete_data, ''))

    # Call the method under test
    uptime_facts = freebsd_hardware.get_uptime_facts()

    # Assert that the returned dictionary is empty due to incomplete data
    assert uptime_facts == {}
