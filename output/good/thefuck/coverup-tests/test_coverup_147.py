# file thefuck/entrypoints/shell_logger.py:33-61
# lines [42, 46, 47, 58]
# branches ['41->42', '57->58']

import os
import pty
import signal
import tty
from unittest.mock import patch, MagicMock

import pytest

from thefuck.entrypoints import shell_logger


@pytest.fixture
def mock_pty_fork():
    with patch('pty.fork') as mock_fork:
        yield mock_fork


@pytest.fixture
def mock_execlp():
    with patch('os.execlp') as mock_execlp:
        yield mock_execlp


@pytest.fixture
def mock_tcgetattr():
    with patch('tty.tcgetattr') as mock_tcgetattr:
        yield mock_tcgetattr


@pytest.fixture
def mock_setraw():
    with patch('tty.setraw') as mock_setraw:
        yield mock_setraw


@pytest.fixture
def mock_tcsetattr():
    with patch('tty.tcsetattr') as mock_tcsetattr:
        yield mock_tcsetattr


@pytest.fixture
def mock_signal():
    with patch('signal.signal') as mock_signal:
        yield mock_signal


@pytest.fixture
def mock_copy():
    with patch('pty._copy') as mock_copy:
        yield mock_copy


@pytest.fixture
def mock_os_close():
    with patch('os.close') as mock_close:
        yield mock_close


@pytest.fixture
def mock_os_waitpid():
    with patch('os.waitpid') as mock_waitpid:
        yield mock_waitpid


@pytest.fixture
def mock_set_pty_size():
    with patch('thefuck.entrypoints.shell_logger._set_pty_size') as mock_size:
        yield mock_size


def test_shell_logger_spawn_execlp_and_tcsetattr(
    mock_pty_fork, mock_execlp, mock_tcgetattr, mock_setraw, mock_tcsetattr,
    mock_signal, mock_copy, mock_os_close, mock_os_waitpid, mock_set_pty_size
):
    # Arrange
    master_fd = 123
    mock_pty_fork.return_value = (pty.CHILD, master_fd)
    mock_tcgetattr.return_value = 'mode'
    mock_os_waitpid.return_value = (123, 0)
    mock_execlp.side_effect = OSError('mocked error')

    # Act & Assert
    with pytest.raises(OSError) as exc_info:
        shell_logger._spawn('shell', 'master_read')
    assert str(exc_info.value) == 'mocked error'

    # Assert
    mock_execlp.assert_called_once_with('shell', 'shell')
    mock_tcgetattr.assert_not_called()
    mock_setraw.assert_not_called()
    mock_tcsetattr.assert_not_called()
    mock_signal.assert_not_called()
    mock_copy.assert_not_called()
    mock_os_close.assert_not_called()
    mock_os_waitpid.assert_not_called()

    # Arrange for OSError during copy
    mock_pty_fork.return_value = (123, master_fd)
    mock_copy.side_effect = OSError
    mock_execlp.side_effect = None  # Reset side effect

    # Act
    shell_logger._spawn('shell', 'master_read')

    # Assert
    mock_tcsetattr.assert_called_once_with(pty.STDIN_FILENO, tty.TCSAFLUSH, 'mode')
    mock_os_close.assert_called_once_with(master_fd)
    mock_os_waitpid.assert_called_once_with(123, 0)
