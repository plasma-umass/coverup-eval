# file: lib/ansible/module_utils/facts/hardware/freebsd.py:71-93
# asked: {"lines": [72, 73, 74, 75, 76, 77, 79, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90, 91, 93], "branches": [[75, 76], [75, 79], [80, 81], [80, 86], [86, 87], [86, 93], [87, 88], [87, 90], [90, 86], [90, 91]]}
# gained: {"lines": [72, 73, 74, 75, 76, 77, 79, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90, 91, 93], "branches": [[75, 76], [75, 79], [80, 81], [80, 86], [86, 87], [86, 93], [87, 88], [87, 90], [90, 86], [90, 91]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

@pytest.fixture
def module_mock():
    return MagicMock()

@pytest.fixture
def freebsd_hardware(module_mock):
    hardware = FreeBSDHardware(module_mock)
    return hardware

def test_get_cpu_facts_no_sysctl(freebsd_hardware, module_mock):
    module_mock.get_bin_path.return_value = None
    module_mock.run_command.return_value = (1, '', 'error')
    
    with patch('ansible.module_utils.facts.hardware.freebsd.get_file_content', return_value=''):
        cpu_facts = freebsd_hardware.get_cpu_facts()
    
    assert 'processor_count' not in cpu_facts
    assert cpu_facts['processor'] == []

def test_get_cpu_facts_with_sysctl(freebsd_hardware, module_mock):
    module_mock.get_bin_path.return_value = '/sbin/sysctl'
    module_mock.run_command.side_effect = [
        (0, '4\n', ''),  # sysctl command
        (0, 'CPU: Intel(R) Xeon(R) CPU\nLogical CPUs per core: 2\n', '')  # dmesg command
    ]
    
    with patch('ansible.module_utils.facts.hardware.freebsd.get_file_content', return_value=''):
        cpu_facts = freebsd_hardware.get_cpu_facts()
    
    assert cpu_facts['processor_count'] == '4'
    assert cpu_facts['processor'] == ['Intel(R) Xeon(R) CPU']
    assert cpu_facts['processor_cores'] == '2'

def test_get_cpu_facts_dmesg_boot_file(freebsd_hardware, module_mock):
    module_mock.get_bin_path.return_value = '/sbin/sysctl'
    module_mock.run_command.return_value = (0, '4\n', '')
    
    dmesg_content = 'CPU: Intel(R) Xeon(R) CPU\nLogical CPUs per core: 2\n'
    with patch('ansible.module_utils.facts.hardware.freebsd.get_file_content', return_value=dmesg_content):
        cpu_facts = freebsd_hardware.get_cpu_facts()
    
    assert cpu_facts['processor_count'] == '4'
    assert cpu_facts['processor'] == ['Intel(R) Xeon(R) CPU']
    assert cpu_facts['processor_cores'] == '2'

def test_get_cpu_facts_dmesg_command(freebsd_hardware, module_mock):
    module_mock.get_bin_path.side_effect = ['/sbin/sysctl', '/sbin/dmesg']
    module_mock.run_command.side_effect = [
        (0, '4\n', ''),  # sysctl command
        (0, 'CPU: Intel(R) Xeon(R) CPU\nLogical CPUs per core: 2\n', '')  # dmesg command
    ]
    
    with patch('ansible.module_utils.facts.hardware.freebsd.get_file_content', return_value=''):
        cpu_facts = freebsd_hardware.get_cpu_facts()
    
    assert cpu_facts['processor_count'] == '4'
    assert cpu_facts['processor'] == ['Intel(R) Xeon(R) CPU']
    assert cpu_facts['processor_cores'] == '2'

def test_get_cpu_facts_dmesg_command_exception(freebsd_hardware, module_mock):
    module_mock.get_bin_path.side_effect = ['/sbin/sysctl', '/sbin/dmesg']
    module_mock.run_command.side_effect = [
        (0, '4\n', ''),  # sysctl command
        Exception('dmesg command failed')  # dmesg command
    ]
    
    with patch('ansible.module_utils.facts.hardware.freebsd.get_file_content', return_value=''):
        cpu_facts = freebsd_hardware.get_cpu_facts()
    
    assert cpu_facts['processor_count'] == '4'
    assert cpu_facts['processor'] == []
    assert 'processor_cores' not in cpu_facts
