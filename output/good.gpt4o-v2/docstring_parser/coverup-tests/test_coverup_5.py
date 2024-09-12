# file: docstring_parser/numpydoc.py:104-114
# asked: {"lines": [104, 105, 112, 113, 114], "branches": []}
# gained: {"lines": [104, 105, 112, 113, 114], "branches": []}

import pytest
from docstring_parser.numpydoc import _SphinxSection

def test_sphinx_section_title_pattern():
    section = _SphinxSection(title="Example", key="example")
    expected_pattern = r"^\.\.\s*(Example)\s*::"
    assert section.title_pattern == expected_pattern
