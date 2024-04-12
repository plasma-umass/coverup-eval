# file lib/ansible/module_utils/facts/hardware/sunos.py:145-166
# lines []
# branches ['154->166']

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

@pytest.fixture
def sunos_hardware(mocker):
    module_mock = Mock()
    return SunOSHardware(module=module_mock)

@pytest.fixture
def mock_get_file_content(mocker):
    return mocker.patch('ansible.module_utils.facts.hardware.sunos.get_file_content')

@pytest.fixture
def mock_get_mount_size(mocker):
    return mocker.patch('ansible.module_utils.facts.hardware.sunos.get_mount_size')

def test_get_mount_facts_with_no_content(sunos_hardware, mock_get_file_content, mock_get_mount_size):
    # Mock the content of /etc/mnttab to be None to test the branch 154->166
    mock_get_file_content.return_value = None

    mount_facts = sunos_hardware.get_mount_facts()

    assert 'mounts' in mount_facts
    assert mount_facts['mounts'] == []
    mock_get_file_content.assert_called_once_with('/etc/mnttab')
    mock_get_mount_size.assert_not_called()
