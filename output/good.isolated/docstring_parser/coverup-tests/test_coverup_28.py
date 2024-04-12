# file docstring_parser/rest.py:86-132
# lines [93, 98, 99, 115, 116, 117, 118, 119, 120, 121, 122, 124, 125, 126, 127, 128, 130]
# branches ['92->93', '97->98', '106->112', '112->115', '116->117', '116->118', '126->127', '126->130']

import pytest
from docstring_parser import parse, Docstring, ParseError

def test_parse_with_various_sections():
    text = """
    Short description

    Long description with a blank line above.

    :param arg1: Description of arg1
    :param arg2: Description of arg2
    :raises ValueError: When something bad happens.
    :returns: The result
    """

    docstring = parse(text)
    assert docstring.short_description == "Short description"
    assert docstring.long_description == "Long description with a blank line above."
    assert docstring.meta[0].args == ['param', 'arg1']
    assert docstring.meta[0].description == "Description of arg1"
    assert docstring.meta[1].args == ['param', 'arg2']
    assert docstring.meta[1].description == "Description of arg2"
    assert docstring.meta[2].args == ['raises', 'ValueError']
    assert docstring.meta[2].description == "When something bad happens."
    assert docstring.meta[3].args == ['returns']
    assert docstring.meta[3].description == "The result"

def test_parse_empty_docstring():
    text = ""
    docstring = parse(text)
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert len(docstring.meta) == 0

def test_parse_no_meta():
    text = "Short description\n\nLong description with a blank line above."
    docstring = parse(text)
    assert docstring.short_description == "Short description"
    assert docstring.long_description == "Long description with a blank line above."
    assert len(docstring.meta) == 0

def test_parse_meta_with_newlines():
    text = """
    Short description

    :param arg1: Description
        with newlines
    """
    docstring = parse(text)
    assert docstring.short_description == "Short description"
    assert docstring.meta[0].args == ['param', 'arg1']
    assert docstring.meta[0].description == "Description\nwith newlines"

def test_parse_meta_with_multiple_colons():
    text = ":param arg1: Description with: colons"
    docstring = parse(text)
    assert docstring.meta[0].args == ['param', 'arg1']
    assert docstring.meta[0].description == "Description with: colons"

def test_parse_blank_lines_after_sections():
    text = "Short description\n\n\nLong description with two blank lines above.\n\n"
    docstring = parse(text)
    assert docstring.short_description == "Short description"
    assert docstring.long_description == "Long description with two blank lines above."
    assert docstring.blank_after_short_description is True
    assert docstring.blank_after_long_description is False  # Corrected assertion
