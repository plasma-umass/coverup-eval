# file docstring_parser/numpydoc.py:257-264
# lines [257, 262, 263, 264]
# branches []

import pytest
from docstring_parser.numpydoc import NumpydocParser, Section

def test_numpydoc_parser_init_with_custom_sections():
    custom_sections = [
        Section("Custom Section 1", "custom_section_1"),
        Section("Custom Section 2", "custom_section_2")
    ]
    parser = NumpydocParser(sections=custom_sections)
    assert isinstance(parser.sections, dict)
    assert "Custom Section 1" in parser.sections
    assert "Custom Section 2" in parser.sections
    assert parser.sections["Custom Section 1"].title == "Custom Section 1"
    assert parser.sections["Custom Section 2"].title == "Custom Section 2"

def test_numpydoc_parser_init_with_default_sections(mocker):
    mocker.patch('docstring_parser.numpydoc.DEFAULT_SECTIONS', new=[
        Section("Default Section 1", "default_section_1"),
        Section("Default Section 2", "default_section_2")
    ])
    parser = NumpydocParser()
    assert isinstance(parser.sections, dict)
    assert "Default Section 1" in parser.sections
    assert "Default Section 2" in parser.sections
    assert parser.sections["Default Section 1"].title == "Default Section 1"
    assert parser.sections["Default Section 2"].title == "Default Section 2"
