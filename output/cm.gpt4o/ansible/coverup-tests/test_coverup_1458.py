# file lib/ansible/module_utils/facts/hardware/netbsd.py:67-99
# lines [83]
# branches ['82->83', '88->76']

import os
import pytest
from unittest.mock import patch, mock_open

# Assuming the NetBSDHardware class is imported from ansible.module_utils.facts.hardware.netbsd
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardware

@pytest.fixture
def mock_os_access(mocker):
    return mocker.patch('os.access', return_value=True)

@pytest.fixture
def mock_get_file_lines(mocker):
    cpuinfo_content = [
        "processor : 0\n",
        "model name : Intel(R) Xeon(R) CPU\n",
        "physical id : 0\n",
        "cpu cores : 4\n",
        "processor : 1\n",
        "model name : Intel(R) Xeon(R) CPU\n",
        "physical id : 0\n",
        "cpu cores : 4\n"
    ]
    return mocker.patch('ansible.module_utils.facts.hardware.netbsd.get_file_lines', return_value=cpuinfo_content)

@pytest.fixture
def mock_module(mocker):
    return mocker.Mock()

def test_get_cpu_facts(mock_os_access, mock_get_file_lines, mock_module):
    hardware = NetBSDHardware(mock_module)
    cpu_facts = hardware.get_cpu_facts()

    assert 'processor' in cpu_facts
    assert len(cpu_facts['processor']) == 2
    assert cpu_facts['processor'][0] == 'Intel(R) Xeon(R) CPU'
    assert cpu_facts['processor'][1] == 'Intel(R) Xeon(R) CPU'
    assert cpu_facts['processor_count'] == 1
    assert cpu_facts['processor_cores'] == 4
