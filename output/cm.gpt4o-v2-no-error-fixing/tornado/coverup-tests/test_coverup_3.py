# file: tornado/log.py:55-71
# asked: {"lines": [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 66, 67, 70, 71], "branches": [[57, 58], [57, 71], [58, 59], [58, 62], [60, 61], [60, 71], [62, 63], [62, 71], [63, 66], [63, 71]]}
# gained: {"lines": [55, 56, 57, 58, 59, 60, 61, 67, 70, 71], "branches": [[57, 58], [57, 71], [58, 59], [60, 61]]}

import pytest
import sys
import colorama
import curses

from unittest import mock

def test_stderr_supports_color_with_curses(monkeypatch):
    # Mock sys.stderr.isatty to return True
    monkeypatch.setattr(sys.stderr, 'isatty', lambda: True)
    
    # Mock curses functions
    monkeypatch.setattr(curses, 'setupterm', lambda: None)
    monkeypatch.setattr(curses, 'tigetnum', lambda x: 8 if x == 'colors' else -1)
    
    from tornado.log import _stderr_supports_color
    assert _stderr_supports_color() == True

def test_stderr_supports_color_with_colorama(monkeypatch):
    # Mock sys.stderr.isatty to return True
    monkeypatch.setattr(sys.stderr, 'isatty', lambda: True)
    
    # Mock colorama.initialise.wrapped_stderr to be sys.stderr
    monkeypatch.setattr(colorama.initialise, 'wrapped_stderr', sys.stderr)
    
    from tornado.log import _stderr_supports_color
    assert _stderr_supports_color() == True

def test_stderr_supports_color_no_color_support(monkeypatch):
    # Mock sys.stderr.isatty to return False
    monkeypatch.setattr(sys.stderr, 'isatty', lambda: False)
    
    from tornado.log import _stderr_supports_color
    assert _stderr_supports_color() == False

def test_stderr_supports_color_exception(monkeypatch):
    # Mock sys.stderr.isatty to raise an exception
    monkeypatch.setattr(sys.stderr, 'isatty', mock.Mock(side_effect=Exception))
    
    from tornado.log import _stderr_supports_color
    assert _stderr_supports_color() == False
