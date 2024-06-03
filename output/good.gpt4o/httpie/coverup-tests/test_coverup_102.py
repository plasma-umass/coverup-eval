# file httpie/output/formatters/colors.py:74-79
# lines [75, 76, 77, 78, 79]
# branches []

import pytest
from unittest.mock import Mock, patch
import pygments
from httpie.output.formatters.colors import ColorFormatter
from httpie.context import Environment

@pytest.fixture
def color_formatter():
    env = Mock(spec=Environment)
    formatter = ColorFormatter(env=env, format_options={})
    formatter.http_lexer = Mock()
    formatter.formatter = Mock()
    return formatter

def test_format_headers(color_formatter):
    headers = "HTTP/1.1 200 OK\nContent-Type: application/json"
    
    with patch('pygments.highlight') as mock_highlight:
        mock_highlight.return_value = "highlighted headers\n"
        result = color_formatter.format_headers(headers)
        
        mock_highlight.assert_called_once_with(
            code=headers,
            lexer=color_formatter.http_lexer,
            formatter=color_formatter.formatter,
        )
        assert result == "highlighted headers"
