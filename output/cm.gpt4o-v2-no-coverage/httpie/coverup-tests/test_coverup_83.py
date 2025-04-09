# file: httpie/output/formatters/colors.py:74-79
# asked: {"lines": [74, 75, 76, 77, 78, 79], "branches": []}
# gained: {"lines": [74, 75, 76, 77, 78, 79], "branches": []}

import pytest
from pygments.lexers.text import HttpLexer as PygmentsHttpLexer
from pygments.formatters.terminal import TerminalFormatter
from httpie.context import Environment
from httpie.output.formatters.colors import ColorFormatter

@pytest.fixture
def color_formatter():
    env = Environment(colors=256)
    return ColorFormatter(env=env, format_options={})

def test_format_headers(color_formatter):
    headers = "HTTP/1.1 200 OK\nContent-Type: application/json"
    formatted_headers = color_formatter.format_headers(headers)
    assert formatted_headers.startswith('\x1b[')  # Check if it starts with ANSI escape code
    assert "\x1b[34mHTTP\x1b[39;49;00m/\x1b[34m1.1\x1b[39;49;00m \x1b[34m200\x1b[39;49;00m \x1b[36mOK\x1b[39;49;00m" in formatted_headers
    assert "\x1b[36mContent-Type\x1b[39;49;00m: application/json" in formatted_headers
