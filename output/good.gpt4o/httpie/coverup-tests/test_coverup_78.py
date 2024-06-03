# file httpie/output/formatters/colors.py:91-99
# lines [91, 95, 96, 97, 98]
# branches []

import pytest
from httpie.output.formatters.colors import ColorFormatter
from httpie.plugins import FormatterPlugin
from pygments.lexers import get_lexer_for_mimetype, get_lexer_by_name
from typing import Optional, Type
from pygments.lexer import Lexer
from httpie.context import Environment

class MockLexer(Lexer):
    pass

@pytest.fixture
def mock_get_lexer(mocker):
    return mocker.patch('httpie.output.formatters.colors.get_lexer', return_value=MockLexer)

def test_get_lexer_for_body(mock_get_lexer):
    env = Environment()
    formatter = ColorFormatter(env=env, format_options={})
    formatter.explicit_json = False
    mime = 'application/json'
    body = '{"key": "value"}'
    
    lexer = formatter.get_lexer_for_body(mime, body)
    
    mock_get_lexer.assert_called_once_with(mime=mime, explicit_json=formatter.explicit_json, body=body)
    assert lexer == MockLexer
