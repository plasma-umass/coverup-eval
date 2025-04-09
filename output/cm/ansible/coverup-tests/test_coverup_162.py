# file lib/ansible/module_utils/facts/hardware/netbsd.py:114-135
# lines [114, 115, 116, 118, 119, 121, 122, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135]
# branches ['121->122', '121->124', '124->125', '124->135', '125->126', '125->127']

import pytest
from unittest.mock import Mock
from ansible.module_utils.facts.hardware.base import Hardware
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardware

# Mocking the get_file_content function
def mock_get_file_content(file_path):
    if file_path == '/etc/fstab':
        return (
            "# Comment line\n"
            "/dev/wd0a / ffs rw 1 1\n"
            "/dev/wd0b none swap sw 0 0\n"
            "\n"  # Empty line
            "/dev/cd0a /mnt/cdrom cd9660 ro 0 0\n"
        )
    return None

# Mocking the get_mount_size function
def mock_get_mount_size(mount_point):
    return {
        'size_total': 1024 * 1024 * 1024,  # 1 GB in bytes
        'size_available': 512 * 1024 * 1024,  # 512 MB in bytes
    }

@pytest.fixture
def netbsd_hardware(mocker):
    module_mock = Mock()
    hardware = NetBSDHardware(module=module_mock)
    mocker.patch('ansible.module_utils.facts.hardware.netbsd.get_file_content', side_effect=mock_get_file_content)
    mocker.patch('ansible.module_utils.facts.hardware.netbsd.get_mount_size', side_effect=mock_get_mount_size)
    return hardware

def test_get_mount_facts(netbsd_hardware):
    mount_facts = netbsd_hardware.get_mount_facts()

    assert 'mounts' in mount_facts
    assert len(mount_facts['mounts']) == 3  # Only 3 valid lines in fstab

    # Check that the comment and empty lines are skipped
    for mount in mount_facts['mounts']:
        assert not mount['mount'].startswith('#')
        assert mount['mount'].strip() != ''

    # Check that the mount info is correctly parsed and includes the statvfs info
    expected_mounts = [
        {'mount': '/', 'device': '/dev/wd0a', 'fstype': 'ffs', 'options': 'rw', 'size_total': 1024 * 1024 * 1024, 'size_available': 512 * 1024 * 1024},
        {'mount': 'none', 'device': '/dev/wd0b', 'fstype': 'swap', 'options': 'sw', 'size_total': 1024 * 1024 * 1024, 'size_available': 512 * 1024 * 1024},
        {'mount': '/mnt/cdrom', 'device': '/dev/cd0a', 'fstype': 'cd9660', 'options': 'ro', 'size_total': 1024 * 1024 * 1024, 'size_available': 512 * 1024 * 1024},
    ]

    for mount, expected in zip(mount_facts['mounts'], expected_mounts):
        assert mount == expected
