# file: tornado/log.py:116-162
# asked: {"lines": [116, 118, 119, 120, 121, 122, 139, 140, 142, 143, 144, 145, 147, 151, 152, 154, 158, 159, 160, 162], "branches": [[143, 144], [143, 162], [144, 145], [144, 158], [147, 151], [147, 154], [158, 159], [158, 160]]}
# gained: {"lines": [116, 118, 119, 120, 121, 122, 139, 140, 142, 143, 144, 145, 147, 151, 152, 154, 158, 159, 160, 162], "branches": [[143, 144], [143, 162], [144, 145], [144, 158], [147, 151], [147, 154], [158, 159], [158, 160]]}

import pytest
import logging
from unittest import mock
from tornado.log import LogFormatter
from tornado.util import unicode_type

DEFAULT_FORMAT = "%(color)s%(levelname)s%(end_color)s: %(message)s"
DEFAULT_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
DEFAULT_COLORS = {
    logging.DEBUG: 4,  # Blue
    logging.INFO: 2,   # Green
    logging.WARNING: 3,  # Yellow
    logging.ERROR: 1,  # Red
    logging.CRITICAL: 5,  # Magenta
}

def test_log_formatter_with_color_support(mocker):
    mocker.patch('tornado.log._stderr_supports_color', return_value=True)
    mocker.patch('curses.tigetstr', side_effect=lambda x: b'\x1b[31m' if x in ['setaf', 'setf'] else b'\x1b[0m')
    mocker.patch('curses.tparm', side_effect=lambda fg_color, code: fg_color)
    mocker.patch('curses.tigetnum', return_value=256)
    mocker.patch('curses.setupterm', return_value=True)

    formatter = LogFormatter(color=True, colors=DEFAULT_COLORS)

    assert formatter._colors[logging.DEBUG] == unicode_type(b'\x1b[31m', 'ascii')
    assert formatter._normal == unicode_type(b'\x1b[0m', 'ascii')

def test_log_formatter_without_color_support(mocker):
    mocker.patch('tornado.log._stderr_supports_color', return_value=False)

    formatter = LogFormatter(color=True, colors=DEFAULT_COLORS)

    assert formatter._colors == {}
    assert formatter._normal == ""

def test_log_formatter_without_curses(mocker):
    mocker.patch('tornado.log._stderr_supports_color', return_value=True)
    mocker.patch('tornado.log.curses', None)

    formatter = LogFormatter(color=True, colors=DEFAULT_COLORS)

    assert formatter._colors[logging.DEBUG] == "\033[2;34m"
    assert formatter._normal == "\033[0m"
