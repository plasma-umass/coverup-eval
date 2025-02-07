# file: lib/ansible/module_utils/facts/hardware/darwin.py:134-154
# asked: {"lines": [134, 137, 138, 141, 145, 146, 147, 148, 150, 152, 153], "branches": [[147, 148], [147, 150]]}
# gained: {"lines": [134, 137, 138, 141, 145, 146, 147, 148, 150, 152, 153], "branches": [[147, 148], [147, 150]]}

import pytest
import struct
import time
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.hardware.darwin import DarwinHardware
from ansible.module_utils.basic import AnsibleModule

@pytest.fixture
def mock_module():
    module = MagicMock(spec=AnsibleModule)
    return module

def test_get_uptime_facts_success(mock_module):
    darwin_hardware = DarwinHardware(module=mock_module)
    mock_module.get_bin_path.return_value = '/usr/sbin/sysctl'
    mock_module.run_command.return_value = (0, struct.pack('@L', int(time.time() - 1000)), '')

    result = darwin_hardware.get_uptime_facts()

    assert 'uptime_seconds' in result
    assert result['uptime_seconds'] >= 1000

def test_get_uptime_facts_failure(mock_module):
    darwin_hardware = DarwinHardware(module=mock_module)
    mock_module.get_bin_path.return_value = '/usr/sbin/sysctl'
    mock_module.run_command.return_value = (1, b'', 'error')

    result = darwin_hardware.get_uptime_facts()

    assert result == {}

def test_get_uptime_facts_insufficient_output(mock_module):
    darwin_hardware = DarwinHardware(module=mock_module)
    mock_module.get_bin_path.return_value = '/usr/sbin/sysctl'
    mock_module.run_command.return_value = (0, b'\x00\x00\x00', '')

    result = darwin_hardware.get_uptime_facts()

    assert result == {}
