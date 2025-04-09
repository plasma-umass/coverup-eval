# file: lib/ansible/module_utils/facts/hardware/darwin.py:134-154
# asked: {"lines": [137, 138, 141, 145, 146, 147, 148, 150, 152, 153], "branches": [[147, 148], [147, 150]]}
# gained: {"lines": [137, 138, 141, 145, 146, 147, 148, 150, 152, 153], "branches": [[147, 148], [147, 150]]}

import pytest
import struct
import time
from ansible.module_utils.facts.hardware.darwin import DarwinHardware

@pytest.fixture
def mock_module(mocker):
    module = mocker.Mock()
    module.get_bin_path.return_value = '/usr/sbin/sysctl'
    return module

@pytest.fixture
def darwin_hardware(mock_module):
    return DarwinHardware(module=mock_module)

def test_get_uptime_facts_success(mocker, darwin_hardware):
    # Mock the current time
    current_time = 1609459200  # Fixed timestamp for testing
    mocker.patch('time.time', return_value=current_time)
    
    # Mock the run_command method to return a successful response
    kern_boottime = current_time - 3600  # 1 hour ago
    packed_boottime = struct.pack('@L', kern_boottime)
    darwin_hardware.module.run_command.return_value = (0, packed_boottime, '')

    # Call the method
    result = darwin_hardware.get_uptime_facts()

    # Assertions
    assert result == {'uptime_seconds': 3600}
    darwin_hardware.module.get_bin_path.assert_called_once_with('sysctl')
    darwin_hardware.module.run_command.assert_called_once_with(['/usr/sbin/sysctl', '-b', 'kern.boottime'], encoding=None)

def test_get_uptime_facts_failure_command(mocker, darwin_hardware):
    # Mock the run_command method to return a failure response
    darwin_hardware.module.run_command.return_value = (1, b'', 'error')

    # Call the method
    result = darwin_hardware.get_uptime_facts()

    # Assertions
    assert result == {}
    darwin_hardware.module.get_bin_path.assert_called_once_with('sysctl')
    darwin_hardware.module.run_command.assert_called_once_with(['/usr/sbin/sysctl', '-b', 'kern.boottime'], encoding=None)

def test_get_uptime_facts_failure_output_length(mocker, darwin_hardware):
    # Mock the run_command method to return an insufficient output length
    darwin_hardware.module.run_command.return_value = (0, b'\x00\x00\x00', '')

    # Call the method
    result = darwin_hardware.get_uptime_facts()

    # Assertions
    assert result == {}
    darwin_hardware.module.get_bin_path.assert_called_once_with('sysctl')
    darwin_hardware.module.run_command.assert_called_once_with(['/usr/sbin/sysctl', '-b', 'kern.boottime'], encoding=None)
