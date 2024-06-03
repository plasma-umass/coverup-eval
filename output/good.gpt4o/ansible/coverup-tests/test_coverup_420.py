# file lib/ansible/module_utils/facts/hardware/darwin.py:79-90
# lines [79, 80, 81, 82, 83, 85, 86, 87, 88, 90]
# branches ['81->82', '81->85']

import pytest
from unittest.mock import patch, MagicMock

# Assuming the DarwinHardware class is imported from ansible.module_utils.facts.hardware.darwin
from ansible.module_utils.facts.hardware.darwin import DarwinHardware

@pytest.fixture
def darwin_hardware(mocker):
    module_mock = MagicMock()
    darwin_hardware = DarwinHardware(module_mock)
    darwin_hardware.sysctl = {}
    return darwin_hardware

def test_get_cpu_facts_intel(darwin_hardware, mocker):
    sysctl_mock = {
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz',
        'machdep.cpu.core_count': 4,
        'hw.logicalcpu': 8
    }
    darwin_hardware.sysctl = sysctl_mock
    
    cpu_facts = darwin_hardware.get_cpu_facts()
    
    assert cpu_facts['processor'] == 'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz'
    assert cpu_facts['processor_cores'] == 4
    assert cpu_facts['processor_vcpus'] == 8

def test_get_cpu_facts_powerpc(darwin_hardware, mocker):
    sysctl_mock = {
        'hw.physicalcpu': 2,
        'hw.logicalcpu': 4
    }
    system_profile_mock = {
        'Processor Name': 'PowerPC G4',
        'Processor Speed': '1.25 GHz'
    }
    darwin_hardware.sysctl = sysctl_mock
    mocker.patch.object(darwin_hardware, 'get_system_profile', return_value=system_profile_mock)
    
    cpu_facts = darwin_hardware.get_cpu_facts()
    
    assert cpu_facts['processor'] == 'PowerPC G4 @ 1.25 GHz'
    assert cpu_facts['processor_cores'] == 2
    assert cpu_facts['processor_vcpus'] == 4

def test_get_cpu_facts_no_logicalcpu(darwin_hardware, mocker):
    sysctl_mock = {
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz',
        'machdep.cpu.core_count': 4,
        'hw.ncpu': 8
    }
    darwin_hardware.sysctl = sysctl_mock
    
    cpu_facts = darwin_hardware.get_cpu_facts()
    
    assert cpu_facts['processor'] == 'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz'
    assert cpu_facts['processor_cores'] == 4
    assert cpu_facts['processor_vcpus'] == 8
