# file thefuck/entrypoints/shell_logger.py:14-24
# lines [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
# branches []

import os
import pytest
from thefuck.entrypoints import shell_logger
from thefuck import const

@pytest.fixture
def mock_file(mocker):
    mock = mocker.mock_open()
    mocker.patch('thefuck.entrypoints.shell_logger.open', mock)
    return mock

@pytest.fixture
def mock_os_read(mocker):
    mocker.patch('os.read', return_value=b'test_data')
    return os.read

@pytest.fixture
def mock_const(mocker):
    mocker.patch.object(const, 'LOG_SIZE_IN_BYTES', 1024)
    mocker.patch.object(const, 'LOG_SIZE_TO_CLEAN', 512)
    return const

def test__read_with_value_error(mock_file, mock_os_read, mock_const, mocker):
    mock_fd = mocker.Mock()
    mock_fd.fileno.return_value = 3
    mock_file.return_value.write.side_effect = [ValueError, None]
    mock_file.return_value.move = mocker.Mock()
    mock_file.return_value.seek = mocker.Mock()

    with shell_logger.open('test.log', 'wb') as f:
        data = shell_logger._read(f, mock_fd.fileno())

    assert data == b'test_data'
    assert mock_file.return_value.move.call_count == 1
    assert mock_file.return_value.move.call_args == mocker.call(0, const.LOG_SIZE_TO_CLEAN, const.LOG_SIZE_IN_BYTES - const.LOG_SIZE_TO_CLEAN)
    assert mock_file.return_value.seek.call_count == 2
    assert mock_file.return_value.seek.call_args_list[0] == mocker.call(const.LOG_SIZE_IN_BYTES - const.LOG_SIZE_TO_CLEAN)
    assert mock_file.return_value.seek.call_args_list[1] == mocker.call(const.LOG_SIZE_IN_BYTES - const.LOG_SIZE_TO_CLEAN)
    assert mock_file.return_value.write.call_count == 2
    assert mock_file.return_value.write.call_args_list[1] == mocker.call(b'\x00' * const.LOG_SIZE_TO_CLEAN)
