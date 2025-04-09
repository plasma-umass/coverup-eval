# file: docstring_parser/google.py:184-266
# asked: {"lines": [189, 190, 191, 194, 197, 198, 199, 200, 202, 203, 206, 207, 208, 209, 210, 211, 213, 214, 217, 218, 219, 220, 221, 222, 223, 225, 226, 227, 228, 229, 230, 231, 232, 235, 237, 238, 239, 240, 243, 244, 245, 247, 248, 249, 252, 253, 254, 255, 256, 258, 259, 260, 261, 262, 263, 264, 266], "branches": [[190, 191], [190, 194], [198, 199], [198, 202], [208, 209], [208, 217], [218, 219], [218, 220], [221, 222], [221, 223], [226, 227], [226, 231], [228, 229], [228, 230], [231, 232], [231, 235], [235, 237], [235, 266], [238, 239], [238, 240], [243, 247], [243, 252], [254, 255], [254, 258], [259, 260], [259, 261], [262, 235], [262, 263]]}
# gained: {"lines": [189, 190, 191, 194, 197, 198, 199, 200, 202, 203, 206, 207, 208, 209, 210, 211, 213, 214, 217, 218, 219, 220, 221, 222, 223, 225, 226, 227, 228, 230, 231, 235, 237, 238, 239, 240, 243, 244, 245, 247, 248, 249, 252, 253, 254, 258, 259, 261, 262, 263, 264, 266], "branches": [[190, 191], [190, 194], [198, 199], [198, 202], [208, 209], [218, 219], [218, 220], [221, 222], [221, 223], [226, 227], [226, 231], [228, 230], [231, 235], [235, 237], [235, 266], [238, 239], [238, 240], [243, 247], [243, 252], [254, 258], [259, 261], [262, 235], [262, 263]]}

import pytest
from docstring_parser.google import GoogleParser, Docstring, ParseError, SectionType
import inspect
import re
from collections import OrderedDict

@pytest.fixture
def parser():
    class TestGoogleParser(GoogleParser):
        titles_re = re.compile(r"^(Args|Returns|Raises):", re.MULTILINE)
        sections = {
            "Args": SectionType.MULTIPLE,
            "Returns": SectionType.SINGULAR,
            "Raises": SectionType.SINGULAR_OR_MULTIPLE,
        }

        def _build_meta(self, part, title):
            return {"title": title, "content": part}

    return TestGoogleParser()

def test_parse_empty_string(parser):
    result = parser.parse("")
    assert isinstance(result, Docstring)
    assert result.short_description is None

def test_parse_no_title(parser):
    docstring = "This is a short description.\n\nThis is a long description."
    result = parser.parse(docstring)
    assert result.short_description == "This is a short description."
    assert result.long_description == "This is a long description."
    assert not result.meta

def test_parse_with_title(parser):
    docstring = "This is a short description.\n\nArgs:\n    arg1: description of arg1"
    result = parser.parse(docstring)
    assert result.short_description == "This is a short description."
    assert result.meta == [{"title": "Args", "content": "arg1: description of arg1"}]

def test_parse_with_multiple_sections(parser):
    docstring = (
        "This is a short description.\n\nArgs:\n    arg1: description of arg1\n\n"
        "Returns:\n    description of return value\n\nRaises:\n    ValueError: if error"
    )
    result = parser.parse(docstring)
    assert result.short_description == "This is a short description."
    assert result.meta == [
        {"title": "Args", "content": "arg1: description of arg1"},
        {"title": "Returns", "content": "description of return value"},
        {"title": "Raises", "content": "ValueError: if error"},
    ]

def test_parse_with_incorrect_indent(parser):
    docstring = (
        "This is a short description.\n\nArgs:\narg1: description of arg1"
    )
    with pytest.raises(ParseError, match="Can't infer indent from"):
        parser.parse(docstring)

def test_parse_with_no_specification(parser):
    docstring = (
        "This is a short description.\n\nArgs:\n    arg1: description of arg1\n\n"
        "Returns:\n    No return value"
    )
    result = parser.parse(docstring)
    assert result.meta == [
        {"title": "Args", "content": "arg1: description of arg1"},
        {"title": "Returns", "content": "No return value"},
    ]
