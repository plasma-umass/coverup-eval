# file: docstring_parser/numpydoc.py:48-77
# asked: {"lines": [48, 49, 58, 59, 60, 62, 63, 69, 71, 77], "branches": []}
# gained: {"lines": [48, 49, 58, 59, 60, 62, 63, 69, 71, 77], "branches": []}

import pytest
from docstring_parser.numpydoc import Section, DocstringMeta
import inspect

@pytest.fixture
def section():
    return Section(title="Parameters", key="param")

def test_section_init(section):
    assert section.title == "Parameters"
    assert section.key == "param"

def test_title_pattern(section):
    expected_pattern = r"^(Parameters)\s*?\n{}\s*$".format("-" * len("Parameters"))
    assert section.title_pattern == expected_pattern

def test_parse(section, mocker):
    text = """
    param1 : int
        Description of param1
    param2 : str
        Description of param2
    """
    cleaned_text = inspect.cleandoc(text)
    mock_clean_str = mocker.patch('docstring_parser.numpydoc._clean_str', return_value=cleaned_text)
    result = list(section.parse(text))
    
    assert len(result) == 1
    assert isinstance(result[0], DocstringMeta)
    assert result[0].args == ["param"]
    assert result[0].description == cleaned_text
    mock_clean_str.assert_called_once_with(text)
