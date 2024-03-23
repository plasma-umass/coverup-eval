# file lib/ansible/module_utils/facts/system/platform.py:42-97
# lines [65, 66, 67, 68, 69, 70, 71, 72, 74, 79, 80, 81, 82, 83, 85, 86, 87, 88, 90]
# branches ['61->67', '63->65', '65->66', '65->76', '67->68', '67->74', '69->70', '69->71', '71->72', '71->76', '76->79', '80->81', '80->85', '89->90', '93->97']

import platform
import socket
import re
import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.system.platform import PlatformFactCollector

# Mocking the platform and socket methods
@pytest.fixture
def mock_platform(mocker):
    mocker.patch('platform.system', return_value='AIX')
    mocker.patch('platform.release', return_value='mock_release')
    mocker.patch('platform.version', return_value='mock_version')
    mocker.patch('platform.machine', return_value='x86_64')
    mocker.patch('platform.python_version', return_value='3.8.1')
    mocker.patch('platform.node', return_value='mock_node.mock_domain')
    mocker.patch('socket.getfqdn', return_value='mock_node.mock_domain')
    mocker.patch('platform.architecture', return_value=('64bit', ''))
    mocker.patch('platform.uname', return_value=('OpenBSD', 'mock_node', 'mock_release', 'mock_version', 'mock_machine', 'mock_architecture'))

# Mocking the module and its methods
@pytest.fixture
def mock_module(mocker):
    mock_module = MagicMock()
    mock_module.get_bin_path.side_effect = lambda x: '/usr/bin/' + x
    mock_module.run_command.side_effect = lambda x: (0, 'mock_architecture\n', '')
    return mock_module

# Mocking the re.search method
@pytest.fixture
def mock_solaris_i86_re(mocker):
    mocker.patch('re.search', return_value=True)

# Mocking the get_file_content function
@pytest.fixture
def mock_get_file_content(mocker):
    mocker.patch('ansible.module_utils.facts.system.platform.get_file_content', return_value='mock_machine_id\n')

# Test function to cover missing lines/branches
def test_platform_fact_collector(mock_platform, mock_module, mock_solaris_i86_re, mock_get_file_content):
    collector = PlatformFactCollector()
    facts = collector.collect(module=mock_module)

    assert facts['system'] == 'AIX'
    assert facts['kernel'] == 'mock_release'
    assert facts['kernel_version'] == 'mock_version'
    assert facts['machine'] == 'x86_64'
    assert facts['python_version'] == '3.8.1'
    assert facts['fqdn'] == 'mock_node.mock_domain'
    assert facts['hostname'] == 'mock_node'
    assert facts['nodename'] == 'mock_node.mock_domain'
    assert facts['domain'] == 'mock_domain'
    assert facts['userspace_bits'] == '64'
    assert facts['architecture'] == 'mock_architecture'
    assert facts['machine_id'] == 'mock_machine_id'
