# file: docstring_parser/numpydoc.py:157-170
# asked: {"lines": [157, 158, 165, 166, 167, 168, 169], "branches": []}
# gained: {"lines": [157, 158, 165, 166, 167, 168, 169], "branches": []}

import pytest
from docstring_parser.numpydoc import RaisesSection, DocstringRaises

@pytest.fixture
def raises_section():
    return RaisesSection(title="Raises", key="raises")

def test_raises_section_parse_item(raises_section):
    key = "ValueError"
    value = "A description of what might raise ValueError"
    
    result = raises_section._parse_item(key, value)
    
    assert isinstance(result, DocstringRaises)
    assert result.args == [raises_section.key, key]
    assert result.description == "A description of what might raise ValueError"
    assert result.type_name == key

def test_raises_section_parse_item_empty_key(raises_section):
    key = ""
    value = "A description of what might raise an unspecified error"
    
    result = raises_section._parse_item(key, value)
    
    assert isinstance(result, DocstringRaises)
    assert result.args == [raises_section.key, key]
    assert result.description == "A description of what might raise an unspecified error"
    assert result.type_name is None
