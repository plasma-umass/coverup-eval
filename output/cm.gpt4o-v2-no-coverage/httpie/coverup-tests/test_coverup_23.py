# file: httpie/output/formatters/colors.py:109-156
# asked: {"lines": [109, 111, 112, 115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}
# gained: {"lines": [109, 111, 112, 115, 116, 117, 118, 120, 121, 122, 123, 124, 129, 130, 133, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 147, 149, 150, 151, 152, 154, 156], "branches": [[117, 118], [117, 120], [129, 130], [129, 133], [134, 135], [134, 141], [141, 134], [141, 142], [147, 149], [147, 156]]}

import pytest
from pygments.lexers import get_lexer_for_mimetype, get_lexer_by_name
from pygments.lexers.special import TextLexer
from pygments.util import ClassNotFound
import json
from httpie.output.formatters.colors import get_lexer

def test_get_lexer_with_valid_mime_type(mocker):
    mocker.patch('pygments.lexers.get_lexer_for_mimetype', return_value='mock_lexer')
    lexer = get_lexer('application/json')
    assert lexer == 'mock_lexer'

def test_get_lexer_with_invalid_mime_type(mocker):
    mocker.patch('pygments.lexers.get_lexer_for_mimetype', side_effect=ClassNotFound)
    mocker.patch('pygments.lexers.get_lexer_by_name', side_effect=ClassNotFound)
    lexer = get_lexer('invalid/mime')
    assert lexer is None

def test_get_lexer_with_subtype_json(mocker):
    mocker.patch('pygments.lexers.get_lexer_for_mimetype', side_effect=ClassNotFound)
    mocker.patch('pygments.lexers.get_lexer_by_name', return_value='json_lexer')
    lexer = get_lexer('application/vnd.api+json')
    assert lexer == 'json_lexer'

def test_get_lexer_with_explicit_json_and_valid_body(mocker):
    mocker.patch('pygments.lexers.get_lexer_for_mimetype', side_effect=ClassNotFound)
    mocker.patch('pygments.lexers.get_lexer_by_name', side_effect=[ClassNotFound, 'json_lexer'])
    mocker.patch('json.loads', return_value={})
    lexer = get_lexer('text/plain', explicit_json=True, body='{"key": "value"}')
    assert lexer == 'json_lexer'

def test_get_lexer_with_explicit_json_and_invalid_body(mocker):
    mocker.patch('pygments.lexers.get_lexer_for_mimetype', side_effect=ClassNotFound)
    mocker.patch('pygments.lexers.get_lexer_by_name', side_effect=ClassNotFound)
    mocker.patch('json.loads', side_effect=ValueError)
    lexer = get_lexer('text/plain', explicit_json=True, body='invalid json')
    assert lexer is None

def test_get_lexer_with_text_lexer(mocker):
    mocker.patch('pygments.lexers.get_lexer_for_mimetype', return_value=TextLexer())
    lexer = get_lexer('text/plain')
    assert isinstance(lexer, TextLexer)
