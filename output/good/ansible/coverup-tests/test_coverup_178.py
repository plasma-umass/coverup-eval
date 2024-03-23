# file lib/ansible/module_utils/facts/hardware/sunos.py:37-65
# lines [37, 38, 43, 44, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 65]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.hardware.sunos import SunOSHardware
from ansible.module_utils.facts.timeout import TimeoutError

@pytest.fixture
def mock_module(mocker):
    mock_module = MagicMock()
    mock_module.run_command_environ_update = {}
    return mock_module

@pytest.fixture
def sunos_hardware(mock_module):
    return SunOSHardware(module=mock_module)

def test_populate_sunos_hardware(mocker, sunos_hardware):
    mocker.patch('ansible.module_utils.facts.hardware.sunos.get_best_parsable_locale', return_value='C')
    mocker.patch.object(sunos_hardware, 'get_cpu_facts', return_value={'cpu': 'some_cpu_info'})
    mocker.patch.object(sunos_hardware, 'get_memory_facts', return_value={'memory': 'some_memory_info'})
    mocker.patch.object(sunos_hardware, 'get_dmi_facts', return_value={'dmi': 'some_dmi_info'})
    mocker.patch.object(sunos_hardware, 'get_device_facts', return_value={'device': 'some_device_info'})
    mocker.patch.object(sunos_hardware, 'get_uptime_facts', return_value={'uptime': 'some_uptime_info'})
    mocker.patch.object(sunos_hardware, 'get_mount_facts', side_effect=TimeoutError)

    hardware_facts = sunos_hardware.populate()

    assert hardware_facts['cpu'] == 'some_cpu_info'
    assert hardware_facts['memory'] == 'some_memory_info'
    assert hardware_facts['dmi'] == 'some_dmi_info'
    assert hardware_facts['device'] == 'some_device_info'
    assert hardware_facts['uptime'] == 'some_uptime_info'
    assert 'mount' not in hardware_facts  # mount_facts should be empty due to TimeoutError

    # Ensure locale environment variables are set correctly
    assert sunos_hardware.module.run_command_environ_update == {
        'LANG': 'C',
        'LC_ALL': 'C',
        'LC_NUMERIC': 'C'
    }
