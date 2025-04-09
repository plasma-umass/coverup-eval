# file thefuck/entrypoints/shell_logger.py:33-61
# lines [39, 41, 42, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 58, 60, 61]
# branches ['41->42', '41->44', '57->58', '57->60']

import os
import pty
import pytest
import signal
import tty
from unittest.mock import patch, ANY
from thefuck.entrypoints import shell_logger


@pytest.fixture
def mock_pty_fork(mocker):
    mocker.patch('pty.fork', return_value=(12345, 67890))
    yield pty.fork


@pytest.fixture
def mock_execlp(mocker):
    mocker.patch('os.execlp')
    yield os.execlp


@pytest.fixture
def mock_tcgetattr(mocker):
    mocker.patch('tty.tcgetattr', side_effect=tty.error)
    yield tty.tcgetattr


@pytest.fixture
def mock_tcsetattr(mocker):
    mocker.patch('tty.tcsetattr')
    yield tty.tcsetattr


@pytest.fixture
def mock_signal(mocker):
    mocker.patch('signal.signal')
    yield signal.signal


@pytest.fixture
def mock_os_close(mocker):
    mocker.patch('os.close')
    yield os.close


@pytest.fixture
def mock_os_waitpid(mocker):
    mocker.patch('os.waitpid', return_value=(12345, 0))
    yield os.waitpid


@pytest.fixture
def mock_pty_copy(mocker):
    mocker.patch('pty._copy', side_effect=OSError)
    yield pty._copy


def test_shell_logger_spawn(mock_pty_fork, mock_execlp, mock_tcgetattr, mock_tcsetattr, mock_signal, mock_os_close, mock_os_waitpid, mock_pty_copy):
    with patch('thefuck.entrypoints.shell_logger._set_pty_size') as mock_set_pty_size:
        exit_status = shell_logger._spawn('bash', lambda fd: None)
        assert exit_status == 0
        mock_pty_fork.assert_called_once()
        mock_tcgetattr.assert_called_once_with(pty.STDIN_FILENO)
        mock_tcsetattr.assert_not_called()
        mock_signal.assert_called_once()
        mock_os_close.assert_called_once_with(67890)
        mock_os_waitpid.assert_called_once_with(12345, 0)
        mock_set_pty_size.assert_called()
        mock_pty_copy.assert_called_once_with(67890, ANY, pty._read)
