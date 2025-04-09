# file thefuck/entrypoints/shell_logger.py:27-30
# lines [27, 28, 29, 30]
# branches []

import array
import fcntl
import pty
import termios
import os
import pytest

from thefuck.entrypoints.shell_logger import _set_pty_size

def test_set_pty_size(mocker):
    # Mocking the fcntl.ioctl function
    mock_ioctl = mocker.patch('fcntl.ioctl')

    # Creating a pseudo-terminal
    master_fd, slave_fd = pty.openpty()

    try:
        # Call the function to test
        _set_pty_size(master_fd)

        # Assertions to ensure the ioctl calls were made correctly
        buf = array.array('h', [0, 0, 0, 0])
        mock_ioctl.assert_any_call(pty.STDOUT_FILENO, termios.TIOCGWINSZ, buf, True)
        mock_ioctl.assert_any_call(master_fd, termios.TIOCSWINSZ, buf)
    finally:
        # Clean up the pseudo-terminal
        os.close(master_fd)
        os.close(slave_fd)
