# file lib/ansible/module_utils/facts/hardware/hpux.py:54-104
# lines [55, 56, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 79, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 93, 94, 95, 97, 98, 99, 100, 101, 102, 104]
# branches ['58->59', '58->62', '62->63', '62->104', '63->64', '63->72', '65->66', '65->67', '68->69', '68->70', '72->74', '72->104', '75->76', '75->97', '81->82', '81->84', '87->88', '87->90', '90->91', '90->93']

import re
import pytest
from unittest.mock import MagicMock

# Assuming the HPUXHardware class is part of a module named hpux
from ansible.module_utils.facts.hardware import hpux

# Mock the run_command method to return predefined outputs
def mock_run_command(cmd, use_unsafe_shell):
    if "ioscan -FkCprocessor | wc -l" in cmd:
        return 0, "4", ""
    elif "/usr/contrib/bin/machinfo | grep 'Number of CPUs'" in cmd:
        return 0, "Number of CPUs = 2", ""
    elif "/usr/contrib/bin/machinfo | grep 'processor family'" in cmd:
        return 0, "processor family: Intel(R) Itanium(R) Processor 9500", ""
    elif "/usr/contrib/bin/machinfo | grep core | wc -l" in cmd:
        return 0, "0", ""
    elif "/usr/contrib/bin/machinfo | grep Intel" in cmd and "cut -d' ' -f4-" in cmd:
        return 0, "Intel(R) Itanium(R) Processor 9500", ""
    elif "/usr/contrib/bin/machinfo | grep Intel" in cmd:
        return 0, "4 Intel(R) Itanium(R) Processor 9500", ""
    elif "/usr/sbin/psrset | grep LCPU" in cmd:
        return 0, "LCPU ON", ""
    elif "/usr/contrib/bin/machinfo | grep logical" in cmd:
        return 0, "8 logical", ""
    elif "/usr/contrib/bin/machinfo | egrep 'socket[s]?$' | tail -1" in cmd:
        return 0, "2 sockets", ""
    elif "/usr/contrib/bin/machinfo | grep -e '[0-9] core' | tail -1" in cmd:
        return 0, "4 core", ""
    else:
        return 0, "", ""

# Test function to cover lines 55-104
@pytest.fixture
def hpux_hardware(mocker):
    module_mock = MagicMock()
    module_mock.run_command = MagicMock(side_effect=mock_run_command)
    hardware = hpux.HPUXHardware(module=module_mock)
    return hardware

def test_get_cpu_facts_hpux_architecture_9000_800(hpux_hardware):
    collected_facts = {'ansible_architecture': '9000/800'}
    cpu_facts = hpux_hardware.get_cpu_facts(collected_facts)
    assert cpu_facts['processor_count'] == 4

def test_get_cpu_facts_hpux_architecture_ia64_B_11_23(hpux_hardware):
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': "B.11.23"}
    cpu_facts = hpux_hardware.get_cpu_facts(collected_facts)
    assert cpu_facts['processor_count'] == 2
    assert cpu_facts['processor'] == "Intel(R) Itanium(R) Processor 9500"
    assert cpu_facts['processor_cores'] == 4

def test_get_cpu_facts_hpux_architecture_ia64_B_11_31_without_hyperthreading(hpux_hardware):
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': "B.11.31"}
    cpu_facts = hpux_hardware.get_cpu_facts(collected_facts)
    assert cpu_facts['processor_count'] == 4
    assert cpu_facts['processor_cores'] == 4
    assert cpu_facts['processor'] == "Intel(R) Itanium(R) Processor 9500"

def test_get_cpu_facts_hpux_architecture_ia64_B_11_31_with_hyperthreading(hpux_hardware):
    collected_facts = {'ansible_architecture': 'ia64', 'ansible_distribution_version': "B.11.31"}
    cpu_facts = hpux_hardware.get_cpu_facts(collected_facts)
    assert cpu_facts['processor_count'] == 4
    assert cpu_facts['processor_cores'] == int(8 / 2)  # Hyperthreading ON, cores divided by 2
    assert cpu_facts['processor'] == "Intel(R) Itanium(R) Processor 9500"
