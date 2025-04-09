# file: lib/ansible/module_utils/facts/hardware/sunos.py:37-65
# asked: {"lines": [38, 43, 44, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 65], "branches": []}
# gained: {"lines": [38, 43, 44, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 65], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.hardware.sunos import SunOSHardware
from ansible.module_utils.facts.timeout import TimeoutError

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.get_bin_path.return_value = '/usr/bin/locale'
    module.run_command.return_value = (0, 'C.utf8\nen_US.utf8\nC\nPOSIX', '')
    return module

@pytest.fixture
def sunos_hardware(mock_module):
    return SunOSHardware(module=mock_module)

def test_populate_all_branches(sunos_hardware, mock_module):
    with patch.object(sunos_hardware, 'get_cpu_facts', return_value={'cpu': 'facts'}), \
         patch.object(sunos_hardware, 'get_memory_facts', return_value={'memory': 'facts'}), \
         patch.object(sunos_hardware, 'get_dmi_facts', return_value={'dmi': 'facts'}), \
         patch.object(sunos_hardware, 'get_device_facts', return_value={'device': 'facts'}), \
         patch.object(sunos_hardware, 'get_uptime_facts', return_value={'uptime': 'facts'}), \
         patch.object(sunos_hardware, 'get_mount_facts', return_value={'mount': 'facts'}):
        
        hardware_facts = sunos_hardware.populate()
        
        assert hardware_facts == {
            'cpu': 'facts',
            'memory': 'facts',
            'dmi': 'facts',
            'device': 'facts',
            'uptime': 'facts',
            'mount': 'facts'
        }

def test_populate_mount_timeout(sunos_hardware, mock_module):
    with patch.object(sunos_hardware, 'get_cpu_facts', return_value={'cpu': 'facts'}), \
         patch.object(sunos_hardware, 'get_memory_facts', return_value={'memory': 'facts'}), \
         patch.object(sunos_hardware, 'get_dmi_facts', return_value={'dmi': 'facts'}), \
         patch.object(sunos_hardware, 'get_device_facts', return_value={'device': 'facts'}), \
         patch.object(sunos_hardware, 'get_uptime_facts', return_value={'uptime': 'facts'}), \
         patch.object(sunos_hardware, 'get_mount_facts', side_effect=TimeoutError):
        
        hardware_facts = sunos_hardware.populate()
        
        assert hardware_facts == {
            'cpu': 'facts',
            'memory': 'facts',
            'dmi': 'facts',
            'device': 'facts',
            'uptime': 'facts'
        }
