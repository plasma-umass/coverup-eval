# file lib/ansible/module_utils/common/process.py:12-44
# lines [36]
# branches ['35->36']

import os
import pytest
from ansible.module_utils.common.process import get_bin_path

@pytest.fixture
def mock_os_path_exists(mocker):
    return mocker.patch('os.path.exists')

@pytest.fixture
def mock_os_path_isdir(mocker):
    return mocker.patch('os.path.isdir')

@pytest.fixture
def mock_is_executable(mocker):
    return mocker.patch('ansible.module_utils.common.process.is_executable')

@pytest.fixture
def mock_os_environ(mocker):
    return mocker.patch.dict('os.environ', {'PATH': '/usr/bin:/bin'})

def test_get_bin_path_empty_dir_in_path(mock_os_path_exists, mock_os_path_isdir, mock_is_executable, mock_os_environ):
    # Setup the mock to simulate an empty directory in the PATH
    mock_os_path_exists.side_effect = lambda x: x not in ['/sbin', '/usr/sbin', '/usr/local/sbin']
    mock_os_path_isdir.return_value = False
    mock_is_executable.return_value = True

    # Add an empty entry to the PATH
    original_path = os.environ['PATH']
    os.environ['PATH'] = os.pathsep + os.environ['PATH']

    # Call get_bin_path with a valid executable that should be found
    executable = 'ls'
    expected_path = '/usr/bin/ls'
    mock_os_path_exists.side_effect = lambda x: x == expected_path
    actual_path = get_bin_path(executable)

    # Verify that the expected path is returned
    assert actual_path == expected_path

    # Cleanup by restoring the original PATH
    os.environ['PATH'] = original_path

    # Verify that the mocks were called as expected
    mock_os_path_exists.assert_any_call(expected_path)
    mock_os_path_isdir.assert_called_once_with(expected_path)
    mock_is_executable.assert_called_once_with(expected_path)
