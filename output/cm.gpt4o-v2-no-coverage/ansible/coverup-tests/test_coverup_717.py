# file: lib/ansible/module_utils/facts/system/chroot.py:42-47
# asked: {"lines": [42, 43, 44, 46, 47], "branches": []}
# gained: {"lines": [42, 43, 44, 46, 47], "branches": []}

import pytest
import os
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.system.chroot import ChrootFactCollector, is_chroot

@pytest.fixture
def mock_module():
    return MagicMock()

def test_is_chroot_debian_chroot(monkeypatch):
    monkeypatch.setenv('debian_chroot', '1')
    assert is_chroot() is True

def test_is_chroot_not_debian_chroot(monkeypatch):
    monkeypatch.delenv('debian_chroot', raising=False)
    with patch('os.stat') as mock_stat:
        mock_stat.side_effect = [os.stat_result((0, 0, 0, 0, 0, 0, 0, 0, 0, 0)), os.stat_result((0, 0, 1, 0, 0, 0, 0, 0, 0, 0))]
        assert is_chroot() is True

def test_is_chroot_exception(mock_module, monkeypatch):
    monkeypatch.delenv('debian_chroot', raising=False)
    with patch('os.stat') as mock_stat:
        mock_stat.side_effect = [os.stat_result((0, 0, 0, 0, 0, 0, 0, 0, 0, 0)), Exception]
        mock_module.get_bin_path.return_value = None
        assert is_chroot(mock_module) is True

def test_is_chroot_btrfs(mock_module, monkeypatch):
    monkeypatch.delenv('debian_chroot', raising=False)
    with patch('os.stat') as mock_stat:
        mock_stat.side_effect = [os.stat_result((0, 0, 0, 0, 0, 0, 0, 0, 0, 0)), Exception]
        mock_module.get_bin_path.return_value = '/usr/bin/stat'
        mock_module.run_command.return_value = (0, 'btrfs', '')
        assert is_chroot(mock_module) is True

def test_is_chroot_xfs(mock_module, monkeypatch):
    monkeypatch.delenv('debian_chroot', raising=False)
    with patch('os.stat') as mock_stat:
        mock_stat.side_effect = [os.stat_result((0, 0, 0, 0, 0, 0, 0, 0, 0, 0)), Exception]
        mock_module.get_bin_path.return_value = '/usr/bin/stat'
        mock_module.run_command.return_value = (0, 'xfs', '')
        assert is_chroot(mock_module) is True

def test_chroot_fact_collector_collect(mock_module):
    collector = ChrootFactCollector()
    with patch('ansible.module_utils.facts.system.chroot.is_chroot', return_value=True):
        facts = collector.collect(mock_module)
        assert facts == {'is_chroot': True}
