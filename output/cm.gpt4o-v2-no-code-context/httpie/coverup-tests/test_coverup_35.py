# file: httpie/output/formatters/colors.py:101-106
# asked: {"lines": [101, 102, 103, 104, 105, 106], "branches": []}
# gained: {"lines": [101, 102, 103, 104, 105, 106], "branches": []}

import pytest
from httpie.output.formatters.colors import ColorFormatter
from pygments.styles import get_style_by_name
from pygments.util import ClassNotFound
from httpie.output.formatters.colors import Solarized256Style

def test_get_style_class_valid(monkeypatch):
    def mock_get_style_by_name(name):
        class MockStyle:
            pass
        return MockStyle

    monkeypatch.setattr('pygments.styles.get_style_by_name', mock_get_style_by_name)
    style_class = ColorFormatter.get_style_class('monokai')
    assert style_class.__name__ == 'MockStyle'

def test_get_style_class_invalid(monkeypatch):
    def mock_get_style_by_name(name):
        raise ClassNotFound

    monkeypatch.setattr('pygments.styles.get_style_by_name', mock_get_style_by_name)
    style_class = ColorFormatter.get_style_class('invalid_scheme')
    assert style_class == Solarized256Style
