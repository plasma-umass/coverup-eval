# file lib/ansible/module_utils/facts/hardware/sunos.py:67-120
# lines [67, 68, 69, 71, 72, 74, 76, 78, 79, 80, 82, 83, 86, 87, 88, 89, 90, 91, 92, 93, 96, 97, 98, 99, 100, 101, 102, 103, 104, 106, 113, 114, 115, 117, 118, 120]
# branches ['78->79', '78->113', '79->80', '79->82', '86->87', '86->88', '88->89', '88->90', '90->91', '90->92', '92->93', '92->101', '96->97', '96->98', '98->99', '98->100', '101->78', '101->102', '103->104', '103->106', '113->114', '113->117']

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def sunos_hardware(mock_module):
    return SunOSHardware(module=mock_module)

def test_get_cpu_facts(sunos_hardware, mocker):
    mocker.patch.object(sunos_hardware.module, 'run_command', return_value=(0, """
module: cpu_info
brand  Intel(R) Xeon(R) CPU
clock_MHz  2400
implementation  x86
chip_id  0
chip_id  1
""", ""))

    collected_facts = {'ansible_machine': 'i86pc'}
    cpu_facts = sunos_hardware.get_cpu_facts(collected_facts)

    assert 'processor' in cpu_facts
    assert len(cpu_facts['processor']) == 1
    assert cpu_facts['processor'][0] == 'Intel(R) Xeon(R) CPU'
    assert cpu_facts['processor_count'] == 2
    assert cpu_facts['processor_cores'] == 2

def test_get_cpu_facts_sparc(sunos_hardware, mocker):
    mocker.patch.object(sunos_hardware.module, 'run_command', return_value=(0, """
module: cpu_info
brand  SPARC64
clock_MHz  1200
implementation  sparcv9
chip_id  0
chip_id  0
""", ""))

    collected_facts = {'ansible_machine': 'sparc'}
    cpu_facts = sunos_hardware.get_cpu_facts(collected_facts)

    assert 'processor' in cpu_facts
    assert len(cpu_facts['processor']) == 1
    assert cpu_facts['processor'][0] == 'SPARC64 @ 1200MHz'
    assert cpu_facts['processor_count'] == 1
    assert cpu_facts['processor_cores'] == 2

def test_get_cpu_facts_no_sockets(sunos_hardware, mocker):
    mocker.patch.object(sunos_hardware.module, 'run_command', return_value=(0, """
module: cpu_info
brand  Intel(R) Xeon(R) CPU
clock_MHz  2400
implementation  x86
""", ""))

    collected_facts = {'ansible_machine': 'i86pc'}
    cpu_facts = sunos_hardware.get_cpu_facts(collected_facts)

    assert 'processor' in cpu_facts
    assert len(cpu_facts['processor']) == 1
    assert cpu_facts['processor'][0] == 'Intel(R) Xeon(R) CPU'
    assert cpu_facts['processor_count'] == 1
    assert cpu_facts['processor_cores'] == 'NA'
