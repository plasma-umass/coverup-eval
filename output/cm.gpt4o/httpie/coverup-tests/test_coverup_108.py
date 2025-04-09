# file httpie/output/formatters/colors.py:109-156
# lines [137, 144, 145]
# branches []

import pytest
from httpie.output.formatters.colors import get_lexer
from pygments.lexers import JsonLexer, TextLexer
from pygments.util import ClassNotFound
import json

def test_get_lexer_handles_mime_type():
    # This will cover the break statement at line 137
    lexer = get_lexer('application/json')
    assert isinstance(lexer, JsonLexer)

def test_get_lexer_handles_lexer_by_name(mocker):
    # Mocking get_lexer_for_mimetype to raise ClassNotFound to cover lines 144-145
    mocker.patch('pygments.lexers.get_lexer_for_mimetype', side_effect=ClassNotFound)
    lexer = get_lexer('application/vnd.api+json')
    assert isinstance(lexer, JsonLexer)

def test_get_lexer_explicit_json_with_body():
    # This will cover the explicit_json and body condition
    body = '{"key": "value"}'
    lexer = get_lexer('text/plain', explicit_json=True, body=body)
    assert isinstance(lexer, JsonLexer)

def test_get_lexer_explicit_json_with_invalid_body():
    # This will cover the explicit_json and body condition with invalid JSON
    body = 'not a json'
    lexer = get_lexer('text/plain', explicit_json=True, body=body)
    assert isinstance(lexer, TextLexer)

