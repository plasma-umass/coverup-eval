# file docstring_parser/numpydoc.py:257-264
# lines [257, 262, 263, 264]
# branches []

import pytest
from unittest import mock
from docstring_parser.numpydoc import NumpydocParser, Section

DEFAULT_SECTIONS = [
    Section(key="parameters", title="Parameters"),
    Section(key="returns", title="Returns"),
    Section(key="examples", title="Examples"),
]

def test_numpydoc_parser_with_custom_sections():
    custom_sections = [
        Section(key="custom1", title="CustomSection1"),
        Section(key="custom2", title="CustomSection2"),
    ]
    parser = NumpydocParser(sections=custom_sections)
    assert "CustomSection1" in parser.sections
    assert "CustomSection2" in parser.sections
    assert "Parameters" not in parser.sections

def test_numpydoc_parser_with_default_sections():
    parser = NumpydocParser()
    assert "Parameters" in parser.sections
    assert "Returns" in parser.sections
    assert "Examples" in parser.sections

@pytest.fixture(autouse=True)
def mock_default_sections(mocker):
    mocker.patch('docstring_parser.numpydoc.DEFAULT_SECTIONS', DEFAULT_SECTIONS)
