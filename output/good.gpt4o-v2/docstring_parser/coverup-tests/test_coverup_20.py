# file: docstring_parser/google.py:269-274
# asked: {"lines": [269, 274], "branches": []}
# gained: {"lines": [269, 274], "branches": []}

import pytest
from docstring_parser.google import parse
from docstring_parser.common import Docstring, DocstringMeta

def test_parse_empty_string():
    result = parse("")
    assert isinstance(result, Docstring)
    assert result.short_description is None
    assert result.long_description is None
    assert result.blank_after_short_description is False
    assert result.blank_after_long_description is False
    assert result.meta == []

def test_parse_with_short_description():
    docstring = "Short description."
    result = parse(docstring)
    assert isinstance(result, Docstring)
    assert result.short_description == "Short description."
    assert result.long_description is None
    assert result.blank_after_short_description is False
    assert result.blank_after_long_description is False
    assert result.meta == []

def test_parse_with_short_and_long_description():
    docstring = "Short description.\n\nLong description."
    result = parse(docstring)
    assert isinstance(result, Docstring)
    assert result.short_description == "Short description."
    assert result.long_description == "Long description."
    assert result.blank_after_short_description is True
    assert result.blank_after_long_description is False
    assert result.meta == []

def test_parse_with_meta(monkeypatch):
    docstring = """
    Short description.

    Args:
        param1: description of param1
        param2: description of param2
    """
    def mock_build_meta(self, part, title):
        return DocstringMeta(args=[part], description=title)

    monkeypatch.setattr("docstring_parser.google.GoogleParser._build_meta", mock_build_meta)
    result = parse(docstring)
    assert isinstance(result, Docstring)
    assert result.short_description == "Short description."
    assert result.long_description is None
    assert result.blank_after_short_description is True
    assert result.blank_after_long_description is False
    assert len(result.meta) == 2
    assert result.meta[0].args == ["param1: description of param1"]
    assert result.meta[0].description == "Args"
    assert result.meta[1].args == ["param2: description of param2"]
    assert result.meta[1].description == "Args"
