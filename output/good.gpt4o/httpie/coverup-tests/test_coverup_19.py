# file httpie/output/formatters/colors.py:81-89
# lines [81, 82, 83, 84, 85, 86, 87, 89]
# branches ['83->84', '83->89']

import pytest
from httpie.output.formatters.colors import ColorFormatter
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter

class MockFormatter(ColorFormatter):
    def __init__(self):
        self.formatter = TerminalFormatter()

    def get_lexer_for_body(self, mime, body):
        if mime == 'application/json':
            return get_lexer_by_name('json')
        return None

@pytest.fixture
def color_formatter():
    return MockFormatter()

def test_format_body_with_lexer(color_formatter):
    body = '{"key": "value"}'
    mime = 'application/json'
    formatted_body = color_formatter.format_body(body, mime)
    assert formatted_body != body
    assert '\x1b[' in formatted_body  # Check for ANSI escape sequences

def test_format_body_without_lexer(color_formatter):
    body = 'plain text'
    mime = 'text/plain'
    formatted_body = color_formatter.format_body(body, mime)
    assert formatted_body == body
