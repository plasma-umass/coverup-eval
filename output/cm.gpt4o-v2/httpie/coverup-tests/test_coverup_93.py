# file: httpie/output/formatters/colors.py:91-99
# asked: {"lines": [91, 95, 96, 97, 98], "branches": []}
# gained: {"lines": [91, 95, 96, 97, 98], "branches": []}

import pytest
from httpie.output.formatters.colors import ColorFormatter
from httpie.context import Environment
from pygments.lexers import JsonLexer, TextLexer

@pytest.fixture
def color_formatter():
    env = Environment(colors=256)
    return ColorFormatter(env=env, explicit_json=True, format_options={})

def test_get_lexer_for_body_json(color_formatter):
    lexer = color_formatter.get_lexer_for_body(mime='application/json', body='{"key": "value"}')
    assert isinstance(lexer, JsonLexer)

def test_get_lexer_for_body_text(color_formatter):
    lexer = color_formatter.get_lexer_for_body(mime='text/plain', body='Just some text.')
    assert isinstance(lexer, TextLexer)

def test_get_lexer_for_body_invalid_json(color_formatter):
    lexer = color_formatter.get_lexer_for_body(mime='application/json', body='{"key": "value"')
    assert isinstance(lexer, JsonLexer)
