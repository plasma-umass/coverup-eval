# file: lib/ansible/module_utils/facts/system/chroot.py:11-39
# asked: {"lines": [11, 13, 15, 16, 18, 19, 21, 22, 23, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 39], "branches": [[15, 16], [15, 18], [27, 28], [27, 37], [29, 30], [29, 37], [32, 33], [32, 34], [34, 35], [34, 37]]}
# gained: {"lines": [11, 13, 15, 16, 18, 19, 21, 22, 23, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 39], "branches": [[15, 16], [15, 18], [27, 28], [27, 37], [29, 30], [32, 33], [32, 34], [34, 35], [34, 37]]}

import os
import pytest
import stat
from unittest.mock import MagicMock, patch

# Import the function to be tested
from ansible.module_utils.facts.system.chroot import is_chroot

@pytest.fixture
def mock_stat():
    with patch('os.stat') as mock_stat:
        yield mock_stat

@pytest.fixture
def mock_environ():
    with patch.dict(os.environ, {}, clear=True):
        yield

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.get_bin_path.return_value = '/usr/bin/stat'
    module.run_command.return_value = (0, 'ext4', '')
    yield module

def test_is_chroot_debian_chroot(mock_environ):
    os.environ['debian_chroot'] = '1'
    assert is_chroot() is True

def test_is_chroot_not_debian_chroot(mock_environ, mock_stat):
    mock_stat.side_effect = [
        MagicMock(st_ino=1, st_dev=1),  # my_root
        MagicMock(st_ino=1, st_dev=1)   # proc_root
    ]
    assert is_chroot() is False

def test_is_chroot_different_inodes(mock_environ, mock_stat):
    mock_stat.side_effect = [
        MagicMock(st_ino=1, st_dev=1),  # my_root
        MagicMock(st_ino=2, st_dev=1)   # proc_root
    ]
    assert is_chroot() is True

def test_is_chroot_exception_no_module(mock_environ, mock_stat):
    mock_stat.side_effect = [
        MagicMock(st_ino=1, st_dev=1),  # my_root
        Exception('stat error')         # proc_root
    ]
    assert is_chroot() is True

def test_is_chroot_exception_with_module(mock_environ, mock_stat, mock_module):
    mock_stat.side_effect = [
        MagicMock(st_ino=1, st_dev=1),  # my_root
        Exception('stat error')         # proc_root
    ]
    assert is_chroot(mock_module) is True

def test_is_chroot_btrfs(mock_environ, mock_stat, mock_module):
    mock_stat.side_effect = [
        MagicMock(st_ino=1, st_dev=1),  # my_root
        Exception('stat error')         # proc_root
    ]
    mock_module.run_command.return_value = (0, 'btrfs', '')
    assert is_chroot(mock_module) is True

def test_is_chroot_xfs(mock_environ, mock_stat, mock_module):
    mock_stat.side_effect = [
        MagicMock(st_ino=1, st_dev=1),  # my_root
        Exception('stat error')         # proc_root
    ]
    mock_module.run_command.return_value = (0, 'xfs', '')
    assert is_chroot(mock_module) is True

def test_is_chroot_ext4(mock_environ, mock_stat, mock_module):
    mock_stat.side_effect = [
        MagicMock(st_ino=1, st_dev=1),  # my_root
        Exception('stat error')         # proc_root
    ]
    mock_module.run_command.return_value = (0, 'ext4', '')
    assert is_chroot(mock_module) is True
