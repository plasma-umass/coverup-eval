# file: lib/ansible/module_utils/facts/hardware/darwin.py:79-90
# asked: {"lines": [79, 80, 81, 82, 83, 85, 86, 87, 88, 90], "branches": [[81, 82], [81, 85]]}
# gained: {"lines": [79, 80, 81, 82, 83, 85, 86, 87, 88, 90], "branches": [[81, 82], [81, 85]]}

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.hardware.darwin import DarwinHardware

@pytest.fixture
def darwin_hardware(mocker):
    module = mocker.MagicMock()
    dh = DarwinHardware(module)
    dh.sysctl = {}
    return dh

def test_get_cpu_facts_intel(darwin_hardware, mocker):
    darwin_hardware.sysctl = {
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz',
        'machdep.cpu.core_count': 4,
        'hw.logicalcpu': 8
    }
    cpu_facts = darwin_hardware.get_cpu_facts()
    assert cpu_facts['processor'] == 'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz'
    assert cpu_facts['processor_cores'] == 4
    assert cpu_facts['processor_vcpus'] == 8

def test_get_cpu_facts_powerpc(darwin_hardware, mocker):
    darwin_hardware.sysctl = {
        'hw.physicalcpu': 2,
        'hw.ncpu': 4
    }
    mocker.patch.object(darwin_hardware, 'get_system_profile', return_value={
        'Processor Name': 'PowerPC G4',
        'Processor Speed': '1.25 GHz'
    })
    cpu_facts = darwin_hardware.get_cpu_facts()
    assert cpu_facts['processor'] == 'PowerPC G4 @ 1.25 GHz'
    assert cpu_facts['processor_cores'] == 2
    assert cpu_facts['processor_vcpus'] == 4

def test_get_cpu_facts_no_logicalcpu(darwin_hardware, mocker):
    darwin_hardware.sysctl = {
        'machdep.cpu.brand_string': 'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz',
        'machdep.cpu.core_count': 4,
        'hw.ncpu': 8
    }
    cpu_facts = darwin_hardware.get_cpu_facts()
    assert cpu_facts['processor'] == 'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz'
    assert cpu_facts['processor_cores'] == 4
    assert cpu_facts['processor_vcpus'] == 8
