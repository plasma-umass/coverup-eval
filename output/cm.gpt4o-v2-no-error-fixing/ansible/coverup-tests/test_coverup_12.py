# file: lib/ansible/module_utils/facts/system/selinux.py:40-91
# asked: {"lines": [40, 41, 42, 47, 48, 49, 50, 51, 54, 56, 57, 59, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 73, 75, 76, 77, 78, 79, 81, 82, 83, 84, 86, 87, 88, 90, 91], "branches": [[47, 48], [47, 54], [56, 57], [56, 59], [68, 69], [68, 71], [83, 84], [83, 86]]}
# gained: {"lines": [40, 41, 42, 47, 48, 49, 50, 51, 54, 56, 57, 59, 61, 62, 63, 64, 66, 67, 68, 69, 72, 73, 75, 76, 77, 78, 79, 81, 82, 83, 84, 87, 88, 90, 91], "branches": [[47, 48], [47, 54], [56, 57], [56, 59], [68, 69], [83, 84]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.system.selinux import SelinuxFactCollector

@pytest.fixture
def selinux_mock():
    with patch('ansible.module_utils.facts.system.selinux.selinux', autospec=True) as mock_selinux:
        yield mock_selinux

def test_collect_no_selinux_library(monkeypatch):
    monkeypatch.setattr('ansible.module_utils.facts.system.selinux.HAVE_SELINUX', False)
    collector = SelinuxFactCollector()
    result = collector.collect()
    assert result['selinux']['status'] == 'Missing selinux Python library'
    assert result['selinux_python_present'] == False

def test_collect_selinux_disabled(selinux_mock, monkeypatch):
    monkeypatch.setattr('ansible.module_utils.facts.system.selinux.HAVE_SELINUX', True)
    selinux_mock.is_selinux_enabled.return_value = False
    collector = SelinuxFactCollector()
    result = collector.collect()
    assert result['selinux']['status'] == 'disabled'
    assert result['selinux_python_present'] == True

def test_collect_selinux_enabled(selinux_mock, monkeypatch):
    monkeypatch.setattr('ansible.module_utils.facts.system.selinux.HAVE_SELINUX', True)
    selinux_mock.is_selinux_enabled.return_value = True
    selinux_mock.security_policyvers.return_value = 30
    selinux_mock.selinux_getenforcemode.return_value = (0, 1)
    selinux_mock.security_getenforce.return_value = 1
    selinux_mock.selinux_getpolicytype.return_value = (0, 'targeted')

    collector = SelinuxFactCollector()
    result = collector.collect()

    assert result['selinux']['status'] == 'enabled'
    assert result['selinux']['policyvers'] == 30
    assert result['selinux']['config_mode'] == 'enforcing'
    assert result['selinux']['mode'] == 'enforcing'
    assert result['selinux']['type'] == 'targeted'
    assert result['selinux_python_present'] == True

def test_collect_selinux_enabled_exceptions(selinux_mock, monkeypatch):
    monkeypatch.setattr('ansible.module_utils.facts.system.selinux.HAVE_SELINUX', True)
    selinux_mock.is_selinux_enabled.return_value = True
    selinux_mock.security_policyvers.side_effect = OSError
    selinux_mock.selinux_getenforcemode.side_effect = OSError
    selinux_mock.security_getenforce.side_effect = OSError
    selinux_mock.selinux_getpolicytype.side_effect = OSError

    collector = SelinuxFactCollector()
    result = collector.collect()

    assert result['selinux']['status'] == 'enabled'
    assert result['selinux']['policyvers'] == 'unknown'
    assert result['selinux']['config_mode'] == 'unknown'
    assert result['selinux']['mode'] == 'unknown'
    assert result['selinux']['type'] == 'unknown'
    assert result['selinux_python_present'] == True
