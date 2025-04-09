# file lib/ansible/executor/discovery/python_target.py:25-38
# lines [29]
# branches ['28->29', '33->36']

import pytest
from ansible.executor.discovery.python_target import get_platform_info
from unittest.mock import MagicMock

# Mock the platform module and the read_utf8_file function
@pytest.fixture
def mock_platform(mocker):
    platform_mock = mocker.patch('ansible.executor.discovery.python_target.platform')
    platform_mock.dist = MagicMock(return_value=('Ubuntu', '18.04', 'Bionic Beaver'))
    return platform_mock

@pytest.fixture
def mock_read_utf8_file(mocker):
    read_utf8_file_mock = mocker.patch('ansible.executor.discovery.python_target.read_utf8_file')
    read_utf8_file_mock.side_effect = lambda x: '' if x == '/etc/os-release' else 'NAME="Ubuntu"'
    return read_utf8_file_mock

# Test function to cover missing lines/branches
def test_get_platform_info_with_dist_and_fallback_os_release(mock_platform, mock_read_utf8_file):
    result = get_platform_info()
    assert result['platform_dist_result'] == ('Ubuntu', '18.04', 'Bionic Beaver')
    assert result['osrelease_content'] == 'NAME="Ubuntu"'
    mock_read_utf8_file.assert_called_with('/usr/lib/os-release')
