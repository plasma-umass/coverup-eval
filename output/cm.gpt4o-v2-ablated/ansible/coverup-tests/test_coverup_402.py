# file: lib/ansible/module_utils/facts/system/service_mgr.py:65-150
# asked: {"lines": [66, 68, 69, 71, 72, 78, 79, 80, 81, 82, 86, 87, 88, 92, 93, 96, 97, 99, 100, 102, 103, 104, 105, 107, 109, 112, 114, 117, 119, 120, 122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 145, 147, 149, 150], "branches": [[68, 69], [68, 71], [87, 88], [87, 96], [92, 93], [92, 96], [96, 97], [96, 99], [99, 100], [99, 102], [102, 103], [102, 107], [107, 109], [107, 112], [112, 114], [112, 117], [117, 119], [117, 123], [119, 120], [119, 122], [123, 125], [123, 126], [126, 127], [126, 128], [128, 129], [128, 130], [130, 131], [130, 132], [132, 134], [132, 145], [134, 135], [134, 136], [136, 137], [136, 138], [138, 139], [138, 140], [140, 141], [140, 142], [142, 143], [142, 145], [145, 147], [145, 149]]}
# gained: {"lines": [66, 68, 69, 71, 72, 78, 79, 80, 81, 82, 86, 87, 88, 92, 93, 96, 99, 100, 102, 103, 104, 105, 107, 109, 112, 114, 117, 119, 120, 123, 125, 126, 127, 128, 129, 130, 131, 132, 134, 135, 136, 137, 138, 139, 140, 142, 143, 145, 147, 149, 150], "branches": [[68, 69], [68, 71], [87, 88], [87, 96], [92, 93], [92, 96], [96, 99], [99, 100], [99, 102], [102, 103], [102, 107], [107, 109], [107, 112], [112, 114], [112, 117], [117, 119], [117, 123], [119, 120], [123, 125], [123, 126], [126, 127], [126, 128], [128, 129], [128, 130], [130, 131], [130, 132], [132, 134], [132, 145], [134, 135], [134, 136], [136, 137], [136, 138], [138, 139], [138, 140], [140, 142], [142, 143], [145, 147], [145, 149]]}

import pytest
import os
import platform
import re
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
from ansible.module_utils.facts.collector import BaseFactCollector
from ansible.module_utils.basic import to_native

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

def test_collect_no_proc_1(mock_collector, mock_module):
    with patch('ansible.module_utils.facts.system.service_mgr.get_file_content', return_value=None):
        with patch('os.path.islink', return_value=False):
            result = mock_collector.collect(module=mock_module)
            assert result['service_mgr'] == 'service'

def test_collect_proc_1_from_file(mock_collector, mock_module):
    with patch('ansible.module_utils.facts.system.service_mgr.get_file_content', return_value='systemd'):
        result = mock_collector.collect(module=mock_module)
        assert result['service_mgr'] == 'systemd'

def test_collect_proc_1_from_command(mock_collector, mock_module):
    mock_module.run_command.return_value = (0, 'systemd\n', '')
    with patch('ansible.module_utils.facts.system.service_mgr.get_file_content', return_value=None):
        result = mock_collector.collect(module=mock_module)
        assert result['service_mgr'] == 'systemd'

def test_collect_proc_1_command_fails(mock_collector, mock_module):
    mock_module.run_command.return_value = (1, '', 'error')
    with patch('ansible.module_utils.facts.system.service_mgr.get_file_content', return_value=None):
        result = mock_collector.collect(module=mock_module)
        assert result['service_mgr'] == 'service'

def test_collect_proc_1_is_link(mock_collector, mock_module):
    with patch('ansible.module_utils.facts.system.service_mgr.get_file_content', return_value=None):
        with patch('os.path.islink', return_value=True):
            with patch('os.readlink', return_value='/sbin/init'):
                result = mock_collector.collect(module=mock_module)
                assert result['service_mgr'] == 'service'

def test_collect_macos(mock_collector, mock_module):
    collected_facts = {'ansible_distribution': 'MacOSX'}
    with patch('platform.mac_ver', return_value=('10.15', ('', '', ''), '')):
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

def test_collect_linux_systemd(mock_collector, mock_module):
    collected_facts = {'ansible_system': 'Linux'}
    with patch.object(mock_collector, 'is_systemd_managed', return_value=True):
        result = mock_collector.collect(module=mock_module, collected_facts=collected_facts)
        assert result['service_mgr'] == 'systemd'

def test_collect_linux_upstart(mock_collector, mock_module):
    collected_facts = {'ansible_system': 'Linux'}
    mock_module.get_bin_path.return_value = '/sbin/initctl'
    with patch('os.path.exists', return_value=True):
        with patch.object(mock_collector, 'is_systemd_managed', return_value=False):
            result = mock_collector.collect(module=mock_module, collected_facts=collected_facts)
            assert result['service_mgr'] == 'upstart'

def test_collect_linux_openrc(mock_collector, mock_module):
    collected_facts = {'ansible_system': 'Linux'}
    with patch('os.path.exists', side_effect=lambda x: x == '/sbin/openrc'):
        with patch.object(mock_collector, 'is_systemd_managed', return_value=False):
            result = mock_collector.collect(module=mock_module, collected_facts=collected_facts)
            assert result['service_mgr'] == 'openrc'

def test_collect_linux_sysvinit(mock_collector, mock_module):
    collected_facts = {'ansible_system': 'Linux'}
    with patch('os.path.exists', side_effect=lambda x: x == '/etc/init.d/'):
        with patch.object(mock_collector, 'is_systemd_managed', return_value=False):
            with patch.object(mock_collector, 'is_systemd_managed_offline', return_value=False):
                result = mock_collector.collect(module=mock_module, collected_facts=collected_facts)
                assert result['service_mgr'] == 'sysvinit'
