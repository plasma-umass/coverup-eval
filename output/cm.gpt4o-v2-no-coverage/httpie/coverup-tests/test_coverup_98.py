# file: httpie/output/formatters/colors.py:81-89
# asked: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}
# gained: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}

import pytest
from unittest.mock import patch, Mock
from pygments.lexer import Lexer
from httpie.output.formatters.colors import ColorFormatter
from httpie.context import Environment

@pytest.fixture
def color_formatter():
    env = Mock(spec=Environment)
    env.colors = 256
    return ColorFormatter(env=env, format_options={})

def test_format_body_with_lexer(color_formatter):
    body = "print('Hello, world!')"
    mime = "text/x-python"
    mock_lexer = Mock(spec=Lexer)
    mock_formatter = Mock()

    with patch.object(color_formatter, 'get_lexer_for_body', return_value=mock_lexer) as mock_get_lexer, \
         patch('pygments.highlight', return_value="highlighted code") as mock_highlight:
        color_formatter.formatter = mock_formatter
        result = color_formatter.format_body(body, mime)

        mock_get_lexer.assert_called_once_with(mime, body)
        mock_highlight.assert_called_once_with(code=body, lexer=mock_lexer, formatter=mock_formatter)
        assert result == "highlighted code"

def test_format_body_without_lexer(color_formatter):
    body = "print('Hello, world!')"
    mime = "text/x-python"

    with patch.object(color_formatter, 'get_lexer_for_body', return_value=None) as mock_get_lexer:
        result = color_formatter.format_body(body, mime)

        mock_get_lexer.assert_called_once_with(mime, body)
        assert result == body
