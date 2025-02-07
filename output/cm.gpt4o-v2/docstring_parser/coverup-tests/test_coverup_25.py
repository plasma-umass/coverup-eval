# file: docstring_parser/google.py:184-266
# asked: {"lines": [222, 229, 232, 239, 247, 248, 249, 255, 256], "branches": [[221, 222], [228, 229], [231, 232], [238, 239], [243, 247], [254, 255]]}
# gained: {"lines": [222, 239], "branches": [[221, 222], [238, 239]]}

import pytest
import re
from docstring_parser.google import GoogleParser
from docstring_parser.common import ParseError, Docstring

@pytest.fixture
def parser(mocker):
    parser = GoogleParser()
    mocker.patch.object(parser, 'titles_re', re.compile(r'(?P<title>Args|Returns|Raises):'))
    mocker.patch.object(parser, 'sections', {'Args': mocker.Mock(type='SINGULAR'), 'Returns': mocker.Mock(type='SINGULAR'), 'Raises': mocker.Mock(type='SINGULAR')})
    return parser

def test_parse_empty_text(parser):
    result = parser.parse("")
    assert isinstance(result, Docstring)
    assert result.short_description is None
    assert result.long_description is None
    assert result.meta == []

def test_parse_no_matches(parser):
    result = parser.parse("Description\n\n")
    assert isinstance(result, Docstring)
    assert result.short_description == "Description"
    assert result.long_description is None
    assert result.meta == []

def test_parse_with_matches(parser):
    result = parser.parse("Description\n\nArgs:\n    param1: description\nReturns:\n    result: description\n")
    assert isinstance(result, Docstring)
    assert result.short_description == "Description"
    assert result.long_description is None
    assert len(result.meta) == 2

def test_parse_no_indent_match(parser):
    with pytest.raises(ParseError, match="Can't infer indent from"):
        parser.parse("Description\n\nArgs:\nparam1: description\n")

def test_parse_no_specification(parser):
    with pytest.raises(ParseError, match='Can\'t infer indent from ""'):
        parser.parse("Description\n\nArgs:\n    param1: description\nReturns:")

def test_parse_singular_element(parser):
    result = parser.parse("Description\n\nArgs:\n    param1: description\n")
    assert isinstance(result, Docstring)
    assert result.short_description == "Description"
    assert result.long_description is None
    assert len(result.meta) == 1
