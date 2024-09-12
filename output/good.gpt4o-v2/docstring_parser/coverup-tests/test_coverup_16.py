# file: docstring_parser/rest.py:86-132
# asked: {"lines": [86, 91, 92, 93, 95, 96, 97, 98, 99, 101, 102, 104, 105, 106, 107, 108, 109, 110, 112, 113, 115, 116, 117, 118, 119, 120, 121, 122, 124, 125, 126, 127, 128, 130, 132], "branches": [[92, 93], [92, 95], [97, 98], [97, 101], [106, 107], [106, 112], [112, 115], [112, 132], [116, 117], [116, 118], [126, 127], [126, 130]]}
# gained: {"lines": [86, 91, 92, 93, 95, 96, 97, 98, 99, 101, 102, 104, 105, 106, 107, 108, 109, 110, 112, 113, 115, 116, 118, 119, 120, 121, 122, 124, 125, 126, 127, 128, 130, 132], "branches": [[92, 93], [92, 95], [97, 98], [97, 101], [106, 107], [106, 112], [112, 115], [112, 132], [116, 118], [126, 127], [126, 130]]}

import pytest
from docstring_parser.rest import parse, ParseError
from docstring_parser.common import Docstring, DocstringMeta, DocstringParam, DocstringReturns, DocstringRaises

def test_parse_empty_string():
    result = parse("")
    assert isinstance(result, Docstring)
    assert result.short_description is None
    assert result.long_description is None
    assert result.meta == []

def test_parse_only_description():
    text = "Short description."
    result = parse(text)
    assert result.short_description == "Short description."
    assert result.long_description is None
    assert result.meta == []

def test_parse_description_with_long_description():
    text = "Short description.\n\nLong description."
    result = parse(text)
    assert result.short_description == "Short description."
    assert result.long_description == "Long description."
    assert result.meta == []

def test_parse_with_meta():
    text = "Short description.\n\n:param str name: The name\n:returns: The result"
    result = parse(text)
    assert result.short_description == "Short description."
    assert result.long_description is None
    assert len(result.meta) == 2
    assert isinstance(result.meta[0], DocstringParam)
    assert result.meta[0].arg_name == "name"
    assert result.meta[0].type_name == "str"
    assert result.meta[0].description == "The name"
    assert isinstance(result.meta[1], DocstringReturns)
    assert result.meta[1].description == "The result"

def test_parse_with_invalid_meta():
    text = "Short description.\n\n:param name The name"
    with pytest.raises(ParseError, match='Error parsing meta information near ":param name The name".'):
        parse(text)

def test_parse_with_multiline_meta():
    text = "Short description.\n\n:param str name: The name\n    continues on the next line\n:returns: The result"
    result = parse(text)
    assert result.short_description == "Short description."
    assert result.long_description is None
    assert len(result.meta) == 2
    assert isinstance(result.meta[0], DocstringParam)
    assert result.meta[0].arg_name == "name"
    assert result.meta[0].type_name == "str"
    assert result.meta[0].description == "The name\ncontinues on the next line"
    assert isinstance(result.meta[1], DocstringReturns)
    assert result.meta[1].description == "The result"
