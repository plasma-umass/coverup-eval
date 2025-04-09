# file: tornado/log.py:116-162
# asked: {"lines": [116, 118, 119, 120, 121, 122, 139, 140, 142, 143, 144, 145, 147, 151, 152, 154, 158, 159, 160, 162], "branches": [[143, 144], [143, 162], [144, 145], [144, 158], [147, 151], [147, 154], [158, 159], [158, 160]]}
# gained: {"lines": [116, 118, 119, 120, 121, 122, 139, 140, 142, 143, 144, 145, 147, 151, 152, 154, 158, 159, 160, 162], "branches": [[143, 144], [143, 162], [144, 145], [144, 158], [147, 151], [147, 154], [158, 159], [158, 160]]}

import logging
import pytest
from unittest import mock
from tornado.log import LogFormatter, _stderr_supports_color

DEFAULT_FORMAT = "%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s"
DEFAULT_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
DEFAULT_COLORS = {
    logging.DEBUG: 4,  # Blue
    logging.INFO: 2,   # Green
    logging.WARNING: 3,  # Yellow
    logging.ERROR: 1,  # Red
    logging.CRITICAL: 5,  # Magenta
}

@pytest.fixture
def mock_curses(mocker):
    mock_curses_module = mocker.patch('tornado.log.curses', create=True)
    mock_curses_module.tigetstr = mock.Mock(side_effect=lambda x: b'\033[0m' if x == 'sgr0' else b'\033[3%dm')
    mock_curses_module.tparm = mock.Mock(side_effect=lambda x, y: b'\033[3%dm' % y)
    return mock_curses_module

@pytest.fixture
def mock_no_curses(mocker):
    mocker.patch('tornado.log.curses', None)

@pytest.fixture
def mock_stderr_supports_color(mocker):
    mocker.patch('tornado.log._stderr_supports_color', return_value=True)

@pytest.fixture
def mock_stderr_no_color(mocker):
    mocker.patch('tornado.log._stderr_supports_color', return_value=False)

def test_log_formatter_with_color_and_curses(mock_curses, mock_stderr_supports_color):
    formatter = LogFormatter(fmt=DEFAULT_FORMAT, datefmt=DEFAULT_DATE_FORMAT, color=True, colors=DEFAULT_COLORS)
    assert formatter._normal == '\033[0m'
    for level, code in DEFAULT_COLORS.items():
        assert formatter._colors[level] == '\033[3%dm' % code

def test_log_formatter_with_color_no_curses(mock_no_curses, mock_stderr_supports_color):
    formatter = LogFormatter(fmt=DEFAULT_FORMAT, datefmt=DEFAULT_DATE_FORMAT, color=True, colors=DEFAULT_COLORS)
    assert formatter._normal == '\033[0m'
    for level, code in DEFAULT_COLORS.items():
        assert formatter._colors[level] == '\033[2;3%dm' % code

def test_log_formatter_no_color(mock_stderr_no_color):
    formatter = LogFormatter(fmt=DEFAULT_FORMAT, datefmt=DEFAULT_DATE_FORMAT, color=False, colors=DEFAULT_COLORS)
    assert formatter._normal == ''
    assert formatter._colors == {}
