# file: docstring_parser/numpydoc.py:48-77
# asked: {"lines": [48, 49, 58, 59, 60, 62, 63, 69, 71, 77], "branches": []}
# gained: {"lines": [48, 49, 58, 59, 60, 62, 63, 69, 71, 77], "branches": []}

import pytest
from docstring_parser.numpydoc import Section, DocstringMeta
import inspect

def test_section_init():
    section = Section("Parameters", "param")
    assert section.title == "Parameters"
    assert section.key == "param"

def test_section_title_pattern():
    section = Section("Parameters", "param")
    expected_pattern = r"^(Parameters)\s*?\n{}\s*$".format("-" * len("Parameters"))
    assert section.title_pattern == expected_pattern

def test_section_parse():
    section = Section("Parameters", "param")
    text = """
    param1 : int
        Description of param1
    param2 : str
        Description of param2
    """
    cleaned_text = inspect.cleandoc(text)
    parsed = list(section.parse(cleaned_text))
    assert len(parsed) == 1
    assert parsed[0].args == ["param"]
    assert parsed[0].description == cleaned_text

@pytest.fixture(autouse=True)
def clean_up(monkeypatch):
    # Clean up or reset any state if necessary
    yield
    # Perform any necessary cleanup after tests
