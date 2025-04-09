# file: httpie/output/formatters/colors.py:74-79
# asked: {"lines": [75, 76, 77, 78, 79], "branches": []}
# gained: {"lines": [75, 76, 77, 78, 79], "branches": []}

import pytest
from httpie.output.formatters.colors import ColorFormatter
from pygments.lexers import HttpLexer
from pygments.formatters import TerminalFormatter
from httpie.context import Environment

@pytest.fixture
def color_formatter():
    env = Environment()
    return ColorFormatter(env=env, http_lexer=HttpLexer(), formatter=TerminalFormatter(), format_options={})

def test_format_headers_executes_all_lines(color_formatter, monkeypatch):
    headers = "HTTP/1.1 200 OK\nContent-Type: application/json"
    
    def mock_highlight(code, lexer, formatter):
        assert code == headers
        assert isinstance(lexer, HttpLexer)
        assert isinstance(formatter, TerminalFormatter)
        return "highlighted headers"
    
    monkeypatch.setattr("pygments.highlight", mock_highlight)
    
    result = color_formatter.format_headers(headers)
    assert result == "highlighted headers"
