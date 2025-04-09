# file: tornado/log.py:55-71
# asked: {"lines": [58, 59, 60, 61, 62, 63, 64, 66, 67, 70], "branches": [[57, 58], [58, 59], [58, 62], [60, 61], [60, 71], [62, 63], [62, 71], [63, 66], [63, 71]]}
# gained: {"lines": [58, 59, 60, 61, 67, 70], "branches": [[57, 58], [58, 59], [60, 61]]}

import pytest
import sys
import curses
from unittest import mock

# Assuming the function _stderr_supports_color is imported from the module
from tornado.log import _stderr_supports_color

def test_stderr_supports_color_with_curses(monkeypatch):
    # Mock sys.stderr to have isatty return True
    class MockStderr:
        def isatty(self):
            return True

    monkeypatch.setattr(sys, 'stderr', MockStderr())

    # Mock curses functions
    monkeypatch.setattr(curses, 'setupterm', lambda: None)
    monkeypatch.setattr(curses, 'tigetnum', lambda x: 8)

    assert _stderr_supports_color() is True

def test_stderr_supports_color_with_colorama(monkeypatch):
    # Mock sys.stderr to have isatty return True
    class MockStderr:
        def isatty(self):
            return True

    monkeypatch.setattr(sys, 'stderr', MockStderr())

    # Mock colorama and its attributes
    mock_colorama = mock.Mock()
    mock_colorama.initialise.wrapped_stderr = sys.stderr

    monkeypatch.setattr('tornado.log.colorama', mock_colorama)

    assert _stderr_supports_color() is True

def test_stderr_supports_color_no_color_support(monkeypatch):
    # Mock sys.stderr to have isatty return True
    class MockStderr:
        def isatty(self):
            return True

    monkeypatch.setattr(sys, 'stderr', MockStderr())

    # Mock curses to raise an exception
    monkeypatch.setattr(curses, 'setupterm', mock.Mock(side_effect=Exception))

    assert _stderr_supports_color() is False

def test_stderr_supports_color_no_isatty(monkeypatch):
    # Mock sys.stderr to not have isatty
    class MockStderr:
        pass

    monkeypatch.setattr(sys, 'stderr', MockStderr())

    assert _stderr_supports_color() is False
