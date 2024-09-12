# file: lib/ansible/module_utils/facts/system/platform.py:42-97
# asked: {"lines": [65, 66, 67, 68, 69, 70, 71, 72, 74, 85, 86, 87, 88], "branches": [[61, 67], [63, 65], [65, 66], [65, 76], [67, 68], [67, 74], [69, 70], [69, 71], [71, 72], [71, 76], [80, 85], [93, 97]]}
# gained: {"lines": [67, 74], "branches": [[61, 67], [67, 74]]}

import pytest
import platform
import socket
from ansible.module_utils.facts.system.platform import PlatformFactCollector
from ansible.module_utils.facts.collector import BaseFactCollector

@pytest.fixture
def mock_platform(mocker):
    mocker.patch('platform.system', return_value='Linux')
    mocker.patch('platform.release', return_value='5.4.0-42-generic')
    mocker.patch('platform.version', return_value='#46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020')
    mocker.patch('platform.machine', return_value='x86_64')
    mocker.patch('platform.python_version', return_value='3.8.5')
    mocker.patch('platform.node', return_value='testnode.localdomain')
    mocker.patch('platform.architecture', return_value=('64bit', 'ELF'))
    mocker.patch('socket.getfqdn', return_value='testnode.localdomain')
    mocker.patch('platform.uname', return_value=('Linux', 'testnode', '5.4.0-42-generic', '#46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020', 'x86_64', 'x86_64'))

@pytest.fixture
def mock_module(mocker):
    module = mocker.Mock()
    module.get_bin_path = mocker.Mock(return_value=None)
    module.run_command = mocker.Mock(return_value=(0, 'x86_64\n', ''))
    return module

@pytest.fixture
def mock_get_file_content(mocker):
    mocker.patch('ansible.module_utils.facts.system.platform.get_file_content', return_value='1234567890abcdef\n')

def test_collect_linux_x86_64(mock_platform, mock_module, mock_get_file_content):
    collector = PlatformFactCollector()
    facts = collector.collect(module=mock_module)
    
    assert facts['system'] == 'Linux'
    assert facts['kernel'] == '5.4.0-42-generic'
    assert facts['kernel_version'] == '#46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020'
    assert facts['machine'] == 'x86_64'
    assert facts['python_version'] == '3.8.5'
    assert facts['fqdn'] == 'testnode.localdomain'
    assert facts['hostname'] == 'testnode'
    assert facts['nodename'] == 'testnode.localdomain'
    assert facts['domain'] == 'localdomain'
    assert facts['userspace_bits'] == '64'
    assert facts['architecture'] == 'x86_64'
    assert facts['userspace_architecture'] == 'x86_64'
    assert facts['machine_id'] == '1234567890abcdef'

def test_collect_aix(mock_platform, mock_module, mock_get_file_content, mocker):
    mocker.patch('platform.system', return_value='AIX')
    mocker.patch('platform.machine', return_value='00F6264A4C00')
    mock_module.get_bin_path = mocker.Mock(side_effect=['/usr/bin/getconf', None])
    mock_module.run_command = mocker.Mock(side_effect=[(0, 'ppc64\n', ''), (0, 'ppc\n', '')])
    
    collector = PlatformFactCollector()
    facts = collector.collect(module=mock_module)
    
    assert facts['system'] == 'AIX'
    assert facts['architecture'] == 'ppc64'
    assert facts['machine_id'] == '1234567890abcdef'

def test_collect_openbsd(mock_platform, mock_module, mock_get_file_content, mocker):
    mocker.patch('platform.system', return_value='OpenBSD')
    mocker.patch('platform.uname', return_value=('OpenBSD', 'testnode', '6.7', 'GENERIC.MP#123', 'amd64', 'amd64'))
    
    collector = PlatformFactCollector()
    facts = collector.collect(module=mock_module)
    
    assert facts['system'] == 'OpenBSD'
    assert facts['architecture'] == 'amd64'
    assert facts['machine_id'] == '1234567890abcdef'
