# file lib/ansible/module_utils/facts/hardware/darwin.py:79-90
# lines [79, 80, 81, 82, 83, 85, 86, 87, 88, 90]
# branches ['81->82', '81->85']

import pytest
from unittest.mock import MagicMock

# Assuming the DarwinHardware class is part of the module 'ansible.module_utils.facts.hardware.darwin'
from ansible.module_utils.facts.hardware.darwin import DarwinHardware

@pytest.fixture
def mock_sysctl_intel():
    return {
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-8650U CPU @ 1.90GHz',
        'machdep.cpu.core_count': '4',
        'hw.logicalcpu': '8'
    }

@pytest.fixture
def mock_sysctl_powerpc():
    return {
        'hw.physicalcpu': '2',
        'hw.logicalcpu': '4'
    }

@pytest.fixture
def mock_system_profile():
    return {
        'Processor Name': 'PowerPC G5',
        'Processor Speed': '2.0GHz'
    }

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.params = {}
    return module

def test_get_cpu_facts_intel(mock_sysctl_intel, mock_module, mocker):
    mocker.patch('ansible.module_utils.facts.hardware.darwin.DarwinHardware.get_system_profile', return_value={})
    darwin_hardware = DarwinHardware(mock_module)
    darwin_hardware.sysctl = mock_sysctl_intel

    cpu_facts = darwin_hardware.get_cpu_facts()

    assert cpu_facts['processor'] == mock_sysctl_intel['machdep.cpu.brand_string']
    assert cpu_facts['processor_cores'] == mock_sysctl_intel['machdep.cpu.core_count']
    assert cpu_facts['processor_vcpus'] == mock_sysctl_intel['hw.logicalcpu']

def test_get_cpu_facts_powerpc(mock_sysctl_powerpc, mock_system_profile, mock_module, mocker):
    mocker.patch('ansible.module_utils.facts.hardware.darwin.DarwinHardware.get_system_profile', return_value=mock_system_profile)
    darwin_hardware = DarwinHardware(mock_module)
    darwin_hardware.sysctl = mock_sysctl_powerpc

    cpu_facts = darwin_hardware.get_cpu_facts()

    expected_processor = '%s @ %s' % (mock_system_profile['Processor Name'], mock_system_profile['Processor Speed'])
    assert cpu_facts['processor'] == expected_processor
    assert cpu_facts['processor_cores'] == mock_sysctl_powerpc['hw.physicalcpu']
    assert cpu_facts['processor_vcpus'] == mock_sysctl_powerpc['hw.logicalcpu']
