# file: lib/ansible/module_utils/facts/hardware/sunos.py:145-166
# asked: {"lines": [145, 146, 147, 148, 152, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 166], "branches": [[154, 155], [154, 166], [155, 156], [155, 166]]}
# gained: {"lines": [145, 146, 147, 148, 152, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 166], "branches": [[154, 155], [154, 166], [155, 156], [155, 166]]}

import pytest
from unittest.mock import patch, mock_open, MagicMock

# Assuming the SunOSHardware class and its dependencies are imported from the appropriate module
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

@pytest.fixture
def sunos_hardware():
    module_mock = MagicMock()
    return SunOSHardware(module=module_mock)

def test_get_mount_facts_no_fstab(sunos_hardware):
    with patch('ansible.module_utils.facts.hardware.sunos.get_file_content', return_value=None):
        result = sunos_hardware.get_mount_facts()
        assert result == {'mounts': []}

def test_get_mount_facts_with_fstab(sunos_hardware):
    fstab_content = (
        "/dev/dsk/c0t0d0s0\t/\tufs\t-\t1234567890\n"
        "/dev/dsk/c0t0d0s1\t/var\tufs\t-\t1234567891\n"
    )
    expected_mounts = [
        {
            'mount': '/',
            'device': '/dev/dsk/c0t0d0s0',
            'fstype': 'ufs',
            'options': '-',
            'time': '1234567890',
            'size': 1000000,  # Mocked value
            'used': 500000,   # Mocked value
            'available': 500000,  # Mocked value
            'percent': '50%'  # Mocked value
        },
        {
            'mount': '/var',
            'device': '/dev/dsk/c0t0d0s1',
            'fstype': 'ufs',
            'options': '-',
            'time': '1234567891',
            'size': 1000000,  # Mocked value
            'used': 500000,   # Mocked value
            'available': 500000,  # Mocked value
            'percent': '50%'  # Mocked value
        }
    ]

    with patch('ansible.module_utils.facts.hardware.sunos.get_file_content', return_value=fstab_content):
        with patch('ansible.module_utils.facts.hardware.sunos.get_mount_size', return_value={
            'size': 1000000,
            'used': 500000,
            'available': 500000,
            'percent': '50%'
        }):
            result = sunos_hardware.get_mount_facts()
            assert result['mounts'] == expected_mounts
