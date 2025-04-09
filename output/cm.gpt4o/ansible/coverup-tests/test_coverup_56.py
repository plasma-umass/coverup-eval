# file lib/ansible/module_utils/common/process.py:12-44
# lines [12, 21, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 44]
# branches ['25->26', '25->28', '26->25', '26->27', '31->32', '31->34', '32->31', '32->33', '34->35', '34->41', '35->36', '35->37', '38->34', '38->39', '41->42', '41->44']

import os
import pytest
from unittest import mock
from ansible.module_utils.common.process import get_bin_path

@pytest.fixture
def mock_os_path_exists(mocker):
    def _mock_os_path_exists(path):
        if path in ['/sbin', '/usr/sbin', '/usr/local/sbin', '/mocked/path/to/executable', '/sbin/executable']:
            return True
        return False
    return mocker.patch('os.path.exists', side_effect=_mock_os_path_exists)

@pytest.fixture
def mock_is_executable(mocker):
    return mocker.patch('ansible.module_utils.common.process.is_executable', return_value=True)

def test_get_bin_path_found_in_opt_dirs(mock_os_path_exists, mock_is_executable):
    opt_dirs = ['/mocked/path']
    arg = 'executable'
    with mock.patch('os.path.join', return_value='/mocked/path/to/executable'):
        result = get_bin_path(arg, opt_dirs=opt_dirs)
        assert result == '/mocked/path/to/executable'

def test_get_bin_path_not_found(mock_os_path_exists, mock_is_executable):
    opt_dirs = ['/nonexistent/path']
    arg = 'nonexistent_executable'
    with pytest.raises(ValueError, match='Failed to find required executable'):
        get_bin_path(arg, opt_dirs=opt_dirs)

def test_get_bin_path_found_in_sbin(mock_os_path_exists, mock_is_executable):
    arg = 'executable'
    with mock.patch('os.path.join', side_effect=lambda d, a: f'{d}/{a}'):
        result = get_bin_path(arg)
        assert result == '/sbin/executable'

def test_get_bin_path_found_in_path(mock_os_path_exists, mock_is_executable):
    arg = 'executable'
    with mock.patch.dict('os.environ', {'PATH': '/mocked/path'}):
        with mock.patch('os.path.join', return_value='/mocked/path/to/executable'):
            result = get_bin_path(arg)
            assert result == '/mocked/path/to/executable'
