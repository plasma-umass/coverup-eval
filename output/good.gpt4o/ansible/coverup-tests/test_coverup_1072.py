# file lib/ansible/module_utils/facts/system/platform.py:42-97
# lines [62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 85, 86, 87, 88, 89, 90]
# branches ['61->62', '63->64', '63->65', '65->66', '65->76', '67->68', '69->70', '69->71', '71->72', '71->76', '76->89', '80->85', '89->90', '89->92', '93->97']

import pytest
import platform
import socket
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.system.platform import PlatformFactCollector

@pytest.fixture
def mock_platform_facts(mocker):
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
    module = MagicMock()
    module.get_bin_path = MagicMock(side_effect=lambda x: '/usr/bin/' + x if x in ['getconf', 'bootinfo'] else None)
    module.run_command = MagicMock(side_effect=lambda x: (0, 'x86_64\n', '') if 'getconf' in x else (0, 'i386\n', ''))
    return module

def test_collect_full_coverage(mock_platform_facts, mock_module):
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

    # Test AIX specific code
    with patch('platform.system', return_value='AIX'):
        with patch('platform.machine', return_value='00F6264A4C00'):
            with patch.object(mock_module, 'get_bin_path', return_value='/usr/bin/getconf'):
                with patch.object(mock_module, 'run_command', return_value=(0, 'x86_64\n', '')):
                    facts = collector.collect(module=mock_module)
                    assert facts['architecture'] == 'x86_64'
            with patch.object(mock_module, 'get_bin_path', return_value=None):
                with patch.object(mock_module, 'run_command', return_value=(0, 'i386\n', '')):
                    facts = collector.collect(module=mock_module)
                    assert facts['architecture'] == 'i386'

    # Test OpenBSD specific code
    with patch('platform.system', return_value='OpenBSD'):
        facts = collector.collect(module=mock_module)
        assert facts['architecture'] == 'x86_64'

    # Test machine_id code
    with patch('ansible.module_utils.facts.system.platform.get_file_content', side_effect=['12345\n', None]):
        facts = collector.collect(module=mock_module)
        assert facts['machine_id'] == '12345'
