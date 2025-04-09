# file: lib/ansible/module_utils/facts/hardware/aix.py:38-55
# asked: {"lines": [38, 39, 41, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 55], "branches": []}
# gained: {"lines": [38, 39, 41, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 55], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.hardware.aix import AIXHardware

@pytest.fixture
def module():
    return MagicMock()

@pytest.fixture
def aix_hardware(module):
    return AIXHardware(module)

def test_populate(aix_hardware, module):
    # Mock the return values of the methods called within populate
    aix_hardware.get_cpu_facts = MagicMock(return_value={'cpu': 'cpu_facts'})
    aix_hardware.get_memory_facts = MagicMock(return_value={'memory': 'memory_facts'})
    aix_hardware.get_dmi_facts = MagicMock(return_value={'dmi': 'dmi_facts'})
    aix_hardware.get_vgs_facts = MagicMock(return_value={'vgs': 'vgs_facts'})
    aix_hardware.get_mount_facts = MagicMock(return_value={'mount': 'mount_facts'})
    aix_hardware.get_device_facts = MagicMock(return_value={'device': 'device_facts'})

    # Call the method
    result = aix_hardware.populate()

    # Assertions to verify that the method calls were made and the result is as expected
    aix_hardware.get_cpu_facts.assert_called_once()
    aix_hardware.get_memory_facts.assert_called_once()
    aix_hardware.get_dmi_facts.assert_called_once()
    aix_hardware.get_vgs_facts.assert_called_once()
    aix_hardware.get_mount_facts.assert_called_once()
    aix_hardware.get_device_facts.assert_called_once()

    assert result == {
        'cpu': 'cpu_facts',
        'memory': 'memory_facts',
        'dmi': 'dmi_facts',
        'vgs': 'vgs_facts',
        'mount': 'mount_facts',
        'device': 'device_facts'
    }
