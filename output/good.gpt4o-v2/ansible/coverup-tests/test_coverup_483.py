# file: lib/ansible/module_utils/facts/hardware/sunos.py:267-279
# asked: {"lines": [267, 268, 271, 273, 274, 277, 279], "branches": [[273, 274], [273, 277]]}
# gained: {"lines": [267, 268, 271, 273, 274, 277, 279], "branches": [[273, 274], [273, 277]]}

import pytest
import time
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

@pytest.fixture
def mock_module(mocker):
    module = mocker.Mock()
    return module

def test_get_uptime_facts_success(mocker, mock_module):
    sunos_hardware = SunOSHardware(mock_module)

    mock_time = 1600000000
    boot_time = 1599990000
    expected_uptime = mock_time - boot_time

    mocker.patch('time.time', return_value=mock_time)
    mock_module.run_command.return_value = (0, f'unix:0:system_misc:boot_time\t{boot_time}', '')

    uptime_facts = sunos_hardware.get_uptime_facts()

    assert uptime_facts['uptime_seconds'] == expected_uptime

def test_get_uptime_facts_failure(mocker, mock_module):
    sunos_hardware = SunOSHardware(mock_module)

    mock_module.run_command.return_value = (1, '', 'error')

    uptime_facts = sunos_hardware.get_uptime_facts()

    assert uptime_facts is None
