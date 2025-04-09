# file: docstring_parser/numpydoc.py:104-114
# asked: {"lines": [104, 105, 112, 113, 114], "branches": []}
# gained: {"lines": [104, 105, 112, 113], "branches": []}

import pytest
from docstring_parser.numpydoc import Section

class _SphinxSection(Section):
    """Base parser for numpydoc sections with sphinx-style syntax.

    E.g. sections that look like this:
        .. title:: something
            possibly over multiple lines
    """

    @property
    def title_pattern(self) -> str:
        return r"^\.\.\s*({})\s*::".format(self.title)

def test_sphinx_section_title_pattern():
    class TestSection(_SphinxSection):
        def __init__(self):
            super().__init__(title="test", key="test_key")

    section = TestSection()
    expected_pattern = r"^\.\.\s*(test)\s*::"
    assert section.title_pattern == expected_pattern
