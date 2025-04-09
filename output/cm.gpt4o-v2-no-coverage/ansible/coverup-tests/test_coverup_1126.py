# file: lib/ansible/module_utils/facts/hardware/sunos.py:145-166
# asked: {"lines": [147, 148, 152, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 166], "branches": [[154, 155], [154, 166], [155, 156], [155, 166]]}
# gained: {"lines": [147, 148, 152, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 166], "branches": [[154, 155], [154, 166], [155, 156], [155, 166]]}

import pytest
from unittest.mock import patch, Mock
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

@pytest.fixture
def sunos_hardware():
    module = Mock()
    return SunOSHardware(module)

@patch('ansible.module_utils.facts.hardware.sunos.get_file_content')
@patch('ansible.module_utils.facts.hardware.sunos.get_mount_size')
def test_get_mount_facts(mock_get_mount_size, mock_get_file_content, sunos_hardware):
    mock_get_file_content.return_value = (
        "/dev/dsk/c0d0s0\t/\tufs\t-\t1234567890\n"
        "/dev/dsk/c0d0s1\t/var\tufs\t-\t1234567891\n"
    )
    mock_get_mount_size.side_effect = [
        {'size_total': 100, 'size_available': 50, 'block_size': 1024, 'block_total': 100, 'block_available': 50, 'block_used': 50, 'inode_total': 100, 'inode_available': 50, 'inode_used': 50},
        {'size_total': 200, 'size_available': 100, 'block_size': 1024, 'block_total': 200, 'block_available': 100, 'block_used': 100, 'inode_total': 200, 'inode_available': 100, 'inode_used': 100}
    ]

    expected_mounts = [
        {
            'mount': '/',
            'device': '/dev/dsk/c0d0s0',
            'fstype': 'ufs',
            'options': '-',
            'time': '1234567890',
            'size_total': 100,
            'size_available': 50,
            'block_size': 1024,
            'block_total': 100,
            'block_available': 50,
            'block_used': 50,
            'inode_total': 100,
            'inode_available': 50,
            'inode_used': 50
        },
        {
            'mount': '/var',
            'device': '/dev/dsk/c0d0s1',
            'fstype': 'ufs',
            'options': '-',
            'time': '1234567891',
            'size_total': 200,
            'size_available': 100,
            'block_size': 1024,
            'block_total': 200,
            'block_available': 100,
            'block_used': 100,
            'inode_total': 200,
            'inode_available': 100,
            'inode_used': 100
        }
    ]

    result = sunos_hardware.get_mount_facts()
    assert result['mounts'] == expected_mounts

@patch('ansible.module_utils.facts.hardware.sunos.get_file_content')
def test_get_mount_facts_no_fstab(mock_get_file_content, sunos_hardware):
    mock_get_file_content.return_value = None
    result = sunos_hardware.get_mount_facts()
    assert result['mounts'] == []
