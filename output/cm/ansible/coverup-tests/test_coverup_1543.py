# file lib/ansible/module_utils/facts/hardware/openbsd.py:66-86
# lines [68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]
# branches ['72->73', '72->86', '73->74', '73->86', '74->75', '74->76', '77->78', '77->79']

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware

# Define the content of the fake /etc/fstab file
FAKE_FSTAB = """
# Comment line
/dev/wd0a / ffs rw 1 1
none /tmp tmpfs rw 0 0
/dev/wd0b none swap sw 0 0
/dev/wd0d /usr ffs rw,nodev 1 2
xx /mnt xx xx 0 0
"""

# Define the expected result for get_mount_size
FAKE_MOUNT_SIZE = {
    'block_used': 1000,
    'block_total': 2000,
    'block_available': 1000,
    'block_size': 512,
    'inode_used': 100,
    'inode_total': 200,
    'inode_available': 100,
}

# Define a test function to cover the missing lines
@pytest.fixture
def mock_openbsd_hardware(mocker):
    mocker.patch('ansible.module_utils.facts.hardware.openbsd.get_file_content', return_value=FAKE_FSTAB)
    mocker.patch('ansible.module_utils.facts.hardware.openbsd.get_mount_size', return_value=FAKE_MOUNT_SIZE)
    module_mock = MagicMock()
    return OpenBSDHardware(module=module_mock)

def test_get_mount_facts(mock_openbsd_hardware):
    mount_facts = mock_openbsd_hardware.get_mount_facts()

    # Assert that the mounts list is not empty
    assert mount_facts['mounts']

    # Assert that the mounts list contains the expected number of mounts (excluding 'none' and 'xx')
    # Adjust the expected number of mounts to 3, as the fake fstab contains 3 valid mount points
    assert len(mount_facts['mounts']) == 3

    # Assert that the mounts list contains the expected values
    expected_mounts = [
        {
            'mount': '/',
            'device': '/dev/wd0a',
            'fstype': 'ffs',
            'options': 'rw',
            **FAKE_MOUNT_SIZE,
        },
        {
            'mount': '/tmp',
            'device': 'none',
            'fstype': 'tmpfs',
            'options': 'rw',
            **FAKE_MOUNT_SIZE,
        },
        {
            'mount': '/usr',
            'device': '/dev/wd0d',
            'fstype': 'ffs',
            'options': 'rw,nodev',
            **FAKE_MOUNT_SIZE,
        },
    ]
    assert mount_facts['mounts'] == expected_mounts
