# file: httpie/output/formatters/colors.py:46-72
# asked: {"lines": [56, 57, 65, 66, 67], "branches": [[55, 56], [61, 65]]}
# gained: {"lines": [56, 57, 65, 66, 67], "branches": [[55, 56], [61, 65]]}

import pytest
from httpie.output.formatters.colors import ColorFormatter, SimplifiedHTTPLexer
from httpie.context import Environment
from pygments.formatters import TerminalFormatter, Terminal256Formatter
from pygments.styles import get_style_by_name

class MockEnvironment(Environment):
    def __init__(self, colors):
        self.colors = colors

@pytest.fixture
def mock_env_0_colors():
    return MockEnvironment(colors=0)

@pytest.fixture
def mock_env_256_colors():
    return MockEnvironment(colors=256)

@pytest.fixture
def mock_env_other_colors():
    return MockEnvironment(colors=16)

def test_color_formatter_disabled(mock_env_0_colors):
    formatter = ColorFormatter(env=mock_env_0_colors, format_options={})
    assert not formatter.enabled

def test_color_formatter_auto_style(mock_env_other_colors, monkeypatch):
    monkeypatch.setattr('httpie.output.formatters.colors.AUTO_STYLE', 'auto')
    formatter = ColorFormatter(env=mock_env_other_colors, color_scheme='auto', format_options={})
    assert isinstance(formatter.formatter, TerminalFormatter)

def test_color_formatter_256_colors(mock_env_256_colors, monkeypatch):
    mock_style_class = get_style_by_name('default')
    monkeypatch.setattr('httpie.output.formatters.colors.ColorFormatter.get_style_class', lambda self, x: mock_style_class)
    formatter = ColorFormatter(env=mock_env_256_colors, color_scheme='default', format_options={})
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)
