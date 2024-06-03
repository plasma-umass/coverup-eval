# file docstring_parser/rest.py:86-132
# lines [86, 91, 92, 93, 95, 96, 97, 98, 99, 101, 102, 104, 105, 106, 107, 108, 109, 110, 112, 113, 115, 116, 117, 118, 119, 120, 121, 122, 124, 125, 126, 127, 128, 130, 132]
# branches ['92->93', '92->95', '97->98', '97->101', '106->107', '106->112', '112->115', '112->132', '116->117', '116->118', '126->127', '126->130']

import pytest
from docstring_parser.rest import parse, Docstring, ParseError
import inspect
import re

def test_parse_empty_text():
    result = parse("")
    assert isinstance(result, Docstring)
    assert result.short_description is None
    assert result.long_description is None
    assert result.meta == []

def test_parse_no_meta():
    text = """
    Short description.

    Long description.
    """
    result = parse(text)
    assert result.short_description == "Short description."
    assert result.long_description == "Long description."
    assert result.meta == []

def test_parse_with_meta():
    text = """
    Short description.

    Long description.

    :param name: description of the parameter
    :returns: description of the return value
    """
    result = parse(text)
    assert result.short_description == "Short description."
    assert result.long_description == "Long description."
    assert len(result.meta) == 2
    assert result.meta[0].args == ['param', 'name']
    assert result.meta[0].description == "description of the parameter"
    assert result.meta[1].args == ['returns']
    assert result.meta[1].description == "description of the return value"

def test_parse_incorrect_meta():
    text = """
    Short description.

    Long description.

    :param name description of the parameter
    """
    with pytest.raises(ParseError, match=r'Error parsing meta information near'):
        parse(text)

def test_parse_blank_lines():
    text = """
    Short description.

    Long description with blank lines.

    :param name: description of the parameter
    """
    result = parse(text)
    assert result.short_description == "Short description."
    assert result.long_description == "Long description with blank lines."
    assert result.blank_after_short_description is True
    assert result.blank_after_long_description is True
    assert len(result.meta) == 1
    assert result.meta[0].args == ['param', 'name']
    assert result.meta[0].description == "description of the parameter"
