# file lib/ansible/module_utils/common/process.py:12-44
# lines [36]
# branches ['26->25', '35->36']

import os
import pytest
from ansible.module_utils.common.process import get_bin_path

@pytest.fixture
def mock_os_path_exists(mocker):
    return mocker.patch('os.path.exists')

@pytest.fixture
def mock_is_executable(mocker):
    return mocker.patch('ansible.module_utils.common.process.is_executable')

def test_get_bin_path_with_empty_and_none_in_opt_dirs(mock_os_path_exists, mock_is_executable, tmp_path):
    # Setup a temporary directory and file to act as the executable
    temp_dir = tmp_path / "opt_bin"
    temp_dir.mkdir()
    temp_executable = temp_dir / "my_executable"
    temp_executable.touch()

    # Mock os.path.exists to return True for the temp_dir and the executable
    mock_os_path_exists.side_effect = lambda path: path == str(temp_dir) or path == str(temp_executable)
    mock_is_executable.return_value = True

    # Call get_bin_path with None and empty string in opt_dirs to trigger line 36 and branch 26->25
    executable_path = get_bin_path("my_executable", opt_dirs=[None, '', str(temp_dir)])

    # Assert that the returned path is correct
    assert executable_path == str(temp_executable)

    # Cleanup is handled by pytest's tmp_path fixture
