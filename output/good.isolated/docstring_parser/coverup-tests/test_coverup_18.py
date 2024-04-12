# file docstring_parser/numpydoc.py:157-170
# lines [157, 158, 165, 166, 167, 168, 169]
# branches []

import pytest
from docstring_parser.numpydoc import RaisesSection
from docstring_parser.common import DocstringRaises

@pytest.fixture
def raises_section():
    return RaisesSection('Raises', 'raises')

def test_raises_section_parse_item_with_key(raises_section):
    key = "ValueError"
    value = "An error raised when invalid value is provided."
    result = raises_section._parse_item(key, value)
    assert isinstance(result, DocstringRaises)
    assert result.args == ['raises', key]
    assert result.description == value.strip()
    assert result.type_name == key

def test_raises_section_parse_item_without_key(raises_section):
    key = ""
    value = "A general exception."
    result = raises_section._parse_item(key, value)
    assert isinstance(result, DocstringRaises)
    assert result.args == ['raises', key]
    assert result.description == value.strip()
    assert result.type_name is None
