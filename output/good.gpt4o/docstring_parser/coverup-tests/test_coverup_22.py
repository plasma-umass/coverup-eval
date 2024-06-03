# file docstring_parser/numpydoc.py:173-198
# lines [173, 174, 183, 185, 186, 187, 188, 190, 192, 193, 194, 195, 196, 197]
# branches ['187->188', '187->190']

import pytest
from docstring_parser.numpydoc import ReturnsSection, DocstringReturns
import re

RETURN_KEY_REGEX = re.compile(r"(?P<name>\w+)\s*:\s*(?P<type>.+)")

@pytest.fixture
def mock_return_key_regex(mocker):
    return mocker.patch('docstring_parser.numpydoc.RETURN_KEY_REGEX', RETURN_KEY_REGEX)

def _clean_str(s: str) -> str:
    return s.strip()

def test_returns_section_parse_item_with_key(mock_return_key_regex):
    section = ReturnsSection(title="Returns", key="return_key")
    key = "result : int"
    value = "The result of the computation."
    
    result = section._parse_item(key, value)
    
    assert isinstance(result, DocstringReturns)
    assert result.args == ["return_key"]
    assert result.description == _clean_str(value)
    assert result.type_name == "int"
    assert result.is_generator == False
    assert result.return_name == "result"

def test_returns_section_parse_item_without_key(mock_return_key_regex):
    section = ReturnsSection(title="Returns", key="return_key")
    key = "int"
    value = "The result of the computation."
    
    result = section._parse_item(key, value)
    
    assert isinstance(result, DocstringReturns)
    assert result.args == ["return_key"]
    assert result.description == _clean_str(value)
    assert result.type_name == None
    assert result.is_generator == False
    assert result.return_name == None
