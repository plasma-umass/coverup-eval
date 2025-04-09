# file tornado/log.py:55-71
# lines [62, 63, 64, 66, 67, 70]
# branches ['58->62', '60->71', '62->63', '62->71', '63->66', '63->71']

import sys
import pytest
from unittest.mock import Mock, MagicMock
from tornado.log import _stderr_supports_color

@pytest.fixture
def mock_curses(mocker):
    curses_mock = mocker.patch('tornado.log.curses')
    curses_mock.setupterm = Mock()
    curses_mock.tigetnum = Mock(return_value=8)
    return curses_mock

@pytest.fixture
def mock_colorama(mocker):
    colorama_mock = mocker.patch('tornado.log.colorama')
    colorama_mock.initialise = MagicMock(wrapped_stderr=sys.stderr)
    return colorama_mock

@pytest.fixture
def mock_isatty(mocker):
    return mocker.patch('sys.stderr.isatty', return_value=True)

def test__stderr_supports_color_with_curses(mock_curses, mock_isatty):
    assert _stderr_supports_color() is True
    mock_curses.setupterm.assert_called_once()
    mock_curses.tigetnum.assert_called_once_with("colors")

def test__stderr_supports_color_with_colorama(mock_colorama, mock_isatty):
    assert _stderr_supports_color() is True

def test__stderr_supports_color_without_tty(mocker):
    mocker.patch('sys.stderr.isatty', return_value=False)
    assert _stderr_supports_color() is False

def test__stderr_supports_color_with_exception(mocker):
    mocker.patch('sys.stderr.isatty', return_value=True)
    mocker.patch('tornado.log.curses', side_effect=Exception)
    assert _stderr_supports_color() is False
