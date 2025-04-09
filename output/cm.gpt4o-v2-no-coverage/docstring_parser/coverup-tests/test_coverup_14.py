# file: docstring_parser/numpydoc.py:104-114
# asked: {"lines": [104, 105, 112, 113, 114], "branches": []}
# gained: {"lines": [104, 105, 112, 113, 114], "branches": []}

import pytest
from docstring_parser.numpydoc import _SphinxSection

class MockSphinxSection(_SphinxSection):
    def __init__(self):
        super().__init__(title="mock_title", key="mock_key")

def test_sphinx_section_title_pattern():
    section = MockSphinxSection()
    expected_pattern = r"^\.\.\s*(mock_title)\s*::"
    
    assert section.title_pattern == expected_pattern
