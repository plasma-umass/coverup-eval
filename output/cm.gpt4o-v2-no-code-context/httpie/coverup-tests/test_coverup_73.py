# file: httpie/output/formatters/colors.py:91-99
# asked: {"lines": [95, 96, 97, 98], "branches": []}
# gained: {"lines": [95, 96, 97, 98], "branches": []}

import pytest
from httpie.output.formatters.colors import ColorFormatter
from httpie.plugins import FormatterPlugin
from pygments.lexers import get_lexer_for_mimetype, get_lexer_by_name
from pygments.lexer import Lexer

class MockLexer(Lexer):
    pass

@pytest.fixture
def color_formatter(monkeypatch):
    class TestColorFormatter(ColorFormatter):
        explicit_json = False

        def __init__(self):
            pass

    def mock_get_lexer(mime, explicit_json, body):
        return MockLexer

    monkeypatch.setattr('httpie.output.formatters.colors.get_lexer', mock_get_lexer)
    return TestColorFormatter()

def test_get_lexer_for_body_with_mime(color_formatter):
    lexer = color_formatter.get_lexer_for_body('application/json', '{"key": "value"}')
    assert lexer == MockLexer

def test_get_lexer_for_body_with_explicit_json(color_formatter):
    color_formatter.explicit_json = True
    lexer = color_formatter.get_lexer_for_body('application/json', '{"key": "value"}')
    assert lexer == MockLexer
