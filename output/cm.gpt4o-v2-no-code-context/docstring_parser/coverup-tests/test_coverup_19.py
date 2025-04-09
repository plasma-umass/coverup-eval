# file: docstring_parser/numpydoc.py:207-218
# asked: {"lines": [207, 208, 210, 211, 213, 214, 216, 217], "branches": [[213, 214], [213, 216]]}
# gained: {"lines": [207, 208, 210, 211, 213, 214, 216, 217], "branches": [[213, 214], [213, 216]]}

import pytest
from docstring_parser.numpydoc import DeprecationSection, DocstringDeprecated
import inspect

class MockDeprecationSection(DeprecationSection):
    def __init__(self):
        self.title = "Deprecation Warning"
        self.key = "deprecation"

def test_deprecation_section_parse_with_description():
    text = "1.0.0\nThis feature is deprecated."
    section = MockDeprecationSection()
    result = list(section.parse(text))
    
    assert len(result) == 1
    assert result[0].version == "1.0.0"
    assert result[0].description == "This feature is deprecated."
    assert result[0].args == [section.key]

def test_deprecation_section_parse_without_description():
    text = "1.0.0"
    section = MockDeprecationSection()
    result = list(section.parse(text))
    
    assert len(result) == 1
    assert result[0].version == "1.0.0"
    assert result[0].description is None
    assert result[0].args == [section.key]
