# file lib/ansible/module_utils/facts/hardware/freebsd.py:151-170
# lines []
# branches ['157->170']

import pytest
from unittest.mock import patch, mock_open
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

@pytest.fixture
def freebsd_hardware():
    class MockModule:
        pass

    return FreeBSDHardware(MockModule())

def test_get_mount_facts_with_fstab(freebsd_hardware):
    fstab_content = """
# This is a comment
/dev/ada0p2 / ufs rw 1 1
/dev/ada0p3 none swap sw 0 0
"""
    expected_mounts = [
        {
            'mount': '/',
            'device': '/dev/ada0p2',
            'fstype': 'ufs',
            'options': 'rw',
            'size_total': 0,  # Assuming get_mount_size returns these keys
            'size_available': 0
        },
        {
            'mount': 'none',
            'device': '/dev/ada0p3',
            'fstype': 'swap',
            'options': 'sw',
            'size_total': 0,  # Assuming get_mount_size returns these keys
            'size_available': 0
        }
    ]

    with patch('ansible.module_utils.facts.hardware.freebsd.get_file_content', return_value=fstab_content), \
         patch('ansible.module_utils.facts.hardware.freebsd.get_mount_size', return_value={'size_total': 0, 'size_available': 0}):
        mount_facts = freebsd_hardware.get_mount_facts()
        assert 'mounts' in mount_facts
        assert mount_facts['mounts'] == expected_mounts

def test_get_mount_facts_without_fstab(freebsd_hardware):
    with patch('ansible.module_utils.facts.hardware.freebsd.get_file_content', return_value=''):
        mount_facts = freebsd_hardware.get_mount_facts()
        assert 'mounts' in mount_facts
        assert mount_facts['mounts'] == []
