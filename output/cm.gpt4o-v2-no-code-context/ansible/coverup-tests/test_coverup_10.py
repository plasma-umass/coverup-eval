# file: lib/ansible/module_utils/facts/system/platform.py:42-97
# asked: {"lines": [42, 43, 45, 46, 47, 48, 50, 52, 53, 54, 56, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 76, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 92, 93, 94, 95, 97], "branches": [[61, 62], [61, 67], [63, 64], [63, 65], [65, 66], [65, 76], [67, 68], [67, 74], [69, 70], [69, 71], [71, 72], [71, 76], [76, 79], [76, 89], [80, 81], [80, 85], [89, 90], [89, 92], [93, 94], [93, 97]]}
# gained: {"lines": [42, 43, 45, 46, 47, 48, 50, 52, 53, 54, 56, 58, 60, 61, 62, 63, 64, 67, 74, 76, 79, 80, 81, 82, 83, 89, 90, 92, 93, 94, 95, 97], "branches": [[61, 62], [61, 67], [63, 64], [67, 74], [76, 79], [76, 89], [80, 81], [89, 90], [89, 92], [93, 94]]}

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

def test_collect_linux_64bit(monkeypatch, platform_fact_collector, mock_module):
    monkeypatch.setattr(platform, 'system', lambda: 'Linux')
    monkeypatch.setattr(platform, 'release', lambda: '5.4.0-42-generic')
    monkeypatch.setattr(platform, 'version', lambda: '#46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020')
    monkeypatch.setattr(platform, 'machine', lambda: 'x86_64')
    monkeypatch.setattr(platform, 'python_version', lambda: '3.8.5')
    monkeypatch.setattr(socket, 'getfqdn', lambda: 'test.example.com')
    monkeypatch.setattr(platform, 'node', lambda: 'test.example.com')
    monkeypatch.setattr(platform, 'architecture', lambda: ('64bit', ''))
    
    facts = platform_fact_collector.collect(module=mock_module)
    
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

def test_collect_aix(monkeypatch, platform_fact_collector, mock_module):
    monkeypatch.setattr(platform, 'system', lambda: 'AIX')
    monkeypatch.setattr(platform, 'release', lambda: '7.2')
    monkeypatch.setattr(platform, 'version', lambda: '1')
    monkeypatch.setattr(platform, 'machine', lambda: '00F6264A4C00')
    monkeypatch.setattr(platform, 'python_version', lambda: '3.7.9')
    monkeypatch.setattr(socket, 'getfqdn', lambda: 'aix.example.com')
    monkeypatch.setattr(platform, 'node', lambda: 'aix.example.com')
    monkeypatch.setattr(platform, 'architecture', lambda: ('64bit', ''))
    
    mock_module.get_bin_path.side_effect = lambda x: '/usr/bin/' + x
    mock_module.run_command.side_effect = lambda x: (0, 'ppc64\n', '')

    facts = platform_fact_collector.collect(module=mock_module)
    
    assert facts['system'] == 'AIX'
    assert facts['kernel'] == '7.2'
    assert facts['kernel_version'] == '1'
    assert facts['machine'] == '00F6264A4C00'
    assert facts['python_version'] == '3.7.9'
    assert facts['fqdn'] == 'aix.example.com'
    assert facts['hostname'] == 'aix'
    assert facts['nodename'] == 'aix.example.com'
    assert facts['domain'] == 'example.com'
    assert facts['userspace_bits'] == '64'
    assert facts['architecture'] == 'ppc64'

def test_collect_openbsd(monkeypatch, platform_fact_collector, mock_module):
    monkeypatch.setattr(platform, 'system', lambda: 'OpenBSD')
    monkeypatch.setattr(platform, 'release', lambda: '6.7')
    monkeypatch.setattr(platform, 'version', lambda: 'GENERIC#123')
    monkeypatch.setattr(platform, 'machine', lambda: 'amd64')
    monkeypatch.setattr(platform, 'python_version', lambda: '3.8.2')
    monkeypatch.setattr(socket, 'getfqdn', lambda: 'openbsd.example.com')
    monkeypatch.setattr(platform, 'node', lambda: 'openbsd.example.com')
    monkeypatch.setattr(platform, 'uname', lambda: ('OpenBSD', '', '', '', '', 'amd64'))
    
    facts = platform_fact_collector.collect(module=mock_module)
    
    assert facts['system'] == 'OpenBSD'
    assert facts['kernel'] == '6.7'
    assert facts['kernel_version'] == 'GENERIC#123'
    assert facts['machine'] == 'amd64'
    assert facts['python_version'] == '3.8.2'
    assert facts['fqdn'] == 'openbsd.example.com'
    assert facts['hostname'] == 'openbsd'
    assert facts['nodename'] == 'openbsd.example.com'
    assert facts['domain'] == 'example.com'
    assert facts['userspace_bits'] == '64'
    assert facts['architecture'] == 'amd64'

def test_collect_machine_id(monkeypatch, platform_fact_collector, mock_module):
    monkeypatch.setattr(platform, 'system', lambda: 'Linux')
    monkeypatch.setattr(platform, 'release', lambda: '5.4.0-42-generic')
    monkeypatch.setattr(platform, 'version', lambda: '#46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020')
    monkeypatch.setattr(platform, 'machine', lambda: 'x86_64')
    monkeypatch.setattr(platform, 'python_version', lambda: '3.8.5')
    monkeypatch.setattr(socket, 'getfqdn', lambda: 'test.example.com')
    monkeypatch.setattr(platform, 'node', lambda: 'test.example.com')
    monkeypatch.setattr(platform, 'architecture', lambda: ('64bit', ''))
    
    with patch('ansible.module_utils.facts.system.platform.get_file_content', side_effect=['1234567890abcdef', None]):
        facts = platform_fact_collector.collect(module=mock_module)
    
    assert facts['machine_id'] == '1234567890abcdef'
