# file: lib/ansible/module_utils/facts/hardware/freebsd.py:129-149
# asked: {"lines": [129, 132, 133, 136, 140, 141, 142, 143, 145, 147, 148], "branches": [[142, 143], [142, 145]]}
# gained: {"lines": [129, 132, 133, 136, 140, 141, 142, 143, 145, 147, 148], "branches": [[142, 143], [142, 145]]}

import pytest
import struct
import time
from unittest.mock import Mock, patch
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

@pytest.fixture
def freebsd_hardware():
    module = Mock()
    return FreeBSDHardware(module)

def test_get_uptime_facts_success(freebsd_hardware):
    sysctl_cmd = '/sbin/sysctl'
    kern_boottime = int(time.time()) - 1000  # 1000 seconds ago
    packed_boottime = struct.pack('@L', kern_boottime)
    
    freebsd_hardware.module.get_bin_path.return_value = sysctl_cmd
    freebsd_hardware.module.run_command.return_value = (0, packed_boottime, '')

    result = freebsd_hardware.get_uptime_facts()

    assert 'uptime_seconds' in result
    assert result['uptime_seconds'] == 1000

def test_get_uptime_facts_failure_rc_non_zero(freebsd_hardware):
    sysctl_cmd = '/sbin/sysctl'
    
    freebsd_hardware.module.get_bin_path.return_value = sysctl_cmd
    freebsd_hardware.module.run_command.return_value = (1, b'', 'error')

    result = freebsd_hardware.get_uptime_facts()

    assert result == {}

def test_get_uptime_facts_failure_output_too_short(freebsd_hardware):
    sysctl_cmd = '/sbin/sysctl'
    short_output = b'\x00\x00\x00\x00'
    
    freebsd_hardware.module.get_bin_path.return_value = sysctl_cmd
    freebsd_hardware.module.run_command.return_value = (0, short_output, '')

    result = freebsd_hardware.get_uptime_facts()

    assert result == {}
