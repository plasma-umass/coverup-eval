# file lib/ansible/module_utils/facts/hardware/darwin.py:134-154
# lines [137, 138, 141, 145, 146, 147, 148, 150, 152, 153]
# branches ['147->148', '147->150']

import pytest
import struct
import time
from unittest.mock import MagicMock

# Assuming the DarwinHardware class is imported from the appropriate module
from ansible.module_utils.facts.hardware.darwin import DarwinHardware

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    mock_module.get_bin_path.return_value = '/usr/sbin/sysctl'
    mock_module.run_command.return_value = (0, struct.pack('@L', int(time.time() - 1000)), '')
    return mock_module

def test_get_uptime_facts(mock_module):
    hardware = DarwinHardware(module=mock_module)
    uptime_facts = hardware.get_uptime_facts()

    assert uptime_facts['uptime_seconds'] >= 1000
    mock_module.get_bin_path.assert_called_once_with('sysctl')
    mock_module.run_command.assert_called_once_with(['/usr/sbin/sysctl', '-b', 'kern.boottime'], encoding=None)
