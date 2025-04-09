# file lib/ansible/module_utils/facts/hardware/sunos.py:145-166
# lines []
# branches ['154->166']

import pytest
from unittest import mock
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

@pytest.fixture
def mock_get_file_content(mocker):
    return mocker.patch('ansible.module_utils.facts.hardware.sunos.get_file_content')

@pytest.fixture
def mock_get_mount_size(mocker):
    return mocker.patch('ansible.module_utils.facts.hardware.sunos.get_mount_size')

@pytest.fixture
def mock_module(mocker):
    return mocker.Mock()

def test_get_mount_facts_with_fstab(mock_get_file_content, mock_get_mount_size, mock_module):
    mock_get_file_content.return_value = (
        "/dev/dsk/c0t0d0s0\t/\tufs\t-\t-\n"
        "/dev/dsk/c0t0d0s1\t/var\tufs\t-\t-\n"
    )
    mock_get_mount_size.side_effect = [
        {'size': 1024, 'used': 512, 'available': 512},
        {'size': 2048, 'used': 1024, 'available': 1024}
    ]

    hardware = SunOSHardware(mock_module)
    mount_facts = hardware.get_mount_facts()

    assert 'mounts' in mount_facts
    assert len(mount_facts['mounts']) == 2
    assert mount_facts['mounts'][0]['mount'] == '/'
    assert mount_facts['mounts'][0]['device'] == '/dev/dsk/c0t0d0s0'
    assert mount_facts['mounts'][0]['fstype'] == 'ufs'
    assert mount_facts['mounts'][0]['options'] == '-'
    assert mount_facts['mounts'][0]['time'] == '-'
    assert mount_facts['mounts'][0]['size'] == 1024
    assert mount_facts['mounts'][0]['used'] == 512
    assert mount_facts['mounts'][0]['available'] == 512

    assert mount_facts['mounts'][1]['mount'] == '/var'
    assert mount_facts['mounts'][1]['device'] == '/dev/dsk/c0t0d0s1'
    assert mount_facts['mounts'][1]['fstype'] == 'ufs'
    assert mount_facts['mounts'][1]['options'] == '-'
    assert mount_facts['mounts'][1]['time'] == '-'
    assert mount_facts['mounts'][1]['size'] == 2048
    assert mount_facts['mounts'][1]['used'] == 1024
    assert mount_facts['mounts'][1]['available'] == 1024

def test_get_mount_facts_without_fstab(mock_get_file_content, mock_module):
    mock_get_file_content.return_value = None

    hardware = SunOSHardware(mock_module)
    mount_facts = hardware.get_mount_facts()

    assert 'mounts' in mount_facts
    assert len(mount_facts['mounts']) == 0
