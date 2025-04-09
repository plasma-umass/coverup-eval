# file httpie/output/formatters/colors.py:109-156
# lines [109, 111, 112, 115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156]
# branches ['117->118', '117->120', '129->130', '129->133', '134->135', '134->141', '141->134', '141->142', '147->149', '147->156']

import pytest
from httpie.output.formatters.colors import get_lexer
from pygments.lexers import JsonLexer, TextLexer
from pygments.util import ClassNotFound
import json

def test_get_lexer_json_mime_type():
    lexer = get_lexer('application/json')
    assert isinstance(lexer, JsonLexer)

def test_get_lexer_subtype_with_plus():
    lexer = get_lexer('application/vnd.api+json')
    assert isinstance(lexer, JsonLexer)

def test_get_lexer_fallback_to_json():
    lexer = get_lexer('application/unknown+json')
    assert isinstance(lexer, JsonLexer)

def test_get_lexer_explicit_json_with_body():
    body = '{"key": "value"}'
    lexer = get_lexer('application/unknown', explicit_json=True, body=body)
    assert isinstance(lexer, JsonLexer)

def test_get_lexer_explicit_json_with_invalid_body():
    body = 'not a json'
    lexer = get_lexer('application/unknown', explicit_json=True, body=body)
    assert isinstance(lexer, TextLexer)

def test_get_lexer_no_lexer_found():
    lexer = get_lexer('application/unknown')
    assert isinstance(lexer, TextLexer)

@pytest.fixture(autouse=True)
def mock_pygments_lexers(mocker):
    mocker.patch('pygments.lexers.get_lexer_for_mimetype', side_effect=ClassNotFound)
    mocker.patch('pygments.lexers.get_lexer_by_name', side_effect=lambda name: JsonLexer() if name == 'json' else TextLexer())
