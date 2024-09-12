# file: httpie/output/formatters/colors.py:46-72
# asked: {"lines": [56, 57, 65, 66, 67], "branches": [[55, 56], [61, 65]]}
# gained: {"lines": [56, 57, 65, 66, 67], "branches": [[55, 56], [61, 65]]}

import pytest
from pygments.formatters.terminal import TerminalFormatter
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers.text import HttpLexer as PygmentsHttpLexer
from httpie.context import Environment
from httpie.output.formatters.colors import ColorFormatter, SimplifiedHTTPLexer, AUTO_STYLE

@pytest.fixture
def mock_env():
    class MockEnvironment(Environment):
        def __init__(self, colors):
            self.colors = colors
    return MockEnvironment

def test_color_formatter_no_colors(mock_env):
    env = mock_env(colors=0)
    formatter = ColorFormatter(env, format_options={})
    assert formatter.enabled is False

def test_color_formatter_auto_style(mock_env, monkeypatch):
    env = mock_env(colors=256)
    monkeypatch.setattr('httpie.output.formatters.colors.AUTO_STYLE', 'auto_style')
    formatter = ColorFormatter(env, color_scheme='auto_style', format_options={})
    assert isinstance(formatter.formatter, TerminalFormatter)
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)

def test_color_formatter_256_colors(mock_env):
    env = mock_env(colors=256)
    formatter = ColorFormatter(env, color_scheme='non_auto_style', format_options={})
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)
