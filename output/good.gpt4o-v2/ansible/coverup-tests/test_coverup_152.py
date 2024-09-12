# file: lib/ansible/module_utils/facts/hardware/sunos.py:37-65
# asked: {"lines": [37, 38, 43, 44, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 65], "branches": []}
# gained: {"lines": [37, 38, 43, 44, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 65], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.hardware.sunos import SunOSHardware
from ansible.module_utils.common.locale import get_best_parsable_locale
from ansible.module_utils.facts import timeout

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.run_command.return_value = (0, 'C.utf8\nen_US.utf8\nC\nPOSIX', '')
    module.get_bin_path.return_value = '/usr/bin/locale'
    return module

@pytest.fixture
def sunos_hardware(mock_module):
    hardware = SunOSHardware(mock_module)
    return hardware

def test_populate_success(sunos_hardware):
    with patch.object(sunos_hardware, 'get_cpu_facts', return_value={'cpu': 'info'}), \
         patch.object(sunos_hardware, 'get_memory_facts', return_value={'memory': 'info'}), \
         patch.object(sunos_hardware, 'get_dmi_facts', return_value={'dmi': 'info'}), \
         patch.object(sunos_hardware, 'get_device_facts', return_value={'device': 'info'}), \
         patch.object(sunos_hardware, 'get_uptime_facts', return_value={'uptime': 'info'}), \
         patch.object(sunos_hardware, 'get_mount_facts', return_value={'mount': 'info'}):
        
        result = sunos_hardware.populate()
        
        assert result == {
            'cpu': 'info',
            'memory': 'info',
            'dmi': 'info',
            'device': 'info',
            'uptime': 'info',
            'mount': 'info'
        }

def test_populate_timeout(sunos_hardware):
    with patch.object(sunos_hardware, 'get_cpu_facts', return_value={'cpu': 'info'}), \
         patch.object(sunos_hardware, 'get_memory_facts', return_value={'memory': 'info'}), \
         patch.object(sunos_hardware, 'get_dmi_facts', return_value={'dmi': 'info'}), \
         patch.object(sunos_hardware, 'get_device_facts', return_value={'device': 'info'}), \
         patch.object(sunos_hardware, 'get_uptime_facts', return_value={'uptime': 'info'}), \
         patch.object(sunos_hardware, 'get_mount_facts', side_effect=timeout.TimeoutError):
        
        result = sunos_hardware.populate()
        
        assert result == {
            'cpu': 'info',
            'memory': 'info',
            'dmi': 'info',
            'device': 'info',
            'uptime': 'info'
        }
