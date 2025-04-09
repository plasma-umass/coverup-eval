# file tornado/log.py:116-162
# lines [144, 145, 147, 151, 152, 154, 158, 159, 160]
# branches ['143->144', '144->145', '144->158', '147->151', '147->154', '158->159', '158->160']

import logging
import pytest
import sys
from unittest import mock
from tornado.log import LogFormatter

@pytest.fixture
def mock_curses(mocker):
    mock_curses = mocker.patch('tornado.log.curses', autospec=True)
    mock_curses.tigetstr.side_effect = lambda x: b'\033[2;3%dm' if x in ['setaf', 'setf'] else b'\033[0m'
    mock_curses.tparm.side_effect = lambda fg_color, code: b'\033[2;3%dm' % code
    return mock_curses

@pytest.fixture
def mock_stderr_supports_color(mocker):
    return mocker.patch('tornado.log._stderr_supports_color', return_value=True)

def test_log_formatter_with_curses(mock_curses, mock_stderr_supports_color):
    colors = {logging.DEBUG: 4, logging.INFO: 2, logging.WARNING: 3, logging.ERROR: 1}
    formatter = LogFormatter(color=True, colors=colors)
    
    assert formatter._colors[logging.DEBUG] == '\033[2;34m'
    assert formatter._colors[logging.INFO] == '\033[2;32m'
    assert formatter._colors[logging.WARNING] == '\033[2;33m'
    assert formatter._colors[logging.ERROR] == '\033[2;31m'
    assert formatter._normal == '\033[0m'

def test_log_formatter_without_curses(mocker, mock_stderr_supports_color):
    mocker.patch('tornado.log.curses', None)
    colors = {logging.DEBUG: 4, logging.INFO: 2, logging.WARNING: 3, logging.ERROR: 1}
    formatter = LogFormatter(color=True, colors=colors)
    
    assert formatter._colors[logging.DEBUG] == '\033[2;34m'
    assert formatter._colors[logging.INFO] == '\033[2;32m'
    assert formatter._colors[logging.WARNING] == '\033[2;33m'
    assert formatter._colors[logging.ERROR] == '\033[2;31m'
    assert formatter._normal == '\033[0m'
