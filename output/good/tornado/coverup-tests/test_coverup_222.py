# file tornado/log.py:116-162
# lines [158, 159, 160]
# branches ['144->158', '158->159', '158->160']

import logging
import pytest
from unittest.mock import patch
from tornado.log import LogFormatter

# Assuming the missing coverage is due to the absence of the `curses` module
# or the `colorama` module on Windows, we need to simulate that environment.

@pytest.fixture
def mock_curses_module(mocker):
    # Mock the curses module to simulate its absence
    mocker.patch("tornado.log.curses", None)
    yield

@pytest.fixture
def mock_stderr_supports_color(mocker):
    # Mock the _stderr_supports_color function to return True
    mocker.patch("tornado.log._stderr_supports_color", return_value=True)
    yield

def test_log_formatter_without_curses(mock_curses_module, mock_stderr_supports_color):
    # Define the colors mapping
    colors = {
        logging.DEBUG: 4,  # Blue
        logging.INFO: 2,  # Green
        logging.WARNING: 3,  # Yellow
        logging.ERROR: 1,  # Red
        logging.CRITICAL: 1,  # Red
    }

    # Create an instance of LogFormatter with color enabled
    formatter = LogFormatter(color=True, colors=colors)

    # Check if the ANSI color codes are set correctly
    assert formatter._colors[logging.DEBUG] == "\033[2;34m"
    assert formatter._colors[logging.INFO] == "\033[2;32m"
    assert formatter._colors[logging.WARNING] == "\033[2;33m"
    assert formatter._colors[logging.ERROR] == "\033[2;31m"
    assert formatter._colors[logging.CRITICAL] == "\033[2;31m"
    assert formatter._normal == "\033[0m"
