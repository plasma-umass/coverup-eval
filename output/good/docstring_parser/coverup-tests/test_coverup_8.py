# file docstring_parser/numpydoc.py:48-77
# lines [48, 49, 58, 59, 60, 62, 63, 69, 71, 77]
# branches []

import pytest
from docstring_parser import DocstringMeta
from docstring_parser.numpydoc import Section

@pytest.fixture
def mock_section():
    return Section(title="Parameters", key="params")

def test_section_title_pattern(mock_section):
    pattern = mock_section.title_pattern
    assert pattern == r"^(Parameters)\s*?\n----------\s*$"

def test_section_parse(mock_section):
    text = "param1: int\n    Description of param1."
    result = list(mock_section.parse(text))
    assert len(result) == 1
    assert isinstance(result[0], DocstringMeta)
    assert result[0].args == ["params"]
    assert result[0].description == "param1: int\n    Description of param1."
