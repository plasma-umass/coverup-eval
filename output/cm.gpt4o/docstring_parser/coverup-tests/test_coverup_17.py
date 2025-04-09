# file docstring_parser/numpydoc.py:104-114
# lines [104, 105, 112, 113, 114]
# branches []

import pytest
from docstring_parser.numpydoc import _SphinxSection

def test_sphinx_section_title_pattern():
    class TestSection(_SphinxSection):
        title = "title"

    section = TestSection(title="title", key="key")
    assert section.title_pattern == r"^\.\.\s*(title)\s*::"
