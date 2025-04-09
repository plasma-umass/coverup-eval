# file: docstring_parser/parser.py:7-25
# asked: {"lines": [7, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], "branches": [[15, 16], [15, 17], [18, 19], [18, 23], [23, 24], [23, 25]]}
# gained: {"lines": [7, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], "branches": [[15, 16], [15, 17], [18, 19], [18, 23], [23, 24], [23, 25]]}

import pytest
from docstring_parser.common import Docstring, ParseError
from docstring_parser.styles import STYLES, Style
from docstring_parser.parser import parse

def test_parse_with_specific_style(monkeypatch):
    def mock_style_parser(text):
        return Docstring()

    monkeypatch.setitem(STYLES, Style.google, mock_style_parser)
    result = parse("Example docstring", style=Style.google)
    assert isinstance(result, Docstring)

def test_parse_with_auto_style(monkeypatch):
    def mock_style_parser(text):
        return Docstring()

    monkeypatch.setitem(STYLES, Style.google, mock_style_parser)
    monkeypatch.setitem(STYLES, Style.rest, mock_style_parser)
    monkeypatch.setitem(STYLES, Style.numpydoc, mock_style_parser)
    
    result = parse("Example docstring", style=Style.auto)
    assert isinstance(result, Docstring)

def test_parse_with_auto_style_and_parse_error(monkeypatch):
    def mock_style_parser_raises(text):
        raise ParseError("Parsing error")

    def mock_style_parser(text):
        return Docstring()

    monkeypatch.setitem(STYLES, Style.google, mock_style_parser_raises)
    monkeypatch.setitem(STYLES, Style.rest, mock_style_parser)
    monkeypatch.setitem(STYLES, Style.numpydoc, mock_style_parser_raises)
    
    result = parse("Example docstring", style=Style.auto)
    assert isinstance(result, Docstring)

def test_parse_with_all_styles_raising_errors(monkeypatch):
    def mock_style_parser_raises(text):
        raise ParseError("Parsing error")

    monkeypatch.setitem(STYLES, Style.google, mock_style_parser_raises)
    monkeypatch.setitem(STYLES, Style.rest, mock_style_parser_raises)
    monkeypatch.setitem(STYLES, Style.numpydoc, mock_style_parser_raises)
    
    with pytest.raises(ParseError):
        parse("Example docstring", style=Style.auto)
