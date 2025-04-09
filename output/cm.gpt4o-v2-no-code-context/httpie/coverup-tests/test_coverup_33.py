# file: httpie/output/formatters/colors.py:81-89
# asked: {"lines": [81, 82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}
# gained: {"lines": [81, 82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}

import pytest
from httpie.output.formatters.colors import ColorFormatter
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter
from httpie.context import Environment

@pytest.fixture
def color_formatter():
    env = Environment()
    format_options = {}
    return ColorFormatter(env=env, format_options=format_options)

def test_format_body_with_lexer(monkeypatch, color_formatter):
    body = "print('Hello, world!')"
    mime = "text/x-python"

    def mock_get_lexer_for_body(mime, body):
        return get_lexer_by_name("python")

    monkeypatch.setattr(color_formatter, 'get_lexer_for_body', mock_get_lexer_for_body)
    monkeypatch.setattr(color_formatter, 'formatter', TerminalFormatter())

    formatted_body = color_formatter.format_body(body, mime)
    assert formatted_body != body
    assert "Hello, world!" in formatted_body

def test_format_body_without_lexer(monkeypatch, color_formatter):
    body = "print('Hello, world!')"
    mime = "text/plain"

    def mock_get_lexer_for_body(mime, body):
        return None

    monkeypatch.setattr(color_formatter, 'get_lexer_for_body', mock_get_lexer_for_body)

    formatted_body = color_formatter.format_body(body, mime)
    assert formatted_body == body
