# file lib/ansible/module_utils/facts/hardware/netbsd.py:67-99
# lines [67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 96, 97, 99]
# branches ['73->74', '73->75', '76->77', '76->92', '81->82', '81->86', '82->83', '82->84', '86->87', '86->90', '88->76', '88->89', '90->76', '90->91', '92->93', '92->96']

import os
import pytest
from unittest.mock import patch, mock_open
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardware
from ansible.module_utils.basic import AnsibleModule

@pytest.fixture
def mock_os_access(mocker):
    return mocker.patch('os.access', return_value=True)

@pytest.fixture
def mock_get_file_lines(mocker):
    cpuinfo_content = [
        "processor\t: 0\n",
        "model name\t: Intel(R) Xeon(R) CPU\n",
        "physical id\t: 0\n",
        "cpu cores\t: 4\n",
        "processor\t: 1\n",
        "model name\t: Intel(R) Xeon(R) CPU\n",
        "physical id\t: 1\n",
        "cpu cores\t: 4\n"
    ]
    return mocker.patch('ansible.module_utils.facts.hardware.netbsd.get_file_lines', return_value=cpuinfo_content)

@pytest.fixture
def mock_ansible_module(mocker):
    mocker.patch('ansible.module_utils.basic._ANSIBLE_ARGS', '{"ANSIBLE_MODULE_ARGS": {}}'.encode('utf-8'))
    return AnsibleModule(argument_spec={})

def test_get_cpu_facts(mock_os_access, mock_get_file_lines, mock_ansible_module):
    hardware = NetBSDHardware(mock_ansible_module)
    cpu_facts = hardware.get_cpu_facts()

    assert 'processor' in cpu_facts
    assert len(cpu_facts['processor']) == 2
    assert cpu_facts['processor'][0] == 'Intel(R) Xeon(R) CPU'
    assert cpu_facts['processor'][1] == 'Intel(R) Xeon(R) CPU'
    assert 'processor_count' in cpu_facts
    assert cpu_facts['processor_count'] == 2
    assert 'processor_cores' in cpu_facts
    assert cpu_facts['processor_cores'] == 8
