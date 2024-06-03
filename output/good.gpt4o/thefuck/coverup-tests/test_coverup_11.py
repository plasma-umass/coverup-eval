# file thefuck/entrypoints/shell_logger.py:33-61
# lines [33, 39, 41, 42, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 58, 60, 61]
# branches ['41->42', '41->44', '57->58', '57->60']

import os
import pty
import signal
import tty
import pytest
from unittest import mock
from thefuck.entrypoints.shell_logger import _spawn

@pytest.fixture
def mock_pty_fork(mocker):
    mocker.patch('pty.fork', return_value=(0, 3))

@pytest.fixture
def mock_os_execlp(mocker):
    mocker.patch('os.execlp')

@pytest.fixture
def mock_tty_tcgetattr(mocker):
    mocker.patch('tty.tcgetattr', return_value='mode')

@pytest.fixture
def mock_tty_setraw(mocker):
    mocker.patch('tty.setraw')

@pytest.fixture
def mock_tty_tcsetattr(mocker):
    mocker.patch('tty.tcsetattr')

@pytest.fixture
def mock_set_pty_size(mocker):
    mocker.patch('thefuck.entrypoints.shell_logger._set_pty_size')

@pytest.fixture
def mock_signal_signal(mocker):
    mocker.patch('signal.signal')

@pytest.fixture
def mock_pty_copy(mocker):
    mocker.patch('pty._copy')

@pytest.fixture
def mock_os_close(mocker):
    mocker.patch('os.close')

@pytest.fixture
def mock_os_waitpid(mocker):
    mocker.patch('os.waitpid', return_value=(1234, 0))

def test_spawn(mock_pty_fork, mock_os_execlp, mock_tty_tcgetattr, mock_tty_setraw, mock_tty_tcsetattr, mock_set_pty_size, mock_signal_signal, mock_pty_copy, mock_os_close, mock_os_waitpid):
    shell = '/bin/bash'
    master_read = mock.Mock()

    exit_status = _spawn(shell, master_read)

    assert exit_status == 0
    pty.fork.assert_called_once()
    os.execlp.assert_called_once_with(shell, shell)
    tty.tcgetattr.assert_called_once_with(pty.STDIN_FILENO)
    tty.setraw.assert_called_once_with(pty.STDIN_FILENO)
    signal.signal.assert_called_once()
    pty._copy.assert_called_once_with(3, master_read, pty._read)
    os.close.assert_called_once_with(3)
    os.waitpid.assert_called_once_with(0, 0)
