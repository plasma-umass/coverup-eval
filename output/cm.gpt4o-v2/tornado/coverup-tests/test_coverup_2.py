# file: tornado/log.py:116-162
# asked: {"lines": [116, 118, 119, 120, 121, 122, 139, 140, 142, 143, 144, 145, 147, 151, 152, 154, 158, 159, 160, 162], "branches": [[143, 144], [143, 162], [144, 145], [144, 158], [147, 151], [147, 154], [158, 159], [158, 160]]}
# gained: {"lines": [116, 118, 119, 120, 121, 122, 139, 140, 142, 143, 144, 145, 147, 151, 152, 154, 158, 159, 160, 162], "branches": [[143, 144], [143, 162], [144, 145], [144, 158], [147, 151], [147, 154], [158, 159], [158, 160]]}

import pytest
import logging
from unittest import mock
from tornado.log import LogFormatter

@pytest.fixture
def mock_curses(monkeypatch):
    mock_curses = mock.Mock()
    monkeypatch.setattr("tornado.log.curses", mock_curses)
    return mock_curses

@pytest.fixture
def mock_stderr_supports_color(monkeypatch):
    monkeypatch.setattr("tornado.log._stderr_supports_color", lambda: True)

def test_log_formatter_with_color_and_curses(mock_curses, mock_stderr_supports_color):
    mock_curses.tigetstr.side_effect = lambda x: b"\x1b[31m" if x in ["setaf", "setf"] else b"\x1b[0m"
    mock_curses.tparm.side_effect = lambda fg_color, code: fg_color

    formatter = LogFormatter(color=True)
    
    assert formatter._colors
    assert formatter._normal == "\x1b[0m"

def test_log_formatter_with_color_without_curses(mock_stderr_supports_color, monkeypatch):
    monkeypatch.setattr("tornado.log.curses", None)

    formatter = LogFormatter(color=True)
    
    assert formatter._colors
    assert formatter._normal == "\033[0m"

def test_log_formatter_without_color(mock_stderr_supports_color):
    formatter = LogFormatter(color=False)
    
    assert not formatter._colors
    assert formatter._normal == ""
