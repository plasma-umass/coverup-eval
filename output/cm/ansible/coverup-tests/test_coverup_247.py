# file lib/ansible/module_utils/facts/utils.py:79-100
# lines [79, 80, 82, 83, 84, 85, 88, 89, 90, 91, 94, 95, 96, 97, 98, 100]
# branches []

import os
import pytest
from ansible.module_utils.facts.utils import get_mount_size

@pytest.fixture
def mock_statvfs(mocker):
    statvfs_result = os.statvfs_result((
        4096,  # f_bsize
        4096,  # f_frsize
        1000000,  # f_blocks
        500000,  # f_bfree
        400000,  # f_bavail
        100000,  # f_files
        80000,  # f_ffree
        70000,  # f_favail
        4096,  # f_flag
        255  # f_namemax
    ))
    mocker.patch('os.statvfs', return_value=statvfs_result)

def test_get_mount_size_success(mock_statvfs):
    mountpoint = '/test_mountpoint'
    mount_size = get_mount_size(mountpoint)

    assert mount_size['size_total'] == 4096 * 1000000
    assert mount_size['size_available'] == 4096 * 400000
    assert mount_size['block_size'] == 4096
    assert mount_size['block_total'] == 1000000
    assert mount_size['block_available'] == 400000
    assert mount_size['block_used'] == 600000
    assert mount_size['inode_total'] == 100000
    assert mount_size['inode_available'] == 70000
    assert mount_size['inode_used'] == 30000

def test_get_mount_size_oserror(mocker):
    mocker.patch('os.statvfs', side_effect=OSError)
    mountpoint = '/invalid_mountpoint'
    mount_size = get_mount_size(mountpoint)

    assert mount_size == {}
