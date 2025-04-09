# file: docstring_parser/numpydoc.py:157-170
# asked: {"lines": [157, 158, 165, 166, 167, 168, 169], "branches": []}
# gained: {"lines": [157, 158, 165, 166, 167, 168, 169], "branches": []}

import pytest
from docstring_parser.common import DocstringRaises
from docstring_parser.numpydoc import RaisesSection

class MockKVSection(RaisesSection):
    def __init__(self):
        self.title = "mock_title"
        self.key = "mock_key"

def _clean_str(value: str) -> str:
    return value.strip()

@pytest.fixture
def mock_raises_section():
    return MockKVSection()

def test_parse_item_with_non_empty_key(mock_raises_section):
    result = mock_raises_section._parse_item("ValueError", " A description ")
    assert isinstance(result, DocstringRaises)
    assert result.args == ["mock_key", "ValueError"]
    assert result.description == "A description"
    assert result.type_name == "ValueError"

def test_parse_item_with_empty_key(mock_raises_section):
    result = mock_raises_section._parse_item("", " A description ")
    assert isinstance(result, DocstringRaises)
    assert result.args == ["mock_key", ""]
    assert result.description == "A description"
    assert result.type_name is None
