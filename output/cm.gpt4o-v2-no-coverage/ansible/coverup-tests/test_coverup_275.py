# file: lib/ansible/module_utils/facts/utils.py:79-100
# asked: {"lines": [79, 80, 82, 83, 84, 85, 88, 89, 90, 91, 94, 95, 96, 97, 98, 100], "branches": []}
# gained: {"lines": [79, 80, 82, 83, 84, 85, 88, 89, 90, 91, 94, 95, 96, 97, 98, 100], "branches": []}

import os
import pytest
from unittest.mock import Mock, patch

from ansible.module_utils.facts.utils import get_mount_size

@pytest.fixture
def mock_statvfs():
    mock = Mock()
    mock.f_frsize = 4096
    mock.f_blocks = 1000000
    mock.f_bavail = 500000
    mock.f_bsize = 4096
    mock.f_files = 100000
    mock.f_favail = 50000
    return mock

def test_get_mount_size_success(mock_statvfs):
    with patch('os.statvfs', return_value=mock_statvfs):
        mountpoint = '/'
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

def test_get_mount_size_oserror():
    with patch('os.statvfs', side_effect=OSError):
        mountpoint = '/'
        result = get_mount_size(mountpoint)
        assert result == {}
