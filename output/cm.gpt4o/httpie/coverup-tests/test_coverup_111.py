# file httpie/output/formatters/colors.py:46-72
# lines [56, 57, 65, 66, 67]
# branches ['55->56', '61->65']

import pytest
from httpie.output.formatters.colors import ColorFormatter
from httpie.context import Environment
from httpie.plugins import FormatterPlugin
from pygments.formatters import Terminal256Formatter, TerminalFormatter
from pygments.styles import get_style_by_name

class MockEnvironment(Environment):
    def __init__(self, colors):
        self.colors = colors

@pytest.fixture
def mock_env_256_colors():
    return MockEnvironment(colors=256)

@pytest.fixture
def mock_env_no_colors():
    return MockEnvironment(colors=0)

def test_color_formatter_no_colors(mock_env_no_colors):
    formatter = ColorFormatter(env=mock_env_no_colors, format_options={})
    assert not formatter.enabled

def test_color_formatter_256_colors(mock_env_256_colors, mocker):
    mocker.patch('httpie.output.formatters.colors.SimplifiedHTTPLexer', autospec=True)
    mocker.patch('httpie.output.formatters.colors.ColorFormatter.get_style_class', return_value=get_style_by_name('default'))
    
    formatter = ColorFormatter(env=mock_env_256_colors, color_scheme='default', format_options={})
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert formatter.http_lexer is not None
    assert formatter.explicit_json is False
