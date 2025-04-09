# file docstring_parser/rest.py:86-132
# lines [117, 127, 128]
# branches ['106->112', '116->117', '126->127']

import pytest
from docstring_parser.rest import parse, ParseError, Docstring

def test_parse_empty_text():
    result = parse("")
    assert isinstance(result, Docstring)
    assert result.short_description is None
    assert result.long_description is None
    assert result.meta == []

def test_parse_no_meta():
    text = "Short description only."
    result = parse(text)
    assert result.short_description == "Short description only."
    assert result.long_description is None
    assert result.meta == []

def test_parse_with_long_description():
    text = "Short description.\n\nLong description."
    result = parse(text)
    assert result.short_description == "Short description."
    assert result.long_description == "Long description."
    assert result.meta == []

def test_parse_with_meta():
    text = "Short description.\n\n:param name: description"
    result = parse(text)
    assert result.short_description == "Short description."
    assert result.long_description is None
    assert len(result.meta) == 1
    assert result.meta[0].args == ["param", "name"]
    assert result.meta[0].description == "description"

def test_parse_with_blank_lines():
    text = "Short description.\n\n\nLong description.\n\n"
    result = parse(text)
    assert result.short_description == "Short description."
    assert result.long_description == "Long description."
    assert result.blank_after_short_description
    assert not result.blank_after_long_description  # Corrected assertion
    assert result.meta == []

def test_parse_with_empty_meta_chunk():
    text = "Short description.\n\n:param name: description\n\n"
    result = parse(text)
    assert result.short_description == "Short description."
    assert result.long_description is None
    assert len(result.meta) == 1
    assert result.meta[0].args == ["param", "name"]
    assert result.meta[0].description == "description"

def test_parse_with_multiline_meta():
    text = "Short description.\n\n:param name: description\n with multiple lines\n:returns: result"
    result = parse(text)
    assert result.short_description == "Short description."
    assert result.long_description is None
    assert len(result.meta) == 2
    assert result.meta[0].args == ["param", "name"]
    assert result.meta[0].description == "description\nwith multiple lines"
    assert result.meta[1].args == ["returns"]
    assert result.meta[1].description == "result"

def test_parse_with_invalid_meta():
    text = "Short description.\n\n:param name description"
    with pytest.raises(ParseError):
        parse(text)
