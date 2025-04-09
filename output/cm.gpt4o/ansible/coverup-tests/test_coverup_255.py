# file lib/ansible/module_utils/facts/utils.py:79-100
# lines [79, 80, 82, 83, 84, 85, 88, 89, 90, 91, 94, 95, 96, 97, 98, 100]
# branches []

import os
import pytest
from unittest.mock import patch

# Assuming the function is imported from the module
from ansible.module_utils.facts.utils import get_mount_size

@pytest.fixture
def mock_statvfs_result():
    class MockStatvfsResult:
        f_frsize = 4096
        f_blocks = 1000000
        f_bavail = 500000
        f_bsize = 4096
        f_files = 100000
        f_favail = 50000

    return MockStatvfsResult()

def test_get_mount_size_success(mock_statvfs_result):
    with patch('os.statvfs', return_value=mock_statvfs_result):
        mountpoint = '/mock/mountpoint'
        result = get_mount_size(mountpoint)
        
        assert result['size_total'] == mock_statvfs_result.f_frsize * mock_statvfs_result.f_blocks
        assert result['size_available'] == mock_statvfs_result.f_frsize * mock_statvfs_result.f_bavail
        assert result['block_size'] == mock_statvfs_result.f_bsize
        assert result['block_total'] == mock_statvfs_result.f_blocks
        assert result['block_available'] == mock_statvfs_result.f_bavail
        assert result['block_used'] == mock_statvfs_result.f_blocks - mock_statvfs_result.f_bavail
        assert result['inode_total'] == mock_statvfs_result.f_files
        assert result['inode_available'] == mock_statvfs_result.f_favail
        assert result['inode_used'] == mock_statvfs_result.f_files - mock_statvfs_result.f_favail

def test_get_mount_size_oserror():
    with patch('os.statvfs', side_effect=OSError):
        mountpoint = '/mock/mountpoint'
        result = get_mount_size(mountpoint)
        
        assert result == {}
