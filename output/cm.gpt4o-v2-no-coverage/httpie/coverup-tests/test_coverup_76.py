# file: httpie/output/formatters/colors.py:91-99
# asked: {"lines": [91, 95, 96, 97, 98], "branches": []}
# gained: {"lines": [91, 95, 96, 97, 98], "branches": []}

import pytest
from pygments.lexer import Lexer
from httpie.output.formatters.colors import ColorFormatter
from httpie.context import Environment
from pygments.lexers.special import TextLexer

class MockEnvironment(Environment):
    def __init__(self, colors):
        self.colors = colors

@pytest.fixture
def mock_env():
    return MockEnvironment(colors=256)

def test_get_lexer_for_body(mock_env, mocker):
    mocker.patch('httpie.output.formatters.colors.get_lexer', return_value=TextLexer)
    formatter = ColorFormatter(env=mock_env, explicit_json=True, format_options={})
    lexer = formatter.get_lexer_for_body(mime='application/json', body='{"key": "value"}')
    assert lexer == TextLexer

def test_get_lexer_for_body_no_lexer(mock_env, mocker):
    mocker.patch('httpie.output.formatters.colors.get_lexer', return_value=None)
    formatter = ColorFormatter(env=mock_env, explicit_json=True, format_options={})
    lexer = formatter.get_lexer_for_body(mime='application/unknown', body='some body')
    assert lexer is None
