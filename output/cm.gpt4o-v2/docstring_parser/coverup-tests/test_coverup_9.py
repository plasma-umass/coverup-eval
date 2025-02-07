# file: docstring_parser/google.py:175-182
# asked: {"lines": [175, 181, 182], "branches": []}
# gained: {"lines": [175, 181, 182], "branches": []}

import pytest
from docstring_parser.google import GoogleParser
from collections import namedtuple

Section = namedtuple('Section', 'title key type')

def test_add_section():
    parser = GoogleParser(sections=[])
    new_section = Section(title="New Section", key="new_key", type="new_type")
    
    parser.add_section(new_section)
    
    assert "New Section" in parser.sections
    assert parser.sections["New Section"] == new_section
