# file: docstring_parser/numpydoc.py:272-279
# asked: {"lines": [272, 278, 279], "branches": []}
# gained: {"lines": [272, 278, 279], "branches": []}

import pytest
from docstring_parser.numpydoc import NumpydocParser, Section

def test_add_section():
    parser = NumpydocParser()
    new_section = Section(title="New Section", key="new_section")
    
    parser.add_section(new_section)
    
    assert "New Section" in parser.sections
    assert parser.sections["New Section"] == new_section

    # Clean up
    del parser.sections["New Section"]
