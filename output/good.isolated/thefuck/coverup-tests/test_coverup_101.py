# file thefuck/entrypoints/shell_logger.py:27-30
# lines [27, 28, 29, 30]
# branches []

import array
import fcntl
import os
import pty
import termios
import pytest
from unittest.mock import patch, call

# Assuming the module is named shell_logger and the function is _set_pty_size
from thefuck.entrypoints import shell_logger

@pytest.fixture
def pty_pair():
    master_fd, slave_fd = pty.openpty()
    yield master_fd, slave_fd
    os.close(master_fd)
    os.close(slave_fd)

def test_set_pty_size(pty_pair):
    master_fd, slave_fd = pty_pair

    with patch('fcntl.ioctl') as mock_ioctl:
        shell_logger._set_pty_size(master_fd)
        assert mock_ioctl.call_count == 2

        # Check if the calls to ioctl were with the correct arguments
        buf = array.array('h', [0, 0, 0, 0])
        fcntl.ioctl(pty.STDOUT_FILENO, termios.TIOCGWINSZ, buf, True)
        expected_calls = [
            call(pty.STDOUT_FILENO, termios.TIOCGWINSZ, buf, True),
            call(master_fd, termios.TIOCSWINSZ, buf)
        ]
        mock_ioctl.assert_has_calls(expected_calls, any_order=True)
