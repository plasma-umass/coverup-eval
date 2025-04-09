# file: docstring_parser/google.py:269-274
# asked: {"lines": [269, 274], "branches": []}
# gained: {"lines": [269, 274], "branches": []}

import pytest
from docstring_parser.google import parse
from docstring_parser.common import Docstring, ParseError, DocstringParam

def test_parse_empty_string():
    result = parse("")
    assert isinstance(result, Docstring)
    assert result.short_description is None
    assert result.long_description is None
    assert result.meta == []

def test_parse_short_description():
    docstring = "Short description."
    result = parse(docstring)
    assert isinstance(result, Docstring)
    assert result.short_description == "Short description."
    assert result.long_description is None
    assert result.meta == []

def test_parse_short_and_long_description():
    docstring = "Short description.\n\nLong description."
    result = parse(docstring)
    assert isinstance(result, Docstring)
    assert result.short_description == "Short description."
    assert result.long_description == "Long description."
    assert result.meta == []

def test_parse_with_meta():
    docstring = """
    Short description.

    Args:
        param1: Description of param1
        param2: Description of param2
    """
    result = parse(docstring)
    assert isinstance(result, Docstring)
    assert result.short_description == "Short description."
    assert result.long_description is None
    assert len(result.meta) == 2
    assert isinstance(result.meta[0], DocstringParam)
    assert result.meta[0].arg_name == "param1"
    assert result.meta[0].description == "Description of param1"
    assert isinstance(result.meta[1], DocstringParam)
    assert result.meta[1].arg_name == "param2"
    assert result.meta[1].description == "Description of param2"

def test_parse_invalid_indent():
    docstring = """
    Short description.

    Args:
    param1: Description of param1
    """
    with pytest.raises(ParseError):
        parse(docstring)
