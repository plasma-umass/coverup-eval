# file: lib/ansible/module_utils/facts/hardware/aix.py:38-55
# asked: {"lines": [38, 39, 41, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 55], "branches": []}
# gained: {"lines": [38, 39, 41, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 55], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.hardware.aix import AIXHardware

@pytest.fixture
def aix_hardware():
    module = MagicMock()
    return AIXHardware(module)

def test_populate(aix_hardware):
    with patch.object(aix_hardware, 'get_cpu_facts', return_value={'cpu': 'cpu_facts'}), \
         patch.object(aix_hardware, 'get_memory_facts', return_value={'memory': 'memory_facts'}), \
         patch.object(aix_hardware, 'get_dmi_facts', return_value={'dmi': 'dmi_facts'}), \
         patch.object(aix_hardware, 'get_vgs_facts', return_value={'vgs': 'vgs_facts'}), \
         patch.object(aix_hardware, 'get_mount_facts', return_value={'mount': 'mount_facts'}), \
         patch.object(aix_hardware, 'get_device_facts', return_value={'devices': 'devices_facts'}):
        
        result = aix_hardware.populate()
        
        expected_result = {
            'cpu': 'cpu_facts',
            'memory': 'memory_facts',
            'dmi': 'dmi_facts',
            'vgs': 'vgs_facts',
            'mount': 'mount_facts',
            'devices': 'devices_facts'
        }
        
        assert result == expected_result
