# file: lib/ansible/module_utils/facts/system/chroot.py:42-47
# asked: {"lines": [42, 43, 44, 46, 47], "branches": []}
# gained: {"lines": [42, 43, 44, 46, 47], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.system.chroot import ChrootFactCollector, is_chroot

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def chroot_collector():
    return ChrootFactCollector()

def test_chroot_fact_collector_name(chroot_collector):
    assert chroot_collector.name == 'chroot'

def test_chroot_fact_collector_fact_ids(chroot_collector):
    assert chroot_collector._fact_ids == {'is_chroot'}

def test_collect_is_chroot_true(monkeypatch, chroot_collector, mock_module):
    monkeypatch.setenv('debian_chroot', '1')
    result = chroot_collector.collect(module=mock_module)
    assert result == {'is_chroot': True}

def test_collect_is_chroot_false(monkeypatch, chroot_collector, mock_module):
    monkeypatch.delenv('debian_chroot', raising=False)
    with patch('os.stat') as mock_stat:
        mock_stat.side_effect = [Mock(st_ino=1, st_dev=1), Mock(st_ino=1, st_dev=1)]
        result = chroot_collector.collect(module=mock_module)
        assert result == {'is_chroot': False}

def test_collect_is_chroot_exception(monkeypatch, chroot_collector, mock_module):
    monkeypatch.delenv('debian_chroot', raising=False)
    with patch('os.stat') as mock_stat:
        mock_stat.side_effect = [Mock(st_ino=1, st_dev=1), Exception]
        mock_module.get_bin_path.return_value = None
        result = chroot_collector.collect(module=mock_module)
        assert result == {'is_chroot': True}
