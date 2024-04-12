# file lib/ansible/module_utils/facts/system/platform.py:42-97
# lines [43, 45, 46, 47, 48, 50, 52, 53, 54, 56, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 76, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 92, 93, 94, 95, 97]
# branches ['61->62', '61->67', '63->64', '63->65', '65->66', '65->76', '67->68', '67->74', '69->70', '69->71', '71->72', '71->76', '76->79', '76->89', '80->81', '80->85', '89->90', '89->92', '93->94', '93->97']

import os
import platform
import pytest
import socket
from unittest.mock import MagicMock, patch

# Assuming the PlatformFactCollector class is in a file named platform.py
# within a package named ansible.module_utils.facts.system
from ansible.module_utils.facts.system.platform import PlatformFactCollector

# Mocking the get_file_content function as it is not defined in the provided code snippet
def mock_get_file_content(file_path):
    if file_path == "/var/lib/dbus/machine-id":
        return "dbus123\n"
    elif file_path == "/etc/machine-id":
        return "etc123\n"
    return None

@pytest.fixture
def mock_module():
    mock = MagicMock()
    mock.get_bin_path.side_effect = lambda x: f'/usr/bin/{x}'
    mock.run_command.side_effect = lambda x: (0, 'x86_64\n', '')
    return mock

@pytest.fixture
def mock_platform(monkeypatch):
    monkeypatch.setattr(platform, 'system', lambda: 'Linux')
    monkeypatch.setattr(platform, 'release', lambda: '4.15.0-29-generic')
    monkeypatch.setattr(platform, 'version', lambda: '#31-Ubuntu SMP Tue Jul 17 15:39:52 UTC 2018')
    monkeypatch.setattr(platform, 'machine', lambda: 'x86_64')
    monkeypatch.setattr(platform, 'python_version', lambda: '3.6.7')
    monkeypatch.setattr(platform, 'node', lambda: 'testnode.example.com')
    monkeypatch.setattr(platform, 'architecture', lambda: ('64bit', 'ELF'))
    monkeypatch.setattr(platform, 'uname', lambda: ('Linux', 'testnode', '4.15.0-29-generic', '#31-Ubuntu SMP Tue Jul 17 15:39:52 UTC 2018', 'x86_64', 'x86_64'))
    monkeypatch.setattr(socket, 'getfqdn', lambda: 'testnode.example.com')

@pytest.fixture
def mock_get_file_content_fixture(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.facts.system.platform.get_file_content', mock_get_file_content)

def test_platform_fact_collector(mock_module, mock_platform, mock_get_file_content_fixture):
    collector = PlatformFactCollector()
    facts = collector.collect(module=mock_module)

    assert facts['system'] == 'Linux'
    assert facts['kernel'] == '4.15.0-29-generic'
    assert facts['kernel_version'] == '#31-Ubuntu SMP Tue Jul 17 15:39:52 UTC 2018'
    assert facts['machine'] == 'x86_64'
    assert facts['python_version'] == '3.6.7'
    assert facts['fqdn'] == 'testnode.example.com'
    assert facts['hostname'] == 'testnode'
    assert facts['nodename'] == 'testnode.example.com'
    assert facts['domain'] == 'example.com'
    assert facts['userspace_bits'] == '64'
    assert facts['architecture'] == 'x86_64'
    assert facts['userspace_architecture'] == 'x86_64'
    assert facts['machine_id'] == 'dbus123'
