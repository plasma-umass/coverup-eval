# file: lib/ansible/module_utils/facts/hardware/freebsd.py:129-149
# asked: {"lines": [129, 132, 133, 136, 140, 141, 142, 143, 145, 147, 148], "branches": [[142, 143], [142, 145]]}
# gained: {"lines": [129, 132, 133, 136, 140, 141, 142, 143, 145, 147, 148], "branches": [[142, 143], [142, 145]]}

import pytest
import struct
import time
from unittest.mock import Mock, patch
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def freebsd_hardware(mock_module):
    return FreeBSDHardware(module=mock_module)

def test_get_uptime_facts_success(freebsd_hardware, mock_module):
    sysctl_cmd = '/sbin/sysctl'
    mock_module.get_bin_path.return_value = sysctl_cmd
    kern_boottime = int(time.time()) - 1000  # simulate a system that has been up for 1000 seconds
    packed_boottime = struct.pack('@L', kern_boottime)
    mock_module.run_command.return_value = (0, packed_boottime, '')

    result = freebsd_hardware.get_uptime_facts()

    assert 'uptime_seconds' in result
    assert result['uptime_seconds'] == 1000

def test_get_uptime_facts_failure(freebsd_hardware, mock_module):
    sysctl_cmd = '/sbin/sysctl'
    mock_module.get_bin_path.return_value = sysctl_cmd
    mock_module.run_command.return_value = (1, b'', 'error')

    result = freebsd_hardware.get_uptime_facts()

    assert result == {}

def test_get_uptime_facts_insufficient_output(freebsd_hardware, mock_module):
    sysctl_cmd = '/sbin/sysctl'
    mock_module.get_bin_path.return_value = sysctl_cmd
    mock_module.run_command.return_value = (0, b'\x00\x00\x00', '')

    result = freebsd_hardware.get_uptime_facts()

    assert result == {}
