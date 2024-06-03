# file lib/ansible/module_utils/facts/hardware/netbsd.py:114-135
# lines [114, 115, 116, 118, 119, 121, 122, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135]
# branches ['121->122', '121->124', '124->125', '124->135', '125->126', '125->127']

import pytest
from unittest.mock import patch, mock_open, MagicMock
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardware
import re

@pytest.fixture
def netbsd_hardware():
    module_mock = MagicMock()
    return NetBSDHardware(module_mock)

def test_get_mount_facts_empty_fstab(netbsd_hardware):
    with patch('ansible.module_utils.facts.hardware.netbsd.get_file_content', return_value=''):
        mount_facts = netbsd_hardware.get_mount_facts()
        assert mount_facts == {'mounts': []}

def test_get_mount_facts_with_fstab(netbsd_hardware):
    fstab_content = """
# This is a comment
/dev/sd0a / ffs rw 1 1
/dev/sd0b none swap sw 0 0
"""
    expected_mounts = [
        {'mount': '/', 'device': '/dev/sd0a', 'fstype': 'ffs', 'options': 'rw', 'size': 0, 'used': 0, 'available': 0, 'percent': 0},
        {'mount': 'none', 'device': '/dev/sd0b', 'fstype': 'swap', 'options': 'sw', 'size': 0, 'used': 0, 'available': 0, 'percent': 0}
    ]

    with patch('ansible.module_utils.facts.hardware.netbsd.get_file_content', return_value=fstab_content), \
         patch('ansible.module_utils.facts.hardware.netbsd.get_mount_size', return_value={'size': 0, 'used': 0, 'available': 0, 'percent': 0}):
        mount_facts = netbsd_hardware.get_mount_facts()
        assert mount_facts['mounts'] == expected_mounts

def test_get_mount_facts_ignores_comments_and_empty_lines(netbsd_hardware):
    fstab_content = """
# This is a comment
/dev/sd0a / ffs rw 1 1

# Another comment
/dev/sd0b none swap sw 0 0
"""
    expected_mounts = [
        {'mount': '/', 'device': '/dev/sd0a', 'fstype': 'ffs', 'options': 'rw', 'size': 0, 'used': 0, 'available': 0, 'percent': 0},
        {'mount': 'none', 'device': '/dev/sd0b', 'fstype': 'swap', 'options': 'sw', 'size': 0, 'used': 0, 'available': 0, 'percent': 0}
    ]

    with patch('ansible.module_utils.facts.hardware.netbsd.get_file_content', return_value=fstab_content), \
         patch('ansible.module_utils.facts.hardware.netbsd.get_mount_size', return_value={'size': 0, 'used': 0, 'available': 0, 'percent': 0}):
        mount_facts = netbsd_hardware.get_mount_facts()
        assert mount_facts['mounts'] == expected_mounts
