# file docstring_parser/numpydoc.py:207-218
# lines [211, 213, 214, 216, 217]
# branches ['213->214', '213->216']

import pytest
from docstring_parser.numpydoc import DeprecationSection, DocstringDeprecated
import inspect

def test_deprecation_section_parse(mocker):
    # Mock the _clean_str function to return the input string for simplicity
    mocker.patch('docstring_parser.numpydoc._clean_str', side_effect=lambda x: x)

    # Create an instance of DeprecationSection with dummy title and key
    section = DeprecationSection(title="Deprecation Warning", key="deprecation")

    text = "1.0.0\nThis feature is deprecated."

    result = list(section.parse(text))

    assert len(result) == 1
    assert isinstance(result[0], DocstringDeprecated)
    assert result[0].version == "1.0.0"
    assert result[0].description == "This feature is deprecated."
    assert result[0].args == [section.key]

    # Test with no description
    text_no_desc = "1.0.0"
    result_no_desc = list(section.parse(text_no_desc))

    assert len(result_no_desc) == 1
    assert isinstance(result_no_desc[0], DocstringDeprecated)
    assert result_no_desc[0].version == "1.0.0"
    assert result_no_desc[0].description is None
    assert result_no_desc[0].args == [section.key]
