# file docstring_parser/google.py:89-114
# lines []
# branches ['107->114']

import pytest
from unittest.mock import MagicMock
from docstring_parser.google import GoogleParser, SectionType, DocstringMeta
import inspect

@pytest.fixture
def google_parser():
    parser = GoogleParser()
    parser.sections = {
        "test_section": MagicMock(type=SectionType.MULTIPLE)
    }
    return parser

def test_build_meta_with_description(google_parser):
    text = "param: This is a description\n    with multiple lines."
    title = "test_section"
    
    google_parser._build_multi_meta = MagicMock(return_value=DocstringMeta(args=["param"], description="This is a description\nwith multiple lines."))
    
    result = google_parser._build_meta(text, title)
    
    assert isinstance(result, DocstringMeta)
    assert result.args[0] == "param"
    assert result.description == "This is a description\nwith multiple lines."

def test_build_meta_without_description(google_parser):
    text = "param:This is a single line description."
    title = "test_section"
    
    google_parser._build_multi_meta = MagicMock(return_value=DocstringMeta(args=["param"], description="This is a single line description."))
    
    result = google_parser._build_meta(text, title)
    
    assert isinstance(result, DocstringMeta)
    assert result.args[0] == "param"
    assert result.description == "This is a single line description."

def test_build_meta_with_empty_description(google_parser):
    text = "param:"
    title = "test_section"
    
    google_parser._build_multi_meta = MagicMock(return_value=DocstringMeta(args=["param"], description=""))
    
    result = google_parser._build_meta(text, title)
    
    assert isinstance(result, DocstringMeta)
    assert result.args[0] == "param"
    assert result.description == ""
