# file: lib/ansible/module_utils/facts/system/platform.py:42-97
# asked: {"lines": [65, 66, 68, 69, 70, 71, 72, 85, 86, 87, 88], "branches": [[63, 65], [65, 66], [65, 76], [67, 68], [69, 70], [69, 71], [71, 72], [71, 76], [80, 85], [93, 97]]}
# gained: {"lines": [65, 66, 68, 69, 70, 85, 86, 87, 88], "branches": [[63, 65], [65, 66], [67, 68], [69, 70], [80, 85]]}

import pytest
import platform
import socket
from ansible.module_utils.facts.system.platform import PlatformFactCollector
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_module():
    return MagicMock()

@pytest.fixture
def platform_fact_collector():
    return PlatformFactCollector()

def test_collect_32bit_x86_64(monkeypatch, platform_fact_collector, mock_module):
    monkeypatch.setattr(platform, 'system', lambda: 'Linux')
    monkeypatch.setattr(platform, 'release', lambda: '5.4.0-42-generic')
    monkeypatch.setattr(platform, 'version', lambda: '#46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020')
    monkeypatch.setattr(platform, 'machine', lambda: 'x86_64')
    monkeypatch.setattr(platform, 'python_version', lambda: '3.8.5')
    monkeypatch.setattr(socket, 'getfqdn', lambda: 'test.example.com')
    monkeypatch.setattr(platform, 'node', lambda: 'test.example.com')
    monkeypatch.setattr(platform, 'architecture', lambda: ('32bit', ''))
    
    facts = platform_fact_collector.collect(module=mock_module)
    
    assert facts['userspace_architecture'] == 'i386'

def test_collect_solaris_i86(monkeypatch, platform_fact_collector, mock_module):
    monkeypatch.setattr(platform, 'system', lambda: 'SunOS')
    monkeypatch.setattr(platform, 'release', lambda: '5.11')
    monkeypatch.setattr(platform, 'version', lambda: '11.4')
    monkeypatch.setattr(platform, 'machine', lambda: 'i86pc')
    monkeypatch.setattr(platform, 'python_version', lambda: '3.7.3')
    monkeypatch.setattr(socket, 'getfqdn', lambda: 'solaris.example.com')
    monkeypatch.setattr(platform, 'node', lambda: 'solaris.example.com')
    monkeypatch.setattr(platform, 'architecture', lambda: ('64bit', ''))
    
    facts = platform_fact_collector.collect(module=mock_module)
    
    assert facts['architecture'] == 'i386'
    assert facts['userspace_architecture'] == 'x86_64'

def test_collect_aix_with_getconf(monkeypatch, platform_fact_collector, mock_module):
    monkeypatch.setattr(platform, 'system', lambda: 'AIX')
    monkeypatch.setattr(platform, 'release', lambda: '7.2')
    monkeypatch.setattr(platform, 'version', lambda: '1')
    monkeypatch.setattr(platform, 'machine', lambda: '00F6264A4C00')
    monkeypatch.setattr(platform, 'python_version', lambda: '3.7.3')
    monkeypatch.setattr(socket, 'getfqdn', lambda: 'aix.example.com')
    monkeypatch.setattr(platform, 'node', lambda: 'aix.example.com')
    monkeypatch.setattr(platform, 'architecture', lambda: ('64bit', ''))
    
    mock_module.get_bin_path.return_value = '/usr/bin/getconf'
    mock_module.run_command.return_value = (0, 'ppc64\n', '')
    
    facts = platform_fact_collector.collect(module=mock_module)
    
    assert facts['architecture'] == 'ppc64'

def test_collect_aix_with_bootinfo(monkeypatch, platform_fact_collector, mock_module):
    monkeypatch.setattr(platform, 'system', lambda: 'AIX')
    monkeypatch.setattr(platform, 'release', lambda: '7.2')
    monkeypatch.setattr(platform, 'version', lambda: '1')
    monkeypatch.setattr(platform, 'machine', lambda: '00F6264A4C00')
    monkeypatch.setattr(platform, 'python_version', lambda: '3.7.3')
    monkeypatch.setattr(socket, 'getfqdn', lambda: 'aix.example.com')
    monkeypatch.setattr(platform, 'node', lambda: 'aix.example.com')
    monkeypatch.setattr(platform, 'architecture', lambda: ('64bit', ''))
    
    mock_module.get_bin_path.side_effect = [None, '/usr/sbin/bootinfo']
    mock_module.run_command.return_value = (0, 'ppc\n', '')
    
    facts = platform_fact_collector.collect(module=mock_module)
    
    assert facts['architecture'] == 'ppc'

def test_collect_machine_id(monkeypatch, platform_fact_collector, mock_module):
    monkeypatch.setattr(platform, 'system', lambda: 'Linux')
    monkeypatch.setattr(platform, 'release', lambda: '5.4.0-42-generic')
    monkeypatch.setattr(platform, 'version', lambda: '#46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020')
    monkeypatch.setattr(platform, 'machine', lambda: 'x86_64')
    monkeypatch.setattr(platform, 'python_version', lambda: '3.8.5')
    monkeypatch.setattr(socket, 'getfqdn', lambda: 'test.example.com')
    monkeypatch.setattr(platform, 'node', lambda: 'test.example.com')
    monkeypatch.setattr(platform, 'architecture', lambda: ('64bit', ''))
    
    with patch('ansible.module_utils.facts.system.platform.get_file_content', side_effect=['1234567890abcdef\n', None]):
        facts = platform_fact_collector.collect(module=mock_module)
    
    assert facts['machine_id'] == '1234567890abcdef'
