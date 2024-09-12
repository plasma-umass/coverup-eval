# file: httpie/output/formatters/colors.py:109-156
# asked: {"lines": [144, 145], "branches": []}
# gained: {"lines": [144, 145], "branches": []}

import pytest
from pygments.util import ClassNotFound
from pygments.lexers.special import TextLexer
from httpie.output.formatters.colors import get_lexer

def test_get_lexer_class_not_found(mocker):
    # Mock the pygments.lexers.get_lexer_by_name to raise ClassNotFound
    mocker.patch('pygments.lexers.get_lexer_by_name', side_effect=ClassNotFound)
    mocker.patch('pygments.lexers.get_lexer_for_mimetype', side_effect=ClassNotFound)

    # Test with a mime type that will trigger the ClassNotFound exception
    lexer = get_lexer('application/unknown+json')
    assert lexer is None

    # Test with a mime type that will trigger the ClassNotFound exception
    lexer = get_lexer('application/unknown')
    assert lexer is None

@pytest.mark.parametrize("mime, expected_lexer", [
    ('application/json', 'json'),
    ('application/vnd.api+json', 'json'),
])
def test_get_lexer_json_subtype(mime, expected_lexer):
    lexer = get_lexer(mime)
    assert lexer.aliases[0] == expected_lexer

def test_get_lexer_explicit_json_with_body():
    body = '{"key": "value"}'
    lexer = get_lexer('text/plain', explicit_json=True, body=body)
    assert lexer.aliases[0] == 'json'

def test_get_lexer_explicit_json_with_invalid_body():
    body = 'not a json body'
    lexer = get_lexer('text/plain', explicit_json=True, body=body)
    assert isinstance(lexer, TextLexer)
