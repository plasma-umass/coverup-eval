# file lib/ansible/module_utils/facts/hardware/sunos.py:267-279
# lines [267, 268, 271, 273, 274, 277, 279]
# branches ['273->274', '273->277']

import pytest
import time
from unittest.mock import MagicMock

# Assuming the SunOSHardware class is part of a module named sunos
from ansible.module_utils.facts.hardware import sunos

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    mock_module.run_command = MagicMock()
    return mock_module

def test_get_uptime_facts_success(mock_module, mocker):
    # Mock the time module's time function
    mocker.patch.object(time, 'time', return_value=1548253689)  # Current time
    # Mock the run_command to simulate kstat output
    mock_module.run_command.return_value = (0, 'unix:0:system_misc:boot_time\t1548249689\n', '')

    hardware = sunos.SunOSHardware(module=mock_module)
    uptime_facts = hardware.get_uptime_facts()

    assert uptime_facts is not None
    assert 'uptime_seconds' in uptime_facts
    assert uptime_facts['uptime_seconds'] == 4000  # 1548253689 - 1548249689

def test_get_uptime_facts_failure(mock_module):
    # Simulate a failure in running the command
    mock_module.run_command.return_value = (1, '', 'An error occurred')

    hardware = sunos.SunOSHardware(module=mock_module)
    uptime_facts = hardware.get_uptime_facts()

    assert uptime_facts is None
