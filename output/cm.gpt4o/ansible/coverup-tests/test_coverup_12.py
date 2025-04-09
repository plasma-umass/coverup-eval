# file lib/ansible/module_utils/facts/system/platform.py:42-97
# lines [42, 43, 45, 46, 47, 48, 50, 52, 53, 54, 56, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 76, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 92, 93, 94, 95, 97]
# branches ['61->62', '61->67', '63->64', '63->65', '65->66', '65->76', '67->68', '67->74', '69->70', '69->71', '71->72', '71->76', '76->79', '76->89', '80->81', '80->85', '89->90', '89->92', '93->94', '93->97']

import pytest
import platform
import socket
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.system.platform import PlatformFactCollector

@pytest.fixture
def mock_module(mocker):
    module = MagicMock()
    module.get_bin_path = MagicMock(return_value='/usr/bin/getconf')
    module.run_command = MagicMock(return_value=(0, 'x86_64\n', ''))
    return module

@pytest.fixture
def mock_get_file_content(mocker):
    return mocker.patch('ansible.module_utils.facts.system.platform.get_file_content', return_value='1234567890abcdef\n')

@pytest.fixture
def mock_platform(mocker):
    mocker.patch('platform.system', return_value='AIX')
    mocker.patch('platform.release', return_value='7.2')
    mocker.patch('platform.version', return_value='7100-04-01-1543')
    mocker.patch('platform.machine', return_value='00F6264A4C00')
    mocker.patch('platform.python_version', return_value='3.8.5')
    mocker.patch('platform.node', return_value='testnode.example.com')
    mocker.patch('platform.architecture', return_value=('64bit', ''))
    mocker.patch('platform.uname', return_value=('OpenBSD', 'testnode', '6.7', '', '', 'amd64'))

@pytest.fixture
def mock_socket(mocker):
    mocker.patch('socket.getfqdn', return_value='testnode.example.com')

def test_collect_platform_facts(mock_module, mock_get_file_content, mock_platform, mock_socket):
    collector = PlatformFactCollector()
    facts = collector.collect(module=mock_module)

    assert facts['system'] == 'AIX'
    assert facts['kernel'] == '7.2'
    assert facts['kernel_version'] == '7100-04-01-1543'
    assert facts['machine'] == '00F6264A4C00'
    assert facts['python_version'] == '3.8.5'
    assert facts['fqdn'] == 'testnode.example.com'
    assert facts['hostname'] == 'testnode'
    assert facts['nodename'] == 'testnode.example.com'
    assert facts['domain'] == 'example.com'
    assert facts['userspace_bits'] == '64'
    assert facts['architecture'] == 'x86_64'
    assert 'userspace_architecture' not in facts
    assert facts['machine_id'] == '1234567890abcdef'
