# file: lib/ansible/module_utils/facts/system/platform.py:42-97
# asked: {"lines": [42, 43, 45, 46, 47, 48, 50, 52, 53, 54, 56, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 76, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 92, 93, 94, 95, 97], "branches": [[61, 62], [61, 67], [63, 64], [63, 65], [65, 66], [65, 76], [67, 68], [67, 74], [69, 70], [69, 71], [71, 72], [71, 76], [76, 79], [76, 89], [80, 81], [80, 85], [89, 90], [89, 92], [93, 94], [93, 97]]}
# gained: {"lines": [42, 43, 45, 46, 47, 48, 50, 52, 53, 54, 56, 58, 60, 61, 62, 63, 64, 76, 79, 80, 81, 82, 83, 89, 90, 92, 93, 94, 95, 97], "branches": [[61, 62], [63, 64], [76, 79], [76, 89], [80, 81], [89, 90], [89, 92], [93, 94]]}

import pytest
import platform
import socket
from ansible.module_utils.facts.system.platform import PlatformFactCollector
from ansible.module_utils.basic import AnsibleModule

@pytest.fixture
def mock_platform(mocker):
    mocker.patch('platform.system', return_value='Linux')
    mocker.patch('platform.release', return_value='5.4.0-42-generic')
    mocker.patch('platform.version', return_value='#46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020')
    mocker.patch('platform.machine', return_value='x86_64')
    mocker.patch('platform.python_version', return_value='3.8.5')
    mocker.patch('socket.getfqdn', return_value='test.example.com')
    mocker.patch('platform.node', return_value='test.example.com')
    mocker.patch('platform.architecture', return_value=('64bit', ''))
    mocker.patch('platform.uname', return_value=('Linux', 'test', '5.4.0-42-generic', '#46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020', 'x86_64', 'x86_64'))

@pytest.fixture
def mock_module(mocker):
    module = mocker.Mock(spec=AnsibleModule)
    module.get_bin_path = mocker.Mock(return_value=None)
    module.run_command = mocker.Mock(return_value=(0, 'x86_64\n', ''))
    return module

def test_collect_linux(mock_platform, mock_module):
    collector = PlatformFactCollector()
    facts = collector.collect(module=mock_module)
    
    assert facts['system'] == 'Linux'
    assert facts['kernel'] == '5.4.0-42-generic'
    assert facts['kernel_version'] == '#46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020'
    assert facts['machine'] == 'x86_64'
    assert facts['python_version'] == '3.8.5'
    assert facts['fqdn'] == 'test.example.com'
    assert facts['hostname'] == 'test'
    assert facts['nodename'] == 'test.example.com'
    assert facts['domain'] == 'example.com'
    assert facts['userspace_bits'] == '64'
    assert facts['architecture'] == 'x86_64'
    assert facts['userspace_architecture'] == 'x86_64'

def test_collect_aix(mock_platform, mock_module, mocker):
    mocker.patch('platform.system', return_value='AIX')
    mock_module.get_bin_path = mocker.Mock(return_value='/usr/bin/getconf')
    mock_module.run_command = mocker.Mock(return_value=(0, 'ppc64\n', ''))
    
    collector = PlatformFactCollector()
    facts = collector.collect(module=mock_module)
    
    assert facts['system'] == 'AIX'
    assert facts['architecture'] == 'ppc64'

def test_collect_openbsd(mock_platform, mock_module, mocker):
    mocker.patch('platform.system', return_value='OpenBSD')
    mocker.patch('platform.uname', return_value=('OpenBSD', 'test', '6.7', '', 'amd64', 'amd64'))
    
    collector = PlatformFactCollector()
    facts = collector.collect(module=mock_module)
    
    assert facts['system'] == 'OpenBSD'
    assert facts['architecture'] == 'amd64'

def test_collect_machine_id(mocker, mock_module):
    mocker.patch('platform.system', return_value='Linux')
    mocker.patch('platform.release', return_value='5.4.0-42-generic')
    mocker.patch('platform.version', return_value='#46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020')
    mocker.patch('platform.machine', return_value='x86_64')
    mocker.patch('platform.python_version', return_value='3.8.5')
    mocker.patch('socket.getfqdn', return_value='test.example.com')
    mocker.patch('platform.node', return_value='test.example.com')
    mocker.patch('platform.architecture', return_value=('64bit', ''))
    mocker.patch('platform.uname', return_value=('Linux', 'test', '5.4.0-42-generic', '#46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020', 'x86_64', 'x86_64'))
    mocker.patch('ansible.module_utils.facts.system.platform.get_file_content', return_value='1234567890abcdef\n')
    
    collector = PlatformFactCollector()
    facts = collector.collect(module=mock_module)
    
    assert facts['machine_id'] == '1234567890abcdef'
