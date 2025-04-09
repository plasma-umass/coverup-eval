# file: lib/ansible/module_utils/facts/hardware/aix.py:38-55
# asked: {"lines": [38, 39, 41, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 55], "branches": []}
# gained: {"lines": [38, 39, 41, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 55], "branches": []}

import pytest
from unittest.mock import patch, MagicMock

# Assuming the AIXHardware class is imported from the module
from ansible.module_utils.facts.hardware.aix import AIXHardware

@pytest.fixture
def aix_hardware():
    module_mock = MagicMock()
    return AIXHardware(module=module_mock)

def test_populate(aix_hardware):
    with patch.object(aix_hardware, 'get_cpu_facts', return_value={'cpu': 'test_cpu'}), \
         patch.object(aix_hardware, 'get_memory_facts', return_value={'memory': 'test_memory'}), \
         patch.object(aix_hardware, 'get_dmi_facts', return_value={'dmi': 'test_dmi'}), \
         patch.object(aix_hardware, 'get_vgs_facts', return_value={'vgs': 'test_vgs'}), \
         patch.object(aix_hardware, 'get_mount_facts', return_value={'mount': 'test_mount'}), \
         patch.object(aix_hardware, 'get_device_facts', return_value={'devices': 'test_devices'}):
        
        result = aix_hardware.populate()
        
        expected_result = {
            'cpu': 'test_cpu',
            'memory': 'test_memory',
            'dmi': 'test_dmi',
            'vgs': 'test_vgs',
            'mount': 'test_mount',
            'devices': 'test_devices'
        }
        
        assert result == expected_result
