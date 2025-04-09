# file lib/ansible/module_utils/facts/hardware/freebsd.py:151-170
# lines [151, 152, 153, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 170]
# branches ['157->158', '157->170', '158->159', '158->170', '159->160', '159->161']

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

# Mocking the get_mount_size function to return a dictionary with dummy data
def mock_get_mount_size(mount_point):
    return {'size_total': 1024, 'size_available': 512}

# Test function to improve coverage for get_mount_facts method
def test_get_mount_facts(mocker):
    # Mocking the get_file_content function to return a fake fstab content
    mocker.patch(
        'ansible.module_utils.facts.hardware.freebsd.get_file_content',
        return_value='/dev/sda1 / ext4 rw,relatime,data=ordered 0 0\n'
                     '# Commented line\n'
                     '\n'
                     '/dev/sda2 /home ext4 rw,relatime,data=ordered 0 0'
    )
    # Mocking the get_mount_size function
    mocker.patch(
        'ansible.module_utils.facts.hardware.freebsd.get_mount_size',
        side_effect=mock_get_mount_size
    )

    # Creating a MagicMock object to pass as the module parameter
    mock_module = MagicMock()

    freebsd_hardware = FreeBSDHardware(module=mock_module)
    mount_facts = freebsd_hardware.get_mount_facts()

    # Assertions to verify the postconditions
    assert 'mounts' in mount_facts
    assert len(mount_facts['mounts']) == 2  # Two valid mount points in the fstab content
    assert mount_facts['mounts'][0]['mount'] == '/'
    assert mount_facts['mounts'][0]['device'] == '/dev/sda1'
    assert mount_facts['mounts'][0]['fstype'] == 'ext4'
    assert mount_facts['mounts'][0]['options'] == 'rw,relatime,data=ordered'
    assert mount_facts['mounts'][0]['size_total'] == 1024
    assert mount_facts['mounts'][0]['size_available'] == 512
    assert mount_facts['mounts'][1]['mount'] == '/home'
    assert mount_facts['mounts'][1]['device'] == '/dev/sda2'
    assert mount_facts['mounts'][1]['fstype'] == 'ext4'
    assert mount_facts['mounts'][1]['options'] == 'rw,relatime,data=ordered'
    assert mount_facts['mounts'][1]['size_total'] == 1024
    assert mount_facts['mounts'][1]['size_available'] == 512
