# file: lib/ansible/module_utils/facts/system/platform.py:42-97
# asked: {"lines": [43, 45, 46, 47, 48, 50, 52, 53, 54, 56, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 76, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 92, 93, 94, 95, 97], "branches": [[61, 62], [61, 67], [63, 64], [63, 65], [65, 66], [65, 76], [67, 68], [67, 74], [69, 70], [69, 71], [71, 72], [71, 76], [76, 79], [76, 89], [80, 81], [80, 85], [89, 90], [89, 92], [93, 94], [93, 97]]}
# gained: {"lines": [43, 45, 46, 47, 48, 50, 52, 53, 54, 56, 58, 60, 61, 62, 63, 64, 76, 79, 80, 81, 82, 83, 89, 90, 92, 93, 94, 95, 97], "branches": [[61, 62], [63, 64], [76, 79], [76, 89], [80, 81], [89, 90], [89, 92], [93, 94]]}

import pytest
import socket
import platform
from ansible.module_utils.facts.system.platform import PlatformFactCollector
from ansible.module_utils.facts.collector import BaseFactCollector

class MockModule:
    def get_bin_path(self, command):
        if command == 'getconf':
            return '/usr/bin/getconf'
        elif command == 'bootinfo':
            return '/usr/bin/bootinfo'
        return None

    def run_command(self, command):
        if command == ['/usr/bin/getconf', 'MACHINE_ARCHITECTURE']:
            return (0, 'x86_64\n', '')
        elif command == ['/usr/bin/bootinfo', '-p']:
            return (0, 'x86_64\n', '')
        return (1, '', 'command not found')

@pytest.fixture
def mock_module():
    return MockModule()

@pytest.fixture(autouse=True)
def mock_platform_functions(monkeypatch):
    monkeypatch.setattr(platform, 'system', lambda: 'Linux')
    monkeypatch.setattr(platform, 'release', lambda: '5.4.0-42-generic')
    monkeypatch.setattr(platform, 'version', lambda: '#46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020')
    monkeypatch.setattr(platform, 'machine', lambda: 'x86_64')
    monkeypatch.setattr(platform, 'python_version', lambda: '3.8.5')
    monkeypatch.setattr(socket, 'getfqdn', lambda: 'test.example.com')
    monkeypatch.setattr(platform, 'node', lambda: 'test.example.com')
    monkeypatch.setattr(platform, 'architecture', lambda: ('64bit', ''))
    monkeypatch.setattr(platform, 'uname', lambda: ('', '', '', '', '', 'amd64'))

@pytest.fixture(autouse=True)
def mock_get_file_content(monkeypatch):
    def mock_get_file_content(path, default=None, strip=True):
        if path == '/var/lib/dbus/machine-id' or path == '/etc/machine-id':
            return '1cc402dd0e11d5ae18db04a6de87223d'
        return default
    monkeypatch.setattr('ansible.module_utils.facts.utils.get_file_content', mock_get_file_content)

def test_collect_linux(mock_module):
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
    assert facts['machine_id'] == '1cc402dd0e11d5ae18db04a6de87223d'

def test_collect_aix(mock_module, monkeypatch):
    monkeypatch.setattr(platform, 'system', lambda: 'AIX')
    collector = PlatformFactCollector()
    facts = collector.collect(module=mock_module)
    assert facts['system'] == 'AIX'
    assert facts['architecture'] == 'x86_64'

def test_collect_openbsd(mock_module, monkeypatch):
    monkeypatch.setattr(platform, 'system', lambda: 'OpenBSD')
    collector = PlatformFactCollector()
    facts = collector.collect(module=mock_module)
    assert facts['system'] == 'OpenBSD'
    assert facts['architecture'] == 'amd64'
