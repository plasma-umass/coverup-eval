# file: lib/ansible/module_utils/facts/hardware/sunos.py:67-120
# asked: {"lines": [67, 68, 69, 71, 72, 74, 76, 78, 79, 80, 82, 83, 86, 87, 88, 89, 90, 91, 92, 93, 96, 97, 98, 99, 100, 101, 102, 103, 104, 106, 113, 114, 115, 117, 118, 120], "branches": [[78, 79], [78, 113], [79, 80], [79, 82], [86, 87], [86, 88], [88, 89], [88, 90], [90, 91], [90, 92], [92, 93], [92, 101], [96, 97], [96, 98], [98, 99], [98, 100], [101, 78], [101, 102], [103, 104], [103, 106], [113, 114], [113, 117]]}
# gained: {"lines": [67, 68, 69, 71, 72, 74, 76, 78, 79, 80, 82, 83, 86, 87, 88, 89, 90, 91, 92, 93, 96, 97, 98, 99, 100, 101, 102, 103, 104, 106, 113, 114, 115, 117, 118, 120], "branches": [[78, 79], [78, 113], [79, 80], [79, 82], [86, 87], [86, 88], [88, 89], [88, 90], [90, 91], [90, 92], [92, 93], [92, 101], [96, 97], [96, 98], [98, 99], [101, 102], [103, 104], [103, 106], [113, 114], [113, 117]]}

import pytest
from unittest.mock import Mock, patch

# Assuming the SunOSHardware class is imported from the module
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

@pytest.fixture
def sunos_hardware():
    module = Mock()
    return SunOSHardware(module)

def test_get_cpu_facts_no_output(sunos_hardware):
    sunos_hardware.module.run_command = Mock(return_value=(0, "", ""))
    result = sunos_hardware.get_cpu_facts()
    assert result == {'processor': [], 'processor_cores': 'NA', 'processor_count': 0}

def test_get_cpu_facts_with_output(sunos_hardware):
    output = """
module: cpu_info
brand Intel(R) Xeon(R) CPU
clock_MHz 2400
implementation x86_64
chip_id 0
chip_id 1
"""
    sunos_hardware.module.run_command = Mock(return_value=(0, output, ""))
    collected_facts = {'ansible_machine': 'i86pc'}
    result = sunos_hardware.get_cpu_facts(collected_facts)
    assert result['processor'] == ['Intel(R) Xeon(R) CPU']
    assert result['processor_cores'] == 2
    assert result['processor_count'] == 2

def test_get_cpu_facts_with_sparc(sunos_hardware):
    output = """
module: cpu_info
brand SPARC64-VII
clock_MHz 2400
implementation sparc
chip_id 0
"""
    sunos_hardware.module.run_command = Mock(return_value=(0, output, ""))
    collected_facts = {'ansible_machine': 'sun4v'}
    result = sunos_hardware.get_cpu_facts(collected_facts)
    assert result['processor'] == ['SPARC64-VII @ 2400MHz']
    assert result['processor_cores'] == 1
    assert result['processor_count'] == 1

def test_get_cpu_facts_multiple_chips(sunos_hardware):
    output = """
module: cpu_info
brand Intel(R) Xeon(R) CPU
clock_MHz 2400
implementation x86_64
chip_id 0
chip_id 0
chip_id 1
"""
    sunos_hardware.module.run_command = Mock(return_value=(0, output, ""))
    collected_facts = {'ansible_machine': 'i86pc'}
    result = sunos_hardware.get_cpu_facts(collected_facts)
    assert result['processor'] == ['Intel(R) Xeon(R) CPU']
    assert result['processor_cores'] == 3
    assert result['processor_count'] == 2

def test_get_cpu_facts_no_chip_id(sunos_hardware):
    output = """
module: cpu_info
brand Intel(R) Xeon(R) CPU
clock_MHz 2400
implementation x86_64
"""
    sunos_hardware.module.run_command = Mock(return_value=(0, output, ""))
    collected_facts = {'ansible_machine': 'i86pc'}
    result = sunos_hardware.get_cpu_facts(collected_facts)
    assert result['processor'] == ['Intel(R) Xeon(R) CPU']
    assert result['processor_cores'] == 'NA'
    assert result['processor_count'] == 1
