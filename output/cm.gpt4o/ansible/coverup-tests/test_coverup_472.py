# file lib/ansible/module_utils/facts/hardware/sunos.py:267-279
# lines [267, 268, 271, 273, 274, 277, 279]
# branches ['273->274', '273->277']

import pytest
import time
from unittest.mock import patch, MagicMock

# Assuming the SunOSHardware class is defined in ansible.module_utils.facts.hardware.sunos
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

@pytest.fixture
def mock_module():
    return MagicMock()

@pytest.fixture
def sunos_hardware(mock_module):
    return SunOSHardware(module=mock_module)

def test_get_uptime_facts_success(sunos_hardware, mocker):
    # Mock the current time
    current_time = 1600000000
    mocker.patch('time.time', return_value=current_time)
    
    # Mock the run_command method to return a successful response
    boot_time = 1599990000
    sunos_hardware.module.run_command.return_value = (0, f'unix:0:system_misc:boot_time\t{boot_time}\n', '')

    # Call the method
    uptime_facts = sunos_hardware.get_uptime_facts()

    # Assert the uptime_seconds is calculated correctly
    assert uptime_facts['uptime_seconds'] == current_time - boot_time

def test_get_uptime_facts_failure(sunos_hardware):
    # Mock the run_command method to return a failure response
    sunos_hardware.module.run_command.return_value = (1, '', 'error')

    # Call the method
    uptime_facts = sunos_hardware.get_uptime_facts()

    # Assert the method returns None on failure
    assert uptime_facts is None
