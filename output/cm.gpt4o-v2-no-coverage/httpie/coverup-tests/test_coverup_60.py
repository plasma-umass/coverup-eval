# file: httpie/output/formatters/colors.py:101-106
# asked: {"lines": [101, 102, 103, 104, 105, 106], "branches": []}
# gained: {"lines": [101, 102, 103, 104, 105, 106], "branches": []}

import pytest
from pygments.util import ClassNotFound
from httpie.output.formatters.colors import ColorFormatter, Solarized256Style
from pygments.styles import get_style_by_name
from pygments.style import Style

def test_get_style_class_valid_style(monkeypatch):
    def mock_get_style_by_name(name):
        return Style

    monkeypatch.setattr("pygments.styles.get_style_by_name", mock_get_style_by_name)
    style_class = ColorFormatter.get_style_class("default")
    assert style_class is Style

def test_get_style_class_invalid_style(monkeypatch):
    def mock_get_style_by_name(name):
        raise ClassNotFound

    monkeypatch.setattr("pygments.styles.get_style_by_name", mock_get_style_by_name)
    style_class = ColorFormatter.get_style_class("nonexistent")
    assert style_class is Solarized256Style
