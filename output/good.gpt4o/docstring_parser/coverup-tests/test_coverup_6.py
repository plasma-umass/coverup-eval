# file docstring_parser/numpydoc.py:48-77
# lines [48, 49, 58, 59, 60, 62, 63, 69, 71, 77]
# branches []

import pytest
from unittest.mock import patch
from docstring_parser.numpydoc import Section, DocstringMeta

@pytest.fixture
def section():
    return Section(title="Parameters", key="param")

def test_section_title_pattern(section):
    pattern = section.title_pattern
    assert pattern == r"^(Parameters)\s*?\n{}\s*$".format("-" * len("Parameters"))

def test_section_parse(section):
    text = "    param1 : int\n        Description of param1"
    with patch('docstring_parser.numpydoc._clean_str', return_value="param1 : int\nDescription of param1") as mock_clean_str:
        result = list(section.parse(text))
        assert len(result) == 1
        assert isinstance(result[0], DocstringMeta)
        assert result[0].args == ["param"]
        assert result[0].description == "param1 : int\nDescription of param1"
        mock_clean_str.assert_called_once_with(text)
