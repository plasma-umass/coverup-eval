# file: lib/ansible/module_utils/facts/utils.py:79-100
# asked: {"lines": [80, 82, 83, 84, 85, 88, 89, 90, 91, 94, 95, 96, 97, 98, 100], "branches": []}
# gained: {"lines": [80, 82, 83, 84, 85, 88, 89, 90, 91, 94, 95, 96, 97, 98, 100], "branches": []}

import os
import pytest
from unittest.mock import MagicMock

# Assuming the function get_mount_size is imported from the module
from ansible.module_utils.facts.utils import get_mount_size

def test_get_mount_size_success(monkeypatch):
    mock_statvfs_result = MagicMock()
    mock_statvfs_result.f_frsize = 4096
    mock_statvfs_result.f_blocks = 1000000
    mock_statvfs_result.f_bavail = 500000
    mock_statvfs_result.f_bsize = 4096
    mock_statvfs_result.f_files = 100000
    mock_statvfs_result.f_favail = 50000

    def mock_statvfs(path):
        return mock_statvfs_result

    monkeypatch.setattr(os, 'statvfs', mock_statvfs)

    mountpoint = '/fake/mountpoint'
    result = get_mount_size(mountpoint)

    assert result['size_total'] == 4096 * 1000000
    assert result['size_available'] == 4096 * 500000
    assert result['block_size'] == 4096
    assert result['block_total'] == 1000000
    assert result['block_available'] == 500000
    assert result['block_used'] == 500000
    assert result['inode_total'] == 100000
    assert result['inode_available'] == 50000
    assert result['inode_used'] == 50000

def test_get_mount_size_oserror(monkeypatch):
    def mock_statvfs(path):
        raise OSError

    monkeypatch.setattr(os, 'statvfs', mock_statvfs)

    mountpoint = '/fake/mountpoint'
    result = get_mount_size(mountpoint)

    assert result == {}
