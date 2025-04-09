# file: lib/ansible/module_utils/facts/system/chroot.py:42-47
# asked: {"lines": [42, 43, 44, 46, 47], "branches": []}
# gained: {"lines": [42, 43, 44, 46, 47], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.system.chroot import ChrootFactCollector, is_chroot

@pytest.fixture
def mock_module():
    return MagicMock()

def test_chroot_fact_collector_collect_debian_chroot(mock_module):
    collector = ChrootFactCollector()
    with patch.dict('os.environ', {'debian_chroot': 'true'}):
        facts = collector.collect(module=mock_module)
        assert facts == {'is_chroot': True}

def test_chroot_fact_collector_collect_proc_root(mock_module):
    collector = ChrootFactCollector()
    with patch('os.stat') as mock_stat:
        mock_stat.side_effect = [
            MagicMock(st_ino=1, st_dev=1),  # my_root
            MagicMock(st_ino=2, st_dev=2)   # proc_root
        ]
        facts = collector.collect(module=mock_module)
        assert facts == {'is_chroot': True}

def test_chroot_fact_collector_collect_exception(mock_module):
    collector = ChrootFactCollector()
    with patch('os.stat') as mock_stat:
        mock_stat.side_effect = [
            MagicMock(st_ino=1, st_dev=1),  # my_root
            Exception('stat failed')        # proc_root
        ]
        mock_module.get_bin_path.return_value = '/usr/bin/stat'
        mock_module.run_command.return_value = (0, 'ext4', '')  # Simulate ext4 filesystem
        facts = collector.collect(module=mock_module)
        assert facts == {'is_chroot': True}

def test_chroot_fact_collector_collect_exception_btrfs(mock_module):
    collector = ChrootFactCollector()
    with patch('os.stat') as mock_stat:
        mock_stat.side_effect = [
            MagicMock(st_ino=1, st_dev=1),  # my_root
            Exception('stat failed')        # proc_root
        ]
        mock_module.get_bin_path.return_value = '/usr/bin/stat'
        mock_module.run_command.return_value = (0, 'btrfs', '')  # Simulate btrfs filesystem
        facts = collector.collect(module=mock_module)
        assert facts == {'is_chroot': True}

def test_chroot_fact_collector_collect_exception_xfs(mock_module):
    collector = ChrootFactCollector()
    with patch('os.stat') as mock_stat:
        mock_stat.side_effect = [
            MagicMock(st_ino=1, st_dev=1),  # my_root
            Exception('stat failed')        # proc_root
        ]
        mock_module.get_bin_path.return_value = '/usr/bin/stat'
        mock_module.run_command.return_value = (0, 'xfs', '')  # Simulate xfs filesystem
        facts = collector.collect(module=mock_module)
        assert facts == {'is_chroot': True}
