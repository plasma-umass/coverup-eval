# file: docstring_parser/numpydoc.py:207-218
# asked: {"lines": [207, 208, 210, 211, 213, 214, 216, 217], "branches": [[213, 214], [213, 216]]}
# gained: {"lines": [207, 208, 210, 211, 213, 214, 216, 217], "branches": [[213, 214], [213, 216]]}

import pytest
from docstring_parser.common import DocstringDeprecated
from docstring_parser.numpydoc import DeprecationSection

class MockSphinxSection:
    key = "deprecation"

def _clean_str(s):
    return s.strip() if s else None

@pytest.fixture
def deprecation_section(monkeypatch):
    monkeypatch.setattr("docstring_parser.numpydoc._SphinxSection", MockSphinxSection)
    monkeypatch.setattr("docstring_parser.numpydoc._clean_str", _clean_str)
    return DeprecationSection(title="Deprecation Warning", key="deprecation")

def test_parse_with_description(deprecation_section):
    text = "v1.0\nThis is deprecated."
    result = list(deprecation_section.parse(text))
    assert len(result) == 1
    assert result[0].version == "v1.0"
    assert result[0].description == "This is deprecated."
    assert result[0].args == ["deprecation"]

def test_parse_without_description(deprecation_section):
    text = "v1.0"
    result = list(deprecation_section.parse(text))
    assert len(result) == 1
    assert result[0].version == "v1.0"
    assert result[0].description is None
    assert result[0].args == ["deprecation"]

def test_parse_empty(deprecation_section):
    text = ""
    result = list(deprecation_section.parse(text))
    assert len(result) == 1
    assert result[0].version is None
    assert result[0].description is None
    assert result[0].args == ["deprecation"]
