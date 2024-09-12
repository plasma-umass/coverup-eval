# file: docstring_parser/numpydoc.py:48-77
# asked: {"lines": [48, 49, 58, 59, 60, 62, 63, 69, 71, 77], "branches": []}
# gained: {"lines": [48, 49, 58, 59, 60, 62, 63, 69, 71, 77], "branches": []}

import pytest
from docstring_parser.common import DocstringMeta
from docstring_parser.numpydoc import Section

def test_section_init():
    section = Section("Parameters", "param")
    assert section.title == "Parameters"
    assert section.key == "param"

def test_section_title_pattern():
    section = Section("Parameters", "param")
    expected_pattern = r"^(Parameters)\s*?\n{}\s*$".format("-" * len("Parameters"))
    assert section.title_pattern == expected_pattern

def test_section_parse(mocker):
    section = Section("Parameters", "param")
    mock_clean_str = mocker.patch("docstring_parser.numpydoc._clean_str", return_value="cleaned text")
    result = list(section.parse("some text"))
    mock_clean_str.assert_called_once_with("some text")
    assert len(result) == 1
    assert isinstance(result[0], DocstringMeta)
    assert result[0].args == ["param"]
    assert result[0].description == "cleaned text"
