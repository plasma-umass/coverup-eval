# file: docstring_parser/google.py:89-114
# asked: {"lines": [], "branches": [[107, 114]]}
# gained: {"lines": [], "branches": [[107, 114]]}

import pytest
from docstring_parser.google import GoogleParser, SectionType, DocstringMeta
import inspect

class MockSection:
    def __init__(self, section_type, key=None):
        self.type = section_type
        self.key = key

@pytest.fixture
def parser(monkeypatch):
    parser = GoogleParser()
    sections = {
        "params": MockSection(SectionType.SINGULAR_OR_MULTIPLE, "param"),
        "returns": MockSection(SectionType.SINGULAR, "return")
    }
    monkeypatch.setattr(parser, 'sections', sections)
    return parser

def test_build_meta_with_desc(parser):
    text = "param: description\n with multiple lines"
    title = "params"
    result = parser._build_meta(text, title)
    assert isinstance(result, DocstringMeta)
    assert result.args[0] == "param"
    assert result.description == "description\nwith multiple lines"

def test_build_meta_without_desc(parser):
    text = "param:"
    title = "params"
    result = parser._build_meta(text, title)
    assert isinstance(result, DocstringMeta)
    assert result.args[0] == "param"
    assert result.description == ""

def test_build_meta_singular(parser):
    text = "return description"
    title = "returns"
    result = parser._build_meta(text, title)
    assert isinstance(result, DocstringMeta)
    assert result.description == "return description"
