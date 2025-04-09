# file lib/ansible/module_utils/facts/hardware/sunos.py:145-166
# lines [145, 146, 147, 148, 152, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 166]
# branches ['154->155', '154->166', '155->156', '155->166']

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

# Mocking the get_file_content function
def mock_get_file_content(file_path):
    if file_path == '/etc/mnttab':
        return "device1\t/mount1\tfstype1\toptions1\ttime1\n" \
               "device2\t/mount2\tfstype2\toptions2\ttime2"
    return None

# Mocking the get_mount_size function
def mock_get_mount_size(mount_point):
    return {'size_total': 123456789, 'size_available': 987654321}

@pytest.fixture
def sunos_hardware(mocker):
    module_mock = MagicMock()
    hardware = SunOSHardware(module=module_mock)
    mocker.patch('ansible.module_utils.facts.hardware.sunos.get_file_content', side_effect=mock_get_file_content)
    mocker.patch('ansible.module_utils.facts.hardware.sunos.get_mount_size', side_effect=mock_get_mount_size)
    return hardware

def test_get_mount_facts(sunos_hardware):
    expected_mounts = [
        {
            'mount': '/mount1',
            'device': 'device1',
            'fstype': 'fstype1',
            'options': 'options1',
            'time': 'time1',
            'size_total': 123456789,
            'size_available': 987654321
        },
        {
            'mount': '/mount2',
            'device': 'device2',
            'fstype': 'fstype2',
            'options': 'options2',
            'time': 'time2',
            'size_total': 123456789,
            'size_available': 987654321
        }
    ]

    mount_facts = sunos_hardware.get_mount_facts()
    assert 'mounts' in mount_facts
    assert mount_facts['mounts'] == expected_mounts
