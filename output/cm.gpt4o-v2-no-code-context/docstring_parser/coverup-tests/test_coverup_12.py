# file: docstring_parser/google.py:89-114
# asked: {"lines": [89, 97, 99, 100, 101, 102, 103, 106, 107, 108, 109, 110, 111, 112, 114], "branches": [[99, 103], [99, 106], [107, 108], [107, 114], [109, 110], [109, 112]]}
# gained: {"lines": [89, 97, 99, 100, 101, 102, 103, 106, 107, 108, 109, 110, 111, 112, 114], "branches": [[99, 103], [99, 106], [107, 108], [109, 110], [109, 112]]}

import pytest
from docstring_parser.google import GoogleParser, SectionType, DocstringMeta
import inspect

@pytest.fixture
def parser():
    class MockSection:
        def __init__(self, type):
            self.type = type

    class MockGoogleParser(GoogleParser):
        def __init__(self):
            self.sections = {
                "params": MockSection(SectionType.SINGULAR_OR_MULTIPLE),
                "returns": MockSection(SectionType.SINGULAR),
                "raises": MockSection(SectionType.MULTIPLE),
            }

        def _build_single_meta(self, section, text):
            return DocstringMeta(args=[text], description="single")

        def _build_multi_meta(self, section, before, desc):
            return DocstringMeta(args=[before], description=desc)

    return MockGoogleParser()

def test_build_meta_singular_or_multiple(parser):
    result = parser._build_meta("param1: description", "params")
    assert result.description == "description"
    assert result.args == ["param1"]

def test_build_meta_singular(parser):
    result = parser._build_meta("return description", "returns")
    assert result.description == "single"
    assert result.args == ["return description"]

def test_build_meta_multiple_with_colon(parser):
    result = parser._build_meta("exception: description", "raises")
    assert result.description == "description"
    assert result.args == ["exception"]

def test_build_meta_multiple_with_colon_and_newline(parser):
    result = parser._build_meta("exception: description\nwith newline", "raises")
    assert result.description == "description\nwith newline"
    assert result.args == ["exception"]

def test_build_meta_multiple_with_colon_and_newline_and_spaces(parser):
    result = parser._build_meta("exception: description\n    with newline", "raises")
    assert result.description == "description\nwith newline"
    assert result.args == ["exception"]
