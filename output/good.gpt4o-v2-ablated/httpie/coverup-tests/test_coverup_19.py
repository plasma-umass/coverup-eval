# file: httpie/output/formatters/colors.py:101-106
# asked: {"lines": [101, 102, 103, 104, 105, 106], "branches": []}
# gained: {"lines": [101, 102, 103, 104, 105, 106], "branches": []}

import pytest
from httpie.output.formatters.colors import ColorFormatter, Solarized256Style
from pygments.styles import get_style_by_name
from pygments.util import ClassNotFound

def test_get_style_class_valid_scheme(monkeypatch):
    class MockStyle:
        pass

    def mock_get_style_by_name(name):
        if name == "valid_scheme":
            return MockStyle
        raise ClassNotFound

    monkeypatch.setattr("pygments.styles.get_style_by_name", mock_get_style_by_name)
    style_class = ColorFormatter.get_style_class("valid_scheme")
    assert style_class is MockStyle

def test_get_style_class_invalid_scheme(monkeypatch):
    def mock_get_style_by_name(name):
        raise ClassNotFound

    monkeypatch.setattr("pygments.styles.get_style_by_name", mock_get_style_by_name)
    style_class = ColorFormatter.get_style_class("invalid_scheme")
    assert style_class is Solarized256Style
