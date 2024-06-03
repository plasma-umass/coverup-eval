# file tornado/log.py:55-71
# lines [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 66, 67, 70, 71]
# branches ['57->58', '57->71', '58->59', '58->62', '60->61', '60->71', '62->63', '62->71', '63->66', '63->71']

import sys
import pytest
import curses
from unittest import mock
from tornado.log import _stderr_supports_color

@pytest.fixture
def mock_sys_stderr_isatty(mocker):
    mock_isatty = mocker.patch.object(sys.stderr, 'isatty', return_value=True)
    yield mock_isatty

@pytest.fixture
def mock_curses_setupterm(mocker):
    mock_setupterm = mocker.patch('curses.setupterm')
    yield mock_setupterm

@pytest.fixture
def mock_curses_tigetnum(mocker):
    mock_tigetnum = mocker.patch('curses.tigetnum', return_value=8)
    yield mock_tigetnum

@pytest.fixture
def mock_colorama_initialise_wrapped_stderr(mocker):
    mock_wrapped_stderr = mocker.patch('colorama.initialise.wrapped_stderr', sys.stderr)
    yield mock_wrapped_stderr

def test_stderr_supports_color_with_curses(mock_sys_stderr_isatty, mock_curses_setupterm, mock_curses_tigetnum):
    assert _stderr_supports_color() is True

def test_stderr_supports_color_with_colorama(mock_sys_stderr_isatty, mock_colorama_initialise_wrapped_stderr):
    with mock.patch('tornado.log.colorama', create=True):
        assert _stderr_supports_color() is True

def test_stderr_supports_color_fallback():
    with mock.patch.object(sys.stderr, 'isatty', return_value=False):
        assert _stderr_supports_color() is False

def test_stderr_supports_color_exception_handling(mocker):
    mocker.patch.object(sys.stderr, 'isatty', side_effect=Exception("Test Exception"))
    assert _stderr_supports_color() is False
