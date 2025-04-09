# file: lib/ansible/module_utils/facts/hardware/sunos.py:37-65
# asked: {"lines": [37, 38, 43, 44, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 65], "branches": []}
# gained: {"lines": [37, 38, 43, 44, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 65], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.hardware.sunos import SunOSHardware
from ansible.module_utils.facts.timeout import TimeoutError

@pytest.fixture
def module():
    module = MagicMock()
    module.run_command.return_value = (0, 'C\nC.utf8\nPOSIX\n', '')
    return module

@pytest.fixture
def sunos_hardware(module):
    return SunOSHardware(module)

def test_populate_all_branches(sunos_hardware, module):
    # Mocking the methods to return sample data
    sunos_hardware.get_cpu_facts = MagicMock(return_value={'cpu': 'cpu_facts'})
    sunos_hardware.get_memory_facts = MagicMock(return_value={'memory': 'memory_facts'})
    sunos_hardware.get_dmi_facts = MagicMock(return_value={'dmi': 'dmi_facts'})
    sunos_hardware.get_device_facts = MagicMock(return_value={'device': 'device_facts'})
    sunos_hardware.get_uptime_facts = MagicMock(return_value={'uptime': 'uptime_facts'})
    sunos_hardware.get_mount_facts = MagicMock(return_value={'mount': 'mount_facts'})

    # Mocking get_best_parsable_locale
    with patch('ansible.module_utils.common.locale.get_best_parsable_locale', return_value='C'):
        hardware_facts = sunos_hardware.populate()

    assert hardware_facts == {
        'cpu': 'cpu_facts',
        'memory': 'memory_facts',
        'dmi': 'dmi_facts',
        'device': 'device_facts',
        'uptime': 'uptime_facts',
        'mount': 'mount_facts'
    }

def test_populate_timeout(sunos_hardware, module):
    # Mocking the methods to return sample data
    sunos_hardware.get_cpu_facts = MagicMock(return_value={'cpu': 'cpu_facts'})
    sunos_hardware.get_memory_facts = MagicMock(return_value={'memory': 'memory_facts'})
    sunos_hardware.get_dmi_facts = MagicMock(return_value={'dmi': 'dmi_facts'})
    sunos_hardware.get_device_facts = MagicMock(return_value={'device': 'device_facts'})
    sunos_hardware.get_uptime_facts = MagicMock(return_value={'uptime': 'uptime_facts'})
    sunos_hardware.get_mount_facts = MagicMock(side_effect=TimeoutError)

    # Mocking get_best_parsable_locale
    with patch('ansible.module_utils.common.locale.get_best_parsable_locale', return_value='C'):
        hardware_facts = sunos_hardware.populate()

    assert hardware_facts == {
        'cpu': 'cpu_facts',
        'memory': 'memory_facts',
        'dmi': 'dmi_facts',
        'device': 'device_facts',
        'uptime': 'uptime_facts'
    }
