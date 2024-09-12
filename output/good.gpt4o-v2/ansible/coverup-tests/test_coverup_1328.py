# file: lib/ansible/module_utils/facts/hardware/hpux.py:54-104
# asked: {"lines": [55, 56, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 79, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 93, 94, 95, 97, 98, 99, 100, 101, 102, 104], "branches": [[58, 59], [58, 62], [62, 63], [62, 104], [63, 64], [63, 72], [65, 66], [65, 67], [68, 69], [68, 70], [72, 74], [72, 104], [75, 76], [75, 97], [81, 82], [81, 84], [87, 88], [87, 90], [90, 91], [90, 93]]}
# gained: {"lines": [55, 56, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 79, 80, 81, 84, 85, 86, 87, 90, 93, 94, 95, 97, 98, 99, 100, 101, 102, 104], "branches": [[58, 59], [58, 62], [62, 63], [63, 64], [63, 72], [65, 66], [68, 69], [72, 74], [72, 104], [75, 76], [75, 97], [81, 84], [87, 90], [90, 93]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.hardware.hpux import HPUXHardware

@pytest.fixture
def hpux_hardware():
    module = Mock()
    return HPUXHardware(module)

def test_get_cpu_facts_architecture_9000_800(hpux_hardware):
    hpux_hardware.module.run_command = Mock(return_value=(0, "4\n", ""))
    collected_facts = {'ansible_architecture': '9000/800'}
    cpu_facts = hpux_hardware.get_cpu_facts(collected_facts)
    assert cpu_facts['processor_count'] == 4

def test_get_cpu_facts_architecture_ia64_B_11_23(hpux_hardware):
    hpux_hardware.module.run_command = Mock(side_effect=[
        (0, "Number of CPUs = 8\n", ""),
        (0, "processor family = Intel Itanium\n", ""),
        (0, "4\n", "")
    ])
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.23'}
    cpu_facts = hpux_hardware.get_cpu_facts(collected_facts)
    assert cpu_facts['processor_count'] == 8
    assert cpu_facts['processor'] == 'Intel Itanium'
    assert cpu_facts['processor_cores'] == 4

def test_get_cpu_facts_architecture_ia64_B_11_31_no_cores(hpux_hardware):
    hpux_hardware.module.run_command = Mock(side_effect=[
        (0, "0\n", ""),
        (0, "8 Intel Itanium\n", ""),
        (0, "LCPU 16\n", ""),
        (0, "16 logical processors\n", ""),
        (0, "Intel Itanium\n", "")
    ])
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'}
    cpu_facts = hpux_hardware.get_cpu_facts(collected_facts)
    assert cpu_facts['processor_count'] == 8
    assert cpu_facts['processor_cores'] == 16
    assert cpu_facts['processor'] == 'Intel Itanium'

def test_get_cpu_facts_architecture_ia64_B_11_31_with_cores(hpux_hardware):
    hpux_hardware.module.run_command = Mock(side_effect=[
        (0, "2\n", ""),
        (0, "4 socket\n", ""),
        (0, "8 core\n", ""),
        (0, "Intel Itanium\n", "")
    ])
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': 'B.11.31'}
    cpu_facts = hpux_hardware.get_cpu_facts(collected_facts)
    assert cpu_facts['processor_count'] == 4
    assert cpu_facts['processor_cores'] == 8
    assert cpu_facts['processor'] == 'Intel Itanium'
