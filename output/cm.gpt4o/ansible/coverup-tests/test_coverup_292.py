# file lib/ansible/module_utils/facts/hardware/aix.py:38-55
# lines [38, 39, 41, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 55]
# branches []

import pytest
from unittest.mock import patch, Mock

# Assuming the AIXHardware class is imported from ansible.module_utils.facts.hardware.aix
from ansible.module_utils.facts.hardware.aix import AIXHardware

@pytest.fixture
def mock_hardware_methods(mocker):
    mocker.patch.object(AIXHardware, 'get_cpu_facts', return_value={'cpu': 'test_cpu'})
    mocker.patch.object(AIXHardware, 'get_memory_facts', return_value={'memory': 'test_memory'})
    mocker.patch.object(AIXHardware, 'get_dmi_facts', return_value={'dmi': 'test_dmi'})
    mocker.patch.object(AIXHardware, 'get_vgs_facts', return_value={'vgs': 'test_vgs'})
    mocker.patch.object(AIXHardware, 'get_mount_facts', return_value={'mount': 'test_mount'})
    mocker.patch.object(AIXHardware, 'get_device_facts', return_value={'devices': 'test_devices'})

def test_populate(mock_hardware_methods):
    mock_module = Mock()
    hardware = AIXHardware(mock_module)
    result = hardware.populate()
    
    expected_result = {
        'cpu': 'test_cpu',
        'memory': 'test_memory',
        'dmi': 'test_dmi',
        'vgs': 'test_vgs',
        'mount': 'test_mount',
        'devices': 'test_devices'
    }
    
    assert result == expected_result
