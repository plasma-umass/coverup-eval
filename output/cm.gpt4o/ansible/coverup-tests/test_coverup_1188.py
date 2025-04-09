# file lib/ansible/module_utils/facts/hardware/netbsd.py:67-99
# lines [74, 83, 96, 97]
# branches ['73->74', '82->83', '88->76', '92->96']

import os
import pytest
from unittest.mock import patch, mock_open

from ansible.module_utils.facts.hardware.netbsd import NetBSDHardware

@pytest.fixture
def mock_os_access(mocker):
    return mocker.patch('os.access')

@pytest.fixture
def mock_get_file_lines(mocker):
    return mocker.patch('ansible.module_utils.facts.hardware.netbsd.get_file_lines')

@pytest.fixture
def mock_module(mocker):
    return mocker.Mock()

def test_get_cpu_facts_no_access(mock_os_access, mock_module):
    mock_os_access.return_value = False
    hardware = NetBSDHardware(mock_module)
    cpu_facts = hardware.get_cpu_facts()
    assert cpu_facts == {}

def test_get_cpu_facts_with_data(mock_os_access, mock_get_file_lines, mock_module):
    mock_os_access.return_value = True
    mock_get_file_lines.return_value = [
        "model name: Intel(R) Xeon(R) CPU",
        "physical id: 0",
        "cpu cores: 4",
        "model name: Intel(R) Xeon(R) CPU",
        "physical id: 1",
        "cpu cores: 4"
    ]
    
    hardware = NetBSDHardware(mock_module)
    cpu_facts = hardware.get_cpu_facts()
    
    assert 'processor' in cpu_facts
    assert len(cpu_facts['processor']) == 2
    assert cpu_facts['processor_count'] == 2
    assert cpu_facts['processor_cores'] == 8

def test_get_cpu_facts_no_sockets(mock_os_access, mock_get_file_lines, mock_module):
    mock_os_access.return_value = True
    mock_get_file_lines.return_value = [
        "model name: Intel(R) Xeon(R) CPU",
        "model name: Intel(R) Xeon(R) CPU"
    ]
    
    hardware = NetBSDHardware(mock_module)
    cpu_facts = hardware.get_cpu_facts()
    
    assert 'processor' in cpu_facts
    assert len(cpu_facts['processor']) == 2
    assert cpu_facts['processor_count'] == 2
    assert cpu_facts['processor_cores'] == 'NA'
