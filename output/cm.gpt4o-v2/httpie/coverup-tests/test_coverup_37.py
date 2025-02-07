# file: httpie/output/formatters/colors.py:109-156
# asked: {"lines": [109, 111, 112, 115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}
# gained: {"lines": [109, 111, 112, 115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}

import pytest
import json
from pygments.lexers import get_lexer_for_mimetype, get_lexer_by_name, TextLexer
from pygments.util import ClassNotFound
from httpie.output.formatters.colors import get_lexer

def test_get_lexer_with_plain_mime():
    lexer = get_lexer('text/plain')
    assert lexer is not None
    assert lexer.name == 'Text only'

def test_get_lexer_with_json_mime():
    lexer = get_lexer('application/json')
    assert lexer is not None
    assert lexer.name == 'JSON'

def test_get_lexer_with_unknown_mime():
    lexer = get_lexer('unknown/mime')
    assert lexer is not None
    assert lexer.name == 'MIME'

def test_get_lexer_with_subtype_suffix():
    lexer = get_lexer('application/vnd.api+json')
    assert lexer is not None
    assert lexer.name == 'JSON'

def test_get_lexer_with_explicit_json_and_valid_body():
    body = json.dumps({"key": "value"})
    lexer = get_lexer('text/plain', explicit_json=True, body=body)
    assert lexer is not None
    assert lexer.name == 'JSON'

def test_get_lexer_with_explicit_json_and_invalid_body():
    body = "not a json"
    lexer = get_lexer('text/plain', explicit_json=True, body=body)
    assert lexer is not None
    assert lexer.name == 'Text only'

def test_get_lexer_with_explicit_json_and_empty_body():
    lexer = get_lexer('text/plain', explicit_json=True, body='')
    assert lexer is not None
    assert lexer.name == 'Text only'
