# file: lib/ansible/module_utils/facts/hardware/darwin.py:134-154
# asked: {"lines": [134, 137, 138, 141, 145, 146, 147, 148, 150, 152, 153], "branches": [[147, 148], [147, 150]]}
# gained: {"lines": [134, 137, 138, 141, 145, 146, 147, 148, 150, 152, 153], "branches": [[147, 148], [147, 150]]}

import pytest
import struct
import time
from unittest.mock import Mock, patch
from ansible.module_utils.facts.hardware.darwin import DarwinHardware

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def darwin_hardware(mock_module):
    return DarwinHardware(module=mock_module)

def test_get_uptime_facts_success(darwin_hardware, mock_module):
    sysctl_cmd = '/usr/sbin/sysctl'
    mock_module.get_bin_path.return_value = sysctl_cmd
    current_time = time.time()
    boot_time = current_time - 3600  # Assume the system has been up for 1 hour
    packed_boot_time = struct.pack('@L', int(boot_time))
    mock_module.run_command.return_value = (0, packed_boot_time, '')

    with patch('time.time', return_value=current_time):
        uptime_facts = darwin_hardware.get_uptime_facts()

    assert uptime_facts == {'uptime_seconds': 3600}
    mock_module.get_bin_path.assert_called_once_with('sysctl')
    mock_module.run_command.assert_called_once_with([sysctl_cmd, '-b', 'kern.boottime'], encoding=None)

def test_get_uptime_facts_failure(darwin_hardware, mock_module):
    sysctl_cmd = '/usr/sbin/sysctl'
    mock_module.get_bin_path.return_value = sysctl_cmd
    mock_module.run_command.return_value = (1, b'', 'error')

    uptime_facts = darwin_hardware.get_uptime_facts()

    assert uptime_facts == {}
    mock_module.get_bin_path.assert_called_once_with('sysctl')
    mock_module.run_command.assert_called_once_with([sysctl_cmd, '-b', 'kern.boottime'], encoding=None)

def test_get_uptime_facts_insufficient_output(darwin_hardware, mock_module):
    sysctl_cmd = '/usr/sbin/sysctl'
    mock_module.get_bin_path.return_value = sysctl_cmd
    mock_module.run_command.return_value = (0, b'\x00\x00\x00', '')

    uptime_facts = darwin_hardware.get_uptime_facts()

    assert uptime_facts == {}
    mock_module.get_bin_path.assert_called_once_with('sysctl')
    mock_module.run_command.assert_called_once_with([sysctl_cmd, '-b', 'kern.boottime'], encoding=None)
