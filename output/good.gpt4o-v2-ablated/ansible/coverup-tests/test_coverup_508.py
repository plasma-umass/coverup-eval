# file: lib/ansible/module_utils/facts/system/service_mgr.py:65-150
# asked: {"lines": [97, 122, 141], "branches": [[96, 97], [119, 122], [140, 141], [142, 145]]}
# gained: {"lines": [97], "branches": [[96, 97]]}

import pytest
import os
import platform
import re
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
from ansible.module_utils.facts.collector import BaseFactCollector
from ansible.module_utils._text import to_native
from distutils.version import LooseVersion

def get_file_content(path):
    try:
        with open(path, 'r') as file:
            return file.read().strip()
    except IOError:
        return None

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.run_command = MagicMock(return_value=(0, '', ''))
    module.get_bin_path = MagicMock(return_value=None)
    return module

@pytest.fixture
def mock_collector():
    return ServiceMgrFactCollector()

def test_collect_no_module(mock_collector):
    result = mock_collector.collect()
    assert result == {}

def test_collect_proc_1_comm(mock_collector, mock_module, monkeypatch):
    monkeypatch.setattr('ansible.module_utils.facts.system.service_mgr.get_file_content', lambda x: 'procd')
    result = mock_collector.collect(module=mock_module)
    assert result['service_mgr'] == 'openwrt_init'

def test_collect_proc_1_ps_command(mock_collector, mock_module, monkeypatch):
    monkeypatch.setattr('ansible.module_utils.facts.system.service_mgr.get_file_content', lambda x: None)
    mock_module.run_command.return_value = (0, 'runit-init\n', '')
    result = mock_collector.collect(module=mock_module)
    assert result['service_mgr'] == 'runit'

def test_collect_proc_1_ps_command_fail(mock_collector, mock_module, monkeypatch):
    monkeypatch.setattr('ansible.module_utils.facts.system.service_mgr.get_file_content', lambda x: None)
    mock_module.run_command.return_value = (1, '', '')
    result = mock_collector.collect(module=mock_module)
    assert result['service_mgr'] == 'service'

def test_collect_proc_1_command(mock_collector, mock_module, monkeypatch):
    monkeypatch.setattr('ansible.module_utils.facts.system.service_mgr.get_file_content', lambda x: None)
    mock_module.run_command.return_value = (0, 'COMMAND\n', '')
    result = mock_collector.collect(module=mock_module)
    assert result['service_mgr'] == 'service'

def test_collect_proc_1_symlink(mock_collector, mock_module, monkeypatch):
    monkeypatch.setattr('os.path.islink', lambda x: True)
    monkeypatch.setattr('os.readlink', lambda x: '/sbin/init')
    result = mock_collector.collect(module=mock_module)
    assert result['service_mgr'] == 'service'

def test_collect_macosx(mock_collector, mock_module, monkeypatch):
    collected_facts = {'ansible_distribution': 'MacOSX'}
    monkeypatch.setattr(platform, 'mac_ver', lambda: ('10.5', ('', '', ''), ''))
    result = mock_collector.collect(module=mock_module, collected_facts=collected_facts)
    assert result['service_mgr'] == 'launchd'

def test_collect_bsd(mock_collector, mock_module):
    collected_facts = {'ansible_system': 'FreeBSD'}
    result = mock_collector.collect(module=mock_module, collected_facts=collected_facts)
    assert result['service_mgr'] == 'bsdinit'

def test_collect_aix(mock_collector, mock_module):
    collected_facts = {'ansible_system': 'AIX'}
    result = mock_collector.collect(module=mock_module, collected_facts=collected_facts)
    assert result['service_mgr'] == 'src'

def test_collect_sunos(mock_collector, mock_module):
    collected_facts = {'ansible_system': 'SunOS'}
    result = mock_collector.collect(module=mock_module, collected_facts=collected_facts)
    assert result['service_mgr'] == 'smf'

def test_collect_openwrt(mock_collector, mock_module):
    collected_facts = {'ansible_distribution': 'OpenWrt'}
    result = mock_collector.collect(module=mock_module, collected_facts=collected_facts)
    assert result['service_mgr'] == 'openwrt_init'

def test_collect_linux_systemd(mock_collector, mock_module, monkeypatch):
    collected_facts = {'ansible_system': 'Linux'}
    monkeypatch.setattr(mock_collector, 'is_systemd_managed', lambda module: True)
    result = mock_collector.collect(module=mock_module, collected_facts=collected_facts)
    assert result['service_mgr'] == 'systemd'

def test_collect_linux_upstart(mock_collector, mock_module, monkeypatch):
    collected_facts = {'ansible_system': 'Linux'}
    mock_module.get_bin_path.return_value = '/sbin/initctl'
    monkeypatch.setattr(os.path, 'exists', lambda x: x == "/etc/init/")
    result = mock_collector.collect(module=mock_module, collected_facts=collected_facts)
    assert result['service_mgr'] == 'upstart'

def test_collect_linux_openrc(mock_collector, mock_module, monkeypatch):
    collected_facts = {'ansible_system': 'Linux'}
    monkeypatch.setattr(os.path, 'exists', lambda x: x == '/sbin/openrc')
    result = mock_collector.collect(module=mock_module, collected_facts=collected_facts)
    assert result['service_mgr'] == 'openrc'

def test_collect_linux_sysvinit(mock_collector, mock_module, monkeypatch):
    collected_facts = {'ansible_system': 'Linux'}
    monkeypatch.setattr(mock_collector, 'is_systemd_managed', lambda module: False)
    monkeypatch.setattr(mock_collector, 'is_systemd_managed_offline', lambda module: False)
    monkeypatch.setattr(os.path, 'exists', lambda x: x == '/etc/init.d/')
    result = mock_collector.collect(module=mock_module, collected_facts=collected_facts)
    assert result['service_mgr'] == 'sysvinit'

def test_collect_fallback_service(mock_collector, mock_module):
    collected_facts = {}
    result = mock_collector.collect(module=mock_module, collected_facts=collected_facts)
    assert result['service_mgr'] == 'service'
