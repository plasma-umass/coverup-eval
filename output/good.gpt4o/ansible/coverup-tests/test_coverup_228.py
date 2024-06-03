# file lib/ansible/module_utils/facts/hardware/openbsd.py:66-86
# lines [66, 67, 68, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]
# branches ['72->73', '72->86', '73->74', '73->86', '74->75', '74->76', '77->78', '77->79']

import pytest
from unittest.mock import patch, mock_open, MagicMock
import re

# Assuming the OpenBSDHardware class is imported from ansible.module_utils.facts.hardware.openbsd
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware

@pytest.fixture
def mock_get_file_content():
    with patch('ansible.module_utils.facts.hardware.openbsd.get_file_content') as mock:
        yield mock

@pytest.fixture
def mock_get_mount_size():
    with patch('ansible.module_utils.facts.hardware.openbsd.get_mount_size') as mock:
        yield mock

def test_get_mount_facts(mock_get_file_content, mock_get_mount_size):
    mock_get_file_content.return_value = """
# This is a comment
/dev/sd0a / ffs rw 1 1
/dev/sd0b none swap sw 0 0
/dev/sd0d /home ffs rw,nodev,nosuid 1 2
/dev/sd0e /tmp ffs rw 1 2
/dev/sd0f /var ffs rw 1 2
/dev/sd0g /usr ffs rw 1 2
/dev/sd0h /usr/local ffs rw 1 2
/dev/sd0i /usr/X11R6 ffs rw 1 2
/dev/sd0j /usr/src ffs rw 1 2
/dev/sd0k /usr/obj ffs rw 1 2
/dev/sd0l /usr/ports ffs rw 1 2
/dev/sd0m /usr/pkg ffs rw 1 2
/dev/sd0n /usr/games ffs rw 1 2
/dev/sd0o /usr/share ffs rw 1 2
/dev/sd0p /usr/local/share ffs rw 1 2
/dev/sd0q /usr/local/lib ffs rw 1 2
/dev/sd0r /usr/local/bin ffs rw 1 2
/dev/sd0s /usr/local/sbin ffs rw 1 2
/dev/sd0t /usr/local/etc ffs rw 1 2
/dev/sd0u /usr/local/include ffs rw 1 2
/dev/sd0v /usr/local/man ffs rw 1 2
/dev/sd0w /usr/local/share/man ffs rw 1 2
/dev/sd0x /usr/local/share/doc ffs rw 1 2
/dev/sd0y /usr/local/share/info ffs rw 1 2
/dev/sd0z /usr/local/share/locale ffs rw 1 2
/dev/sd0aa /usr/local/share/misc ffs rw 1 2
/dev/sd0ab /usr/local/share/zoneinfo ffs rw 1 2
/dev/sd0ac /usr/local/share/terminfo ffs rw 1 2
/dev/sd0ad /usr/local/share/locale/locale.alias ffs rw 1 2
/dev/sd0ae /usr/local/share/locale/locale.dir ffs rw 1 2
"""

    mock_get_mount_size.side_effect = lambda mount: {
        'size_total': 1000000,
        'size_available': 500000
    }

    mock_module = MagicMock()
    hardware = OpenBSDHardware(mock_module)
    mount_facts = hardware.get_mount_facts()

    assert 'mounts' in mount_facts
    assert len(mount_facts['mounts']) > 0
    for mount in mount_facts['mounts']:
        assert 'mount' in mount
        assert 'device' in mount
        assert 'fstype' in mount
        assert 'options' in mount
        assert 'size_total' in mount
        assert 'size_available' in mount
