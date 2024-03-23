# file lib/ansible/module_utils/facts/hardware/aix.py:38-55
# lines [38, 39, 41, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 55]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.hardware.aix import AIXHardware

@pytest.fixture
def aix_hardware(mocker):
    mocker.patch.object(AIXHardware, 'get_cpu_facts', return_value={'cpu': 'facts'})
    mocker.patch.object(AIXHardware, 'get_memory_facts', return_value={'memory': 'facts'})
    mocker.patch.object(AIXHardware, 'get_dmi_facts', return_value={'dmi': 'facts'})
    mocker.patch.object(AIXHardware, 'get_vgs_facts', return_value={'vgs': 'facts'})
    mocker.patch.object(AIXHardware, 'get_mount_facts', return_value={'mount': 'facts'})
    mocker.patch.object(AIXHardware, 'get_device_facts', return_value={'devices': 'facts'})
    module_mock = MagicMock()
    return AIXHardware(module=module_mock)

def test_aix_hardware_populate(aix_hardware):
    expected_facts = {
        'cpu': 'facts',
        'memory': 'facts',
        'dmi': 'facts',
        'vgs': 'facts',
        'mount': 'facts',
        'devices': 'facts'
    }
    facts = aix_hardware.populate()
    assert facts == expected_facts
