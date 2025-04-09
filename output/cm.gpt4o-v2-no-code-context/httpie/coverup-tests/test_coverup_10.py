# file: httpie/output/formatters/colors.py:109-156
# asked: {"lines": [109, 111, 112, 115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}
# gained: {"lines": [109, 111, 112, 115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}

import pytest
from httpie.output.formatters.colors import get_lexer
from pygments.lexers import JsonLexer, TextLexer
from pygments.util import ClassNotFound
import json

def test_get_lexer_basic_mime():
    lexer = get_lexer('application/json')
    assert isinstance(lexer, JsonLexer)

def test_get_lexer_with_subtype_suffix():
    lexer = get_lexer('application/vnd.api+json')
    assert isinstance(lexer, JsonLexer)

def test_get_lexer_with_invalid_mime():
    lexer = get_lexer('invalid/mime')
    assert lexer is None

def test_get_lexer_with_explicit_json_and_valid_body():
    lexer = get_lexer('text/plain', explicit_json=True, body='{"key": "value"}')
    assert isinstance(lexer, JsonLexer)

def test_get_lexer_with_explicit_json_and_invalid_body():
    lexer = get_lexer('text/plain', explicit_json=True, body='not a json')
    assert isinstance(lexer, TextLexer)

def test_get_lexer_with_json_in_subtype():
    lexer = get_lexer('application/vnd.api+json')
    assert isinstance(lexer, JsonLexer)

def test_get_lexer_with_fallback_to_subtype():
    lexer = get_lexer('application/vnd.api+xml')
    assert lexer is None  # Assuming no lexer for 'vnd.api' or 'xml'

def test_get_lexer_with_fallback_to_json():
    lexer = get_lexer('application/vnd.api+json')
    assert isinstance(lexer, JsonLexer)

@pytest.fixture(autouse=True)
def mock_pygments_lexers(monkeypatch):
    class MockLexer:
        pass

    def mock_get_lexer_for_mimetype(mime_type):
        if mime_type == 'application/json':
            return JsonLexer()
        elif mime_type == 'text/plain':
            return TextLexer()
        raise ClassNotFound

    def mock_get_lexer_by_name(name):
        if name == 'json':
            return JsonLexer()
        elif name == 'text':
            return TextLexer()
        raise ClassNotFound

    monkeypatch.setattr('pygments.lexers.get_lexer_for_mimetype', mock_get_lexer_for_mimetype)
    monkeypatch.setattr('pygments.lexers.get_lexer_by_name', mock_get_lexer_by_name)
