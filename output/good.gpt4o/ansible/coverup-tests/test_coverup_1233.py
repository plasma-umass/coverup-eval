# file lib/ansible/module_utils/common/process.py:12-44
# lines [27, 36]
# branches ['26->27', '35->36']

import os
import pytest
from unittest import mock

# Assuming the function is imported from the module
from ansible.module_utils.common.process import get_bin_path

def test_get_bin_path_with_opt_dirs(mocker):
    # Mock os.path.exists to control the behavior of the function
    mocker.patch('os.path.exists', side_effect=lambda x: x in ['/mocked_dir', '/mocked_dir/test_executable', '/sbin', '/usr/sbin', '/usr/local/sbin'])

    # Test with opt_dirs containing a valid directory
    result = get_bin_path('test_executable', opt_dirs=['/mocked_dir'])
    assert result == '/mocked_dir/test_executable'

def test_get_bin_path_with_empty_path(mocker):
    # Mock os.path.exists to control the behavior of the function
    mocker.patch('os.path.exists', side_effect=lambda x: x in ['/sbin', '/usr/sbin', '/usr/local/sbin'])

    # Mock os.environ to control the PATH environment variable
    mocker.patch.dict(os.environ, {'PATH': ''})

    # Test with an empty PATH environment variable
    with pytest.raises(ValueError, match='Failed to find required executable'):
        get_bin_path('test_executable')

# Mock is_executable function to always return True for testing purposes
def is_executable(path):
    return True

# Apply the mock to the is_executable function
@pytest.fixture(autouse=True)
def mock_is_executable(mocker):
    mocker.patch('ansible.module_utils.common.process.is_executable', side_effect=is_executable)
