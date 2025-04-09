# file lib/ansible/module_utils/facts/hardware/freebsd.py:151-170
# lines [151, 152, 153, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 170]
# branches ['157->158', '157->170', '158->159', '158->170', '159->160', '159->161']

import pytest
from unittest.mock import patch, mock_open, MagicMock
import re

# Assuming the FreeBSDHardware class and its dependencies are imported from the module
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

@pytest.fixture
def mock_get_file_content():
    with patch('ansible.module_utils.facts.hardware.freebsd.get_file_content') as mock:
        yield mock

@pytest.fixture
def mock_get_mount_size():
    with patch('ansible.module_utils.facts.hardware.freebsd.get_mount_size') as mock:
        yield mock

def test_get_mount_facts(mock_get_file_content, mock_get_mount_size):
    # Mock the content of /etc/fstab
    mock_get_file_content.return_value = """
# This is a comment
/dev/ada0p2 / ufs rw 1 1
/dev/ada0p3 /home ufs rw 2 2
"""
    # Mock the return value of get_mount_size
    mock_get_mount_size.side_effect = lambda mount_point: {'size': 1000, 'used': 500, 'available': 500}

    # Mock the module argument required by Hardware's __init__
    mock_module = MagicMock()

    hardware = FreeBSDHardware(mock_module)
    mount_facts = hardware.get_mount_facts()

    expected_mounts = [
        {
            'mount': '/',
            'device': '/dev/ada0p2',
            'fstype': 'ufs',
            'options': 'rw',
            'size': 1000,
            'used': 500,
            'available': 500
        },
        {
            'mount': '/home',
            'device': '/dev/ada0p3',
            'fstype': 'ufs',
            'options': 'rw',
            'size': 1000,
            'used': 500,
            'available': 500
        }
    ]

    assert 'mounts' in mount_facts
    assert mount_facts['mounts'] == expected_mounts
