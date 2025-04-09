# file: docstring_parser/rest.py:86-132
# asked: {"lines": [86, 91, 92, 93, 95, 96, 97, 98, 99, 101, 102, 104, 105, 106, 107, 108, 109, 110, 112, 113, 115, 116, 117, 118, 119, 120, 121, 122, 124, 125, 126, 127, 128, 130, 132], "branches": [[92, 93], [92, 95], [97, 98], [97, 101], [106, 107], [106, 112], [112, 115], [112, 132], [116, 117], [116, 118], [126, 127], [126, 130]]}
# gained: {"lines": [86, 91, 92, 93, 95, 96, 97, 98, 99, 101, 102, 104, 105, 106, 107, 108, 109, 110, 112, 113, 115, 116, 118, 119, 120, 121, 122, 124, 125, 126, 130, 132], "branches": [[92, 93], [92, 95], [97, 98], [97, 101], [106, 107], [106, 112], [112, 115], [112, 132], [116, 118], [126, 130]]}

import pytest
from docstring_parser.rest import parse
from docstring_parser.common import Docstring, ParseError

def test_parse_empty_string():
    result = parse("")
    assert isinstance(result, Docstring)
    assert result.short_description is None
    assert result.long_description is None
    assert result.blank_after_short_description is False
    assert result.blank_after_long_description is False
    assert result.meta == []

def test_parse_only_short_description():
    result = parse("Short description.")
    assert isinstance(result, Docstring)
    assert result.short_description == "Short description."
    assert result.long_description is None
    assert result.blank_after_short_description is False
    assert result.blank_after_long_description is False
    assert result.meta == []

def test_parse_short_and_long_description():
    result = parse("Short description.\n\nLong description.")
    assert isinstance(result, Docstring)
    assert result.short_description == "Short description."
    assert result.long_description == "Long description."
    assert result.blank_after_short_description is True
    assert result.blank_after_long_description is False
    assert result.meta == []

def test_parse_with_meta():
    result = parse("Short description.\n\n:param str name: The name of the person.\n:returns: A greeting string.")
    assert isinstance(result, Docstring)
    assert result.short_description == "Short description."
    assert result.long_description is None
    assert result.blank_after_short_description is True
    assert result.blank_after_long_description is False
    assert len(result.meta) == 2
    assert result.meta[0].args == ["param", "str", "name"]
    assert result.meta[0].description == "The name of the person."
    assert result.meta[1].args == ["returns"]
    assert result.meta[1].description == "A greeting string."

def test_parse_error_in_meta():
    with pytest.raises(ParseError, match='Error parsing meta information near ":param str name".'):
        parse("Short description.\n\n:param str name")

def test_parse_with_blank_lines():
    result = parse("Short description.\n\n\nLong description.\n\n")
    assert isinstance(result, Docstring)
    assert result.short_description == "Short description."
    assert result.long_description == "Long description."
    assert result.blank_after_short_description is True
    assert result.blank_after_long_description is False
    assert result.meta == []
