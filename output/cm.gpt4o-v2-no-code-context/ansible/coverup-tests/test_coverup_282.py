# file: lib/ansible/module_utils/facts/hardware/darwin.py:134-154
# asked: {"lines": [134, 137, 138, 141, 145, 146, 147, 148, 150, 152, 153], "branches": [[147, 148], [147, 150]]}
# gained: {"lines": [134, 137, 138, 141, 145, 146, 147, 148, 150, 152, 153], "branches": [[147, 148], [147, 150]]}

import pytest
import struct
import time
from ansible.module_utils.facts.hardware.darwin import DarwinHardware
from unittest.mock import MagicMock

@pytest.fixture
def darwin_hardware():
    module = MagicMock()
    return DarwinHardware(module)

def test_get_uptime_facts_success(darwin_hardware, monkeypatch):
    sysctl_cmd = '/usr/sbin/sysctl'
    monkeypatch.setattr(darwin_hardware.module, 'get_bin_path', lambda x: sysctl_cmd)
    
    # Mock the run_command to return a successful response
    kern_boottime = int(time.time()) - 1000  # 1000 seconds ago
    packed_time = struct.pack('@L', kern_boottime)
    darwin_hardware.module.run_command = MagicMock(return_value=(0, packed_time, ''))
    
    result = darwin_hardware.get_uptime_facts()
    
    assert 'uptime_seconds' in result
    assert result['uptime_seconds'] == 1000

def test_get_uptime_facts_failure(darwin_hardware, monkeypatch):
    sysctl_cmd = '/usr/sbin/sysctl'
    monkeypatch.setattr(darwin_hardware.module, 'get_bin_path', lambda x: sysctl_cmd)
    
    # Mock the run_command to return a failure response
    darwin_hardware.module.run_command = MagicMock(return_value=(1, b'', 'error'))
    
    result = darwin_hardware.get_uptime_facts()
    
    assert result == {}

def test_get_uptime_facts_insufficient_output(darwin_hardware, monkeypatch):
    sysctl_cmd = '/usr/sbin/sysctl'
    monkeypatch.setattr(darwin_hardware.module, 'get_bin_path', lambda x: sysctl_cmd)
    
    # Mock the run_command to return insufficient output
    darwin_hardware.module.run_command = MagicMock(return_value=(0, b'\x00\x00', ''))
    
    result = darwin_hardware.get_uptime_facts()
    
    assert result == {}
