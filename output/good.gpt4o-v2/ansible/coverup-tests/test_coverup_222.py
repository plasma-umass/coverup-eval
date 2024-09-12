# file: lib/ansible/module_utils/facts/utils.py:79-100
# asked: {"lines": [79, 80, 82, 83, 84, 85, 88, 89, 90, 91, 94, 95, 96, 97, 98, 100], "branches": []}
# gained: {"lines": [79, 80, 82, 83, 84, 85, 88, 89, 90, 91, 94, 95, 96, 97, 98, 100], "branches": []}

import os
import pytest
from unittest.mock import patch

from ansible.module_utils.facts.utils import get_mount_size

@pytest.fixture
def mock_statvfs():
    with patch('os.statvfs') as mock:
        yield mock

def test_get_mount_size_success(mock_statvfs):
    # Mock the return value of os.statvfs
    mock_statvfs.return_value = os.statvfs_result(
        (4096, 4096, 1000000, 500000, 500000, 1000000, 800000, 800000, 255, 255)
    )
    
    mountpoint = '/fake/mountpoint'
    result = get_mount_size(mountpoint)
    
    assert result['size_total'] == 4096 * 1000000
    assert result['size_available'] == 4096 * 500000
    assert result['block_size'] == 4096
    assert result['block_total'] == 1000000
    assert result['block_available'] == 500000
    assert result['block_used'] == 500000
    assert result['inode_total'] == 1000000
    assert result['inode_available'] == 800000
    assert result['inode_used'] == 200000

def test_get_mount_size_oserror(mock_statvfs):
    # Mock os.statvfs to raise an OSError
    mock_statvfs.side_effect = OSError
    
    mountpoint = '/fake/mountpoint'
    result = get_mount_size(mountpoint)
    
    assert result == {}
