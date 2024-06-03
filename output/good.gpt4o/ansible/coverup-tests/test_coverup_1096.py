# file lib/ansible/module_utils/facts/hardware/sunos.py:37-65
# lines [38, 43, 44, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 65]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.hardware.sunos import SunOSHardware
from ansible.module_utils.facts.hardware.base import Hardware
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.facts.timeout import TimeoutError

@pytest.fixture
def mock_module():
    module = MagicMock(spec=AnsibleModule)
    return module

@pytest.fixture
def sunos_hardware(mock_module):
    return SunOSHardware(mock_module)

@patch('ansible.module_utils.facts.hardware.sunos.get_best_parsable_locale')
@patch.object(SunOSHardware, 'get_cpu_facts', return_value={'cpu': 'test_cpu'})
@patch.object(SunOSHardware, 'get_memory_facts', return_value={'memory': 'test_memory'})
@patch.object(SunOSHardware, 'get_dmi_facts', return_value={'dmi': 'test_dmi'})
@patch.object(SunOSHardware, 'get_device_facts', return_value={'device': 'test_device'})
@patch.object(SunOSHardware, 'get_uptime_facts', return_value={'uptime': 'test_uptime'})
@patch.object(SunOSHardware, 'get_mount_facts', side_effect=TimeoutError)
def test_populate_handles_timeout(mock_get_mount_facts, mock_get_uptime_facts, mock_get_device_facts, mock_get_dmi_facts, mock_get_memory_facts, mock_get_cpu_facts, mock_get_best_parsable_locale, sunos_hardware):
    mock_get_best_parsable_locale.return_value = 'C'
    
    result = sunos_hardware.populate()
    
    mock_get_best_parsable_locale.assert_called_once_with(sunos_hardware.module)
    assert sunos_hardware.module.run_command_environ_update == {'LANG': 'C', 'LC_ALL': 'C', 'LC_NUMERIC': 'C'}
    mock_get_cpu_facts.assert_called_once()
    mock_get_memory_facts.assert_called_once()
    mock_get_dmi_facts.assert_called_once()
    mock_get_device_facts.assert_called_once()
    mock_get_uptime_facts.assert_called_once()
    mock_get_mount_facts.assert_called_once()
    
    assert result == {
        'cpu': 'test_cpu',
        'memory': 'test_memory',
        'dmi': 'test_dmi',
        'device': 'test_device',
        'uptime': 'test_uptime'
    }
