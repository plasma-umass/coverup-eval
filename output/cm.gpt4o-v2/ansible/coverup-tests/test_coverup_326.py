# file: lib/ansible/module_utils/facts/hardware/freebsd.py:129-149
# asked: {"lines": [129, 132, 133, 136, 140, 141, 142, 143, 145, 147, 148], "branches": [[142, 143], [142, 145]]}
# gained: {"lines": [129, 132, 133, 136, 140, 141, 142, 143, 145, 147, 148], "branches": [[142, 143], [142, 145]]}

import struct
import time
import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
from ansible.module_utils.basic import AnsibleModule

@pytest.fixture
def module():
    return MagicMock(spec=AnsibleModule)

@pytest.fixture
def freebsd_hardware(module):
    return FreeBSDHardware(module)

def test_get_uptime_facts_success(freebsd_hardware, module):
    sysctl_cmd = '/sbin/sysctl'
    module.get_bin_path.return_value = sysctl_cmd
    kern_boottime = int(time.time()) - 1000
    packed_boottime = struct.pack('@L', kern_boottime)
    module.run_command.return_value = (0, packed_boottime, '')

    result = freebsd_hardware.get_uptime_facts()

    assert 'uptime_seconds' in result
    assert result['uptime_seconds'] == 1000

def test_get_uptime_facts_failure_rc_non_zero(freebsd_hardware, module):
    sysctl_cmd = '/sbin/sysctl'
    module.get_bin_path.return_value = sysctl_cmd
    module.run_command.return_value = (1, b'', 'error')

    result = freebsd_hardware.get_uptime_facts()

    assert result == {}

def test_get_uptime_facts_failure_output_too_short(freebsd_hardware, module):
    sysctl_cmd = '/sbin/sysctl'
    module.get_bin_path.return_value = sysctl_cmd
    module.run_command.return_value = (0, b'\x00\x00\x00', '')

    result = freebsd_hardware.get_uptime_facts()

    assert result == {}
