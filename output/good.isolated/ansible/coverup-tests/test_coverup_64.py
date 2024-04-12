# file lib/ansible/module_utils/common/process.py:12-44
# lines [12, 21, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44]
# branches ['25->26', '25->28', '26->25', '26->27', '31->32', '31->34', '32->31', '32->33', '34->35', '34->41', '35->36', '35->37', '38->34', '38->39', '41->42', '41->44']

import os
import pytest
import stat
from unittest.mock import MagicMock

# Assuming the module under test is 'ansible.module_utils.common.process'
# and the function to test is 'get_bin_path'
from ansible.module_utils.common.process import get_bin_path

# Mock the is_executable function to always return True
@pytest.fixture
def mock_is_executable(mocker):
    return mocker.patch('ansible.module_utils.common.process.is_executable', return_value=True)

# Mock os.path.exists to control the test environment
@pytest.fixture
def mock_os_path_exists(mocker):
    return mocker.patch('os.path.exists', return_value=True)

# Mock os.access to control the test environment
@pytest.fixture
def mock_os_access(mocker):
    return mocker.patch('os.access', return_value=True)

# Mock os.environ to control the test environment
@pytest.fixture
def mock_os_environ(mocker):
    return mocker.patch.dict('os.environ', {'PATH': '/usr/bin'})

# Mock os.path.isdir to always return False
@pytest.fixture
def mock_os_path_isdir(mocker):
    return mocker.patch('os.path.isdir', return_value=False)

# Mock os.stat to simulate executable file stats
@pytest.fixture
def mock_os_stat(mocker):
    fake_stat = MagicMock(st_mode=(stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO))
    return mocker.patch('os.stat', return_value=fake_stat)

def test_get_bin_path_executable_found(mock_os_path_exists, mock_os_access, mock_os_environ, mock_os_path_isdir, mock_os_stat, mock_is_executable):
    executable = 'fake_executable'
    expected_path = '/usr/bin/' + executable
    assert get_bin_path(executable) == expected_path

def test_get_bin_path_executable_not_found(mock_os_path_exists, mock_os_access, mock_os_environ, mock_os_path_isdir, mock_os_stat, mock_is_executable):
    mock_os_path_exists.return_value = False
    executable = 'nonexistent_executable'
    with pytest.raises(ValueError):
        get_bin_path(executable)

def test_get_bin_path_with_opt_dirs(mock_os_path_exists, mock_os_access, mock_os_environ, mock_os_path_isdir, mock_os_stat, mock_is_executable):
    mock_os_path_exists.side_effect = lambda path: path.startswith('/opt')
    executable = 'fake_executable'
    opt_dirs = ['/opt/bin']
    expected_path = '/opt/bin/' + executable
    assert get_bin_path(executable, opt_dirs=opt_dirs) == expected_path

def test_get_bin_path_with_sbin_in_path(mock_os_path_exists, mock_os_access, mock_os_environ, mock_os_path_isdir, mock_os_stat, mock_is_executable):
    mock_os_path_exists.side_effect = lambda path: '/sbin' in path
    executable = 'fake_executable'
    expected_path = '/sbin/' + executable
    assert get_bin_path(executable) == expected_path

def test_get_bin_path_with_empty_path_elements(mock_os_path_exists, mock_os_access, mocker, mock_os_path_isdir, mock_os_stat, mock_is_executable):
    mocker.patch.dict('os.environ', {'PATH': '/usr/bin::/bin'})
    mock_os_path_exists.side_effect = lambda path: '/usr/bin' in path
    executable = 'fake_executable'
    expected_path = '/usr/bin/' + executable
    assert get_bin_path(executable) == expected_path
