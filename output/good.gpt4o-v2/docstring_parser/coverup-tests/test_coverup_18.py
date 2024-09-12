# file: docstring_parser/numpydoc.py:157-170
# asked: {"lines": [157, 158, 165, 166, 167, 168, 169], "branches": []}
# gained: {"lines": [157, 158, 165, 166, 167, 168, 169], "branches": []}

import pytest
from docstring_parser.numpydoc import RaisesSection
from docstring_parser.common import DocstringRaises

class MockKVSection:
    def __init__(self, title, key):
        self.title = title
        self.key = key

    def _clean_str(self, value):
        return value.strip()

@pytest.fixture
def mock_raises_section(monkeypatch):
    monkeypatch.setattr("docstring_parser.numpydoc._KVSection", MockKVSection)
    return RaisesSection("Raises", "raises")

def test_raises_section_parse_item(mock_raises_section):
    section = mock_raises_section
    key = "ValueError"
    value = "A description of what might raise ValueError"
    
    result = section._parse_item(key, value)
    
    assert isinstance(result, DocstringRaises)
    assert result.args == [section.key, key]
    assert result.description == "A description of what might raise ValueError"
    assert result.type_name == "ValueError"

def test_raises_section_parse_item_empty_key(mock_raises_section):
    section = mock_raises_section
    key = ""
    value = "A description with no specific error type"
    
    result = section._parse_item(key, value)
    
    assert isinstance(result, DocstringRaises)
    assert result.args == [section.key, key]
    assert result.description == "A description with no specific error type"
    assert result.type_name is None
