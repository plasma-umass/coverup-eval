# file docstring_parser/numpydoc.py:207-218
# lines [207, 208, 210, 211, 213, 214, 216, 217]
# branches ['213->214', '213->216']

import pytest
from docstring_parser.numpydoc import DeprecationSection
from docstring_parser.common import DocstringDeprecated
from unittest.mock import Mock

@pytest.fixture
def deprecation_section():
    return DeprecationSection('Deprecation', 'deprecation')

def test_deprecation_section_with_description(deprecation_section):
    text = "1.0\nThis feature is deprecated."
    deprecated_items = list(deprecation_section.parse(text))
    assert len(deprecated_items) == 1
    assert deprecated_items[0].version == "1.0"
    assert deprecated_items[0].description == "This feature is deprecated."

def test_deprecation_section_without_description(deprecation_section):
    text = "1.0"
    deprecated_items = list(deprecation_section.parse(text))
    assert len(deprecated_items) == 1
    assert deprecated_items[0].version == "1.0"
    assert deprecated_items[0].description is None
