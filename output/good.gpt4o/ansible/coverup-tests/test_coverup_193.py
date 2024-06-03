# file lib/ansible/module_utils/facts/hardware/sunos.py:145-166
# lines [145, 146, 147, 148, 152, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 166]
# branches ['154->155', '154->166', '155->156', '155->166']

import pytest
from unittest.mock import patch, Mock

# Assuming the SunOSHardware class and its dependencies are imported from the module
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

@pytest.fixture
def sunos_hardware():
    # Mocking the module argument required by the Hardware base class
    module_mock = Mock()
    return SunOSHardware(module=module_mock)

@patch('ansible.module_utils.facts.hardware.sunos.get_file_content')
@patch('ansible.module_utils.facts.hardware.sunos.get_mount_size')
def test_get_mount_facts(mock_get_mount_size, mock_get_file_content, sunos_hardware):
    # Mock the content of /etc/mnttab
    mock_get_file_content.return_value = (
        "/dev/dsk/c0t0d0s0\t/\tufs\trw\t1234567890\n"
        "/dev/dsk/c0t0d0s1\t/var\tufs\trw\t1234567891\n"
    )
    
    # Mock the return value of get_mount_size
    mock_get_mount_size.side_effect = [
        {'size': 1024, 'used': 512, 'available': 512, 'percent': '50%'},
        {'size': 2048, 'used': 1024, 'available': 1024, 'percent': '50%'}
    ]
    
    expected_mount_facts = {
        'mounts': [
            {
                'mount': '/',
                'device': '/dev/dsk/c0t0d0s0',
                'fstype': 'ufs',
                'options': 'rw',
                'time': '1234567890',
                'size': 1024,
                'used': 512,
                'available': 512,
                'percent': '50%'
            },
            {
                'mount': '/var',
                'device': '/dev/dsk/c0t0d0s1',
                'fstype': 'ufs',
                'options': 'rw',
                'time': '1234567891',
                'size': 2048,
                'used': 1024,
                'available': 1024,
                'percent': '50%'
            }
        ]
    }
    
    mount_facts = sunos_hardware.get_mount_facts()
    
    assert mount_facts == expected_mount_facts
    mock_get_file_content.assert_called_once_with('/etc/mnttab')
    assert mock_get_mount_size.call_count == 2
    mock_get_mount_size.assert_any_call('/')
    mock_get_mount_size.assert_any_call('/var')
