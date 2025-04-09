# file docstring_parser/numpydoc.py:104-114
# lines [104, 105, 112, 113, 114]
# branches []

import re
import pytest
from docstring_parser.numpydoc import _SphinxSection

class MockSphinxSection(_SphinxSection):
    def __init__(self):
        super().__init__("example", "example_key")

def test_sphinx_section_title_pattern():
    mock_section = MockSphinxSection()
    title_pattern = mock_section.title_pattern
    assert re.match(title_pattern, ".. example::") is not None
    assert re.match(title_pattern, ".. example:: something") is not None
    assert re.match(title_pattern, ".. example::\nsomething") is not None
    assert re.match(title_pattern, ".. notexample:: something") is None
