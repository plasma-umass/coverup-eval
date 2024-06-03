# file lib/ansible/module_utils/facts/hardware/darwin.py:134-154
# lines [134, 137, 138, 141, 145, 146, 147, 148, 150, 152, 153]
# branches ['147->148', '147->150']

import pytest
import struct
import time
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.hardware.darwin import DarwinHardware

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.get_bin_path.return_value = '/usr/sbin/sysctl'
    return module

def test_get_uptime_facts_success(mock_module):
    darwin_hardware = DarwinHardware(mock_module)

    # Mock the run_command to return a successful response
    kern_boottime = int(time.time()) - 3600  # 1 hour ago
    packed_boottime = struct.pack('@L', kern_boottime)
    mock_module.run_command.return_value = (0, packed_boottime, '')

    result = darwin_hardware.get_uptime_facts()

    assert 'uptime_seconds' in result
    assert result['uptime_seconds'] == 3600

def test_get_uptime_facts_failure(mock_module):
    darwin_hardware = DarwinHardware(mock_module)

    # Mock the run_command to return a failure response
    mock_module.run_command.return_value = (1, b'', 'error')

    result = darwin_hardware.get_uptime_facts()

    assert result == {}

def test_get_uptime_facts_insufficient_output(mock_module):
    darwin_hardware = DarwinHardware(mock_module)

    # Mock the run_command to return insufficient output
    mock_module.run_command.return_value = (0, b'\x00\x00\x00', '')

    result = darwin_hardware.get_uptime_facts()

    assert result == {}
